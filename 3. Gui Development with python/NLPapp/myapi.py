import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('GwcxKZ06H0CEIDL5xOusv7O06Kq7ihIq9R6Hh6utr6c')

    def sentiment_analysis(self , text):
        response = paralleldots.sentiment(text)
        return response

    def ner_nlp(self , text):
        response = paralleldots.ner(text)
        return response