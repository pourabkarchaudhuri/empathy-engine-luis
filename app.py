from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import json
from textblob import TextBlob
import random
import sentiment_analysis
import stress_analysis
import luis

import os

DEFAULT_STRESS = 78

stress = DEFAULT_STRESS

with open('intents.json') as json_data:
    intents = json.load(json_data)

extraction_dict = ["Okay. Fine. I'll come with you. Just get me to safety. Let's go!", "Then what are we waiting for. Let's go!"]
fallback_dict = ["Please ask me something else!", "I dont think you should be asking me that", "I am not going to respond to that", "I dont want to talk about that. If you have any other questions then ok."]
repeat_dict = ['Stop repeating yourself!', "You are saying the same thing over and over again.", "Stop saying the same thing.", "I am in so much pain, and here you are asking me the same thing over and over again!"]

app = Flask(__name__)
CORS(app)

@app.route("/ml/api/v1.0/assistant", methods=['POST'])
def classify():
    global stress
    # ERROR_THRESHOLD = THRESHOLD

    context = None
    # print("Trigger")
    sentence = request.json['sentence']

    # print(sentence)
   
    nlu = json.loads(luis.luis_api(sentence))
    print(nlu)
    return_list = []
    # output_context = None
    entities = None
    # print("LUIS NLU Inference : ", nlu['topScoringIntent']['intent'])
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity * 100
    print("Sentiment", sentiment)
    sentiment = sentiment_analysis.sentiment_analyzer(sentence)
    print("Generated Sentiment", sentiment)
    intent_name = nlu['prediction']['topIntent']
    print("intentname", intent_name)
    score = nlu['prediction']['intents'][intent_name]['score']
    print("score", score)
    if intent_name == "None":
        print("Fallback detected")
        
        stress_payload = stress_analysis.stress_analyzer(sentiment['polarity'], 'fallback', stress)

        stress = stress_payload['stress']
        trigger = stress_payload['trigger']
        responsive = stress_payload['responsive']
        reaction = stress_payload['reaction']
        completion = stress_payload['completion']

        return_list.append({"query": sentence, "intent": "fallback", "response": random.choice(fallback_dict), "context": context, "probability": "{0:.2f}".format(score), "entities": entities, "sentiment":sentiment, "stress":stress, "trigger": trigger, "responsive":responsive, "reaction":reaction, 'completion':False})
       
        
    else:
        print("Inference Exists")
        
        stress_payload = stress_analysis.stress_analyzer(sentiment['polarity'], intent_name , stress)

        stress = stress_payload['stress']
        trigger = stress_payload['trigger']
        responsive = stress_payload['responsive']
        reaction = stress_payload['reaction']
        completion = stress_payload['completion']

        if completion is True:
            # print("Extraction completion event triggered!")
            return_list.append({"query": sentence, "intent": intent_name , "response": random.choice(extraction_dict), "context": context, "probability": "{0:.2f}".format(score), "entities": entities, "sentiment":sentiment, "stress":stress, "trigger":trigger, "responsive":responsive, "reaction":reaction, 'completion':completion})

        else:
            if stress_payload['repeat'] is not None:
                return_list.append({"query": sentence, "intent": intent_name , "response": random.choice(repeat_dict) + " " + "You are only talking about " + intent_name.replace("_", " "), "context": context, "probability": "{0:.2f}".format(score), "entities": entities, "sentiment":sentiment, "stress":stress, "trigger":trigger, "responsive":responsive, "reaction":reaction, 'completion':completion})
            
            else:              
                for x_tend in intents['intents']:
                    if intent_name == x_tend['tag']:
                        normal_response = random.choice(x_tend['responses'])
    
                        return_list.append({"query": sentence, "intent": intent_name , "response": normal_response, "context": context, "probability": "{0:.2f}".format(score), "entities": entities, "sentiment":sentiment, "stress":stress, "trigger":trigger, "responsive":responsive, "reaction":reaction, 'completion':completion})

    response = jsonify({"result":return_list, "error":None})
    # print("Completion Status : {}".format(completion))
    if completion:
        stress = DEFAULT_STRESS
        # print("Level complete. Resetting Stress to default {}".format(DEFAULT_STRESS))
        
    print("GLOBAL STRESS LEVEL : {}".format(stress))
    return response

#Implement Another API to RESET The stress value and threshold remotely
@app.route("/ml/api/v1.0/reset", methods=['GET'])
def reset():
    global stress
    stress = int(request.args.get('stress'))
    return jsonify({"result":stress, "error":None})


# running REST interface, port=3000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

