from textblob import TextBlob
import math

def sentiment_analyzer(text, polarity, inferenced_polarity):

    inferenced_subjectivity = ""

    testimonial = TextBlob(text)

    subjectivity = round(testimonial.sentiment.subjectivity, 2)

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
    


