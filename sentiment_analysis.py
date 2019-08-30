from textblob import TextBlob
import math

def sentiment_analyzer(text, polarity, inferenced_polarity):

    inferenced_subjectivity = ""


    testimonial = TextBlob(text)
    polarity = round(testimonial.sentiment.polarity, 2)
    subjectivity = round(testimonial.sentiment.subjectivity, 2)

    if polarity==0.0:
        inferenced_polarity = 'neutral'
        # print("Negative")
    elif polarity<0.65 and polarity>0.00:
        # print("Neutral")
        inferenced_polarity = 'supportive'
    elif polarity>=0.65:
        inferenced_polarity = 'positive'
        # print("Positive")
    else:
        inferenced_polarity = 'negative'
        # print("Unrecognized")




    if subjectivity<0.45:
        inferenced_subjectivity = 'objective'

    elif subjectivity<0.65 and subjectivity>0.45:
        inferenced_subjectivity = 'neutral'

    elif subjectivity>=0.65:
        inferenced_subjectivity = 'subjective'

    else:
        inferenced_subjectivity = 'unrecognized'
    
    response = {
            'polarity': inferenced_polarity,
            'subjectivity': inferenced_subjectivity
        }
    return response
    


