class RequestObject:
    def __init__(self, document, currencyFrom, currencyTo, amount, total):
        self.document = document
        self.currencyFrom = currencyFrom
        self.currencyTo = currencyTo
        self.amount = amount
        self.total = total
