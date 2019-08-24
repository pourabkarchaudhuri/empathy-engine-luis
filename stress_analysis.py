# Stress Levels:
# 90 to 100 : Extreme/Angry
# 80 to 90 : Critical Shocks/Unresponsive
# 70 to 80 : Worried
# 50 to 70 : Slighly responsive
# Below 50 : Responsive

import random
intent_state = False
intent_state_name = None
global_intent_repeat = 0
is_completed = False

repeat_counter = 0

# is_repeat = False
def stress_analyzer(sentiment, intent, stress):
    trigger = None
    is_responsive = True
    global intent_state
    global intent_state_name
    global is_completed
    global repeat_counter
    if intent_state is not True:
        # print("Fresh Start")
        intent_state_name = None
        repeat_counter = 0
    else:
        if intent_state_name == intent:
            repeat_counter = repeat_counter + 1
            # print("Repeating Intent : {}".format(intent))
            if(stress>90):
                stress = stress + random.randint(1, 5)
                trigger = 'dont_annoy'
            elif stress>80 and stress<=90:
                trigger = None
                is_responsive = False
            elif stress>70 and stress<=80 :
                trigger = 'worry'
            elif stress>0 and stress<=70:
                trigger = None
        else:
            # print("New Intent : {}".format(intent))
            intent_state_name = None
            repeat_counter = 0

    reaction = ""
    
    intent_state = True
    # print("Repeat Counter : {}".format(repeat_counter))
    if repeat_counter > 1:
        # intent_state_name = None    
        stress = stress + random.randint(1, 5)
        # print("Stress due to repeat : {}".format(stress))
    else:
        intent_state_name = None
        if intent == "fallback":
            stress = stress + random.randint(1, 3)
        else:
            print("Stress : {}".format(stress))
            if stress<100:
                if sentiment=='negative':
                    stress = stress + random.randint(1, 5)
                elif sentiment=='positive':
                    stress = stress - random.randint(1, 5)
                elif sentiment=='supportive':
                    stress = stress - random.randint(1, 5)
                elif sentiment=='neutral':
                    stress = stress - random.randint(1, 2)
                else:
                    print("No change in stress")
            else:
                print("Full Stress")

    

    # print("Stress after change : {}, Sentiment : {}".format(stress, sentiment))

    if stress>=100:
        stress=95
    
    if stress>90:
        reaction = "extreme"
    elif stress>80 and stress<=90:
        reaction = "shock"
    elif stress>70 and stress<=80:
        reaction = "worried"
    elif stress>60 and stress<=70:
        reaction = "responsive"
    elif stress<=60:
        reaction = "relieved"
        is_completed = True

    # print("Current Stress Level {}, with Reaction {}".format(stress, reaction))
    # intent_state_name = intent
    

    # print("Resultant State Name is {}, State {}, Stress {}".format(intent_state_name, intent_state, stress))
    response = {
        'reaction':reaction,
        'stress': stress,
        'trigger': trigger,
        'responsive': is_responsive,
        'completion': is_completed,
        'repeat': intent_state_name
    }
    intent_state_name = intent
    is_completed = False
    print("Output Payload : ", response)
    return response

# stress_analyzer('negative', 'greetings', 78)
    