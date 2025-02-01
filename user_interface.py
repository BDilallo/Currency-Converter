from api_caller import API_Caller
from request_object import RequestObject
from converter import Converter

class User_Interface ():
        
    def __init__(self):
        User_Interface.sessionKey()
        User_Interface.displayCommands()
        User_Interface.runner()
    
    apiResponse = {}
    apiKey = "NIL"
    def sessionKey():
        while True:
            User_Interface.apiKey = str(input("Enter API Key for session: "))
            if User_Interface.apiKey.upper() == "EXIT": 
                print("- Exiting...")
                return
            else:
                User_Interface.apiResponse = API_Caller.makeCall(User_Interface.apiKey)
                if User_Interface.apiResponse.json() ["result"] == "error": 
                    print("- API call failed. Please validate API Key to proceed.")
                else:
                    print("- Key Validated, Intialization call made.")
                    break

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
    
    def displayCodes():
        temp = ""
        for count, item in enumerate(User_Interface.currencyCodes):
            if 0 == count % 10 and count != 0 and count != len(User_Interface.currencyCodes)-1:
                temp += item+" | "+"\n"
            else:
                temp += item+" | "
        print("                  Supported Currency Codes")
        print("-----------------------------------------------------------------")
        print(temp)
        print("-----------------------------------------------------------------")

    def displayCommands():
        CMDs = "        Command     || Function" + "\n--------------------------------------------------" 
        CMDs += "\n -   (CONVERT)      || Convert Currency" + "\n -   (CODES)        || View Currency Codes" 
        CMDs += "\n -   (COMMANDS)     || Review These Commands" 
        CMDs += "\n -   (EXIT)         || Exits Current Interface"+ "\n--------------------------------------------------"

        print(CMDs)

    def parameters():
        requestObject = RequestObject(User_Interface.apiResponse,"","",-1,-1)

        while True: 
            requestObject.currencyFrom = str(input("Enter currency code to convert from: ")).upper()
            if requestObject.currencyFrom == "EXIT": print("- Input Aborted."); return
            if requestObject.currencyFrom == "CODES": User_Interface.displayCodes()
            if requestObject.currencyFrom in User_Interface.currencyCodes: break
            else: print("- Invalid Input. Please enter a valid currency code.")

        while True: 
            requestObject.currencyTo = str(input("Enter currency code to convert to: ")).upper()
            if requestObject.currencyTo == "EXIT": print("- Input Aborted."); return
            if requestObject.currencyFrom == "CODES": User_Interface.displayCodes()
            if requestObject.currencyTo in User_Interface.currencyCodes: break
            else: print("- Invalid Input. Please enter a valid currency code.")
                    
        while True:
            tempString = str(input("Enter amount to convert: "))
            if tempString.upper() == "EXIT": print("- Input Aborted."); return
            if tempString.isnumeric(): 
                requestObject.amount = float(tempString) 
                break
            else: print("- Invalid Input. Please enter a numeric value.")

        resultObject = Converter.makeConversion(requestObject)
        print(f"- {resultObject.amount} {resultObject.currencyFrom} is {resultObject.total:.2f} {resultObject.currencyTo} when converted.")
        


    def runner():
        while True:
            userInput = str(input("> ")).upper()

            match userInput:
                case "CONVERT":
                    User_Interface.parameters()
                case "CODES":
                    User_Interface.displayCodes()
                case "COMMANDS":
                    User_Interface.displayCommands()
                case "EXIT":
                    print("- Exiting...")
                    return
