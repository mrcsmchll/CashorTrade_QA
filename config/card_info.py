from datetime import datetime


class Card:

    def __init__(self):
        self.number = "4242424242424242"
        self.exp_date = self.expiration_date()
        self.cvc = "123"

        self.address = "avenue testing"
        self.postal = "1832"
        self.city = "lomas"
    
    def expiration_date(self):
        month = datetime.today().month
        year = datetime.today().year + 1
        return str(month) + str(year)[-2:]