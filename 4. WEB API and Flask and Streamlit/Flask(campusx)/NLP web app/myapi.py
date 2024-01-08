import paralleldots
paralleldots.set_api_key('GwcxKZ06H0CEIDL5xOusv7O06Kq7ihIq9R6Hh6utr6c')
class API:
    def ner(self , text):
        result = paralleldots.ner(text)
        return result
