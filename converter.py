from request_object import RequestObject
class Converter:

    def makeConversion(newRequest: RequestObject):
        codeFrom = newRequest.currencyFrom
        codeTo = newRequest.currencyTo
        amountFrom = newRequest.amount

        data = newRequest.document.json()

        fromRate = data["conversion_rates"].get(codeFrom)
        toRate = data["conversion_rates"].get(codeTo)

        convertedUSD = amountFrom/fromRate
        newRequest.total = convertedUSD*toRate
        newRequest.amount = amountFrom
        return newRequest