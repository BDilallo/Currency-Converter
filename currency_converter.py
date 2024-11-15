

class CurrencyConverter:

    fromCurrency = ""
    toCurrency = ""
    amountCurrency = 0

    currencyCodes = ['AED','AFN','ALL','AMD','ANG','AOA','ARS','AUD','AWG','AZN','BAM','BBD','BDT','BGN',
                     'BHD','BIF','BMD','BND','BOB','BRL','BSD','BTN','BWP','BYN','BZD','CAD','CDF','CHF',
                     'CLP','CNY','COP','CRC','CUP','CVE','CZK','DJF','DKK','DOP','DZD','EGP','ERN','ETB',
                     'EUR','FJD','FKP','FOK','GBP','GEL','GGP','GHS','GIP','GMD','GNF','GTQ','GYD','HKD',
                     'HNL','HRK','HTG','HUF','IDR','ILS','IMP','INR','IQD','IRR','ISK','JEP','JMD','JOD',
                     'JPY','KES','KGS','KHR','KID','KMF','KRW','KWD','KYD','KZT','LAK','LBP','LKR','LRD',
                     'LSL','LYD','MAD','MDL','MGA','MKD','MMK','MNT','MOP','MRU','MUR','MVR','MWK','MXN',
                     'MYR','MZN','NAD','NGN','NIO','NOK','NPR','NZD','OMR','PAB','PEN','PGK','PHP','PKR',
                     'PLN','PYG','QAR','RON','RSD','RUB','RWF','SAR','SBD','SCR','SDG','SEK','SGD','SHP',
                     'SLE','SOS','SRD','SSP','STN','SYP','SZL','THB','TJS','TMT','TND','TOP','TRY','TTD',
                     'TVD','TWD','TZS','UAH','UGX','USD','UYU','UZS','VES','VND','VUV','WST','XAF','XCD',
                     'XDR','XOF','XPF','YER','ZAR','ZMW','ZWL',]

    def __init__(self):
        CurrencyConverter.displayCodes()
        CurrencyConverter.intake()
    
    def displayCodes():
        temp = ""
        for count, item in enumerate(CurrencyConverter.currencyCodes):
            if 0 == count % 10 and count != 0 and count != len(CurrencyConverter.currencyCodes)-1:
                temp += item+" | "+"\n"
            else:
                temp += item+" | "
        print("\nSupported Currency Codes")
        print("-----------------------------------------------------------------")
        print(temp)
        print("-----------------------------------------------------------------\n")

    def intake():
        while True: 
            CurrencyConverter.fromCurrency = str(input("Enter currency code to convert from: ")).upper()
            if CurrencyConverter.fromCurrency in CurrencyConverter.currencyCodes:
                break
            else:
                print("- Invalid Input. Please enter a valid currency code.")

        while True: 
            CurrencyConverter.toCurrency = str(input("Enter currency code to convert to: ")).upper()
            if CurrencyConverter.toCurrency in CurrencyConverter.currencyCodes:
                break
            else:
                print("- Invalid Input. Please enter a valid currency code.")
                
        while True: 
            try:
                CurrencyConverter.amountCurrency = float(input("Enter amount to convert: "))
                break
            except:
                print("- Invalid Input. Please enter a numeric value.")

converter = CurrencyConverter()