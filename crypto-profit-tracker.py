'''Text-based cryptocurrency profit tracker that culaculates profits based off of info from CSV file'''
from pycoingecko import CoinGeckoAPI
import csv
import sys
import argparse
def main():

    print("Argument vector", sys.argv)
    print("Argument vector length", len(sys.argv))


    if (len(sys.argv) > 1):
        parser = argparse.ArgumentParser(description='Calculate profits of crypto purchase based on current CoinGecko pricing')

        #Arguments for using data entered on command line
        parser.add_argument('crypto_token', metavar= "T", nargs=1, help='the corresponding cryptocurrency Token as featured on CoinGecko')
        parser.add_argument('amount_bought', metavar= "A", type=float, nargs=1, help='the Amount of cryptocurrency purchased')
        # parser.add_argument('date_purchased', metavar= "D", nargs=1, help='the Date of purchase using MM-DD-YYYY formatting')
        parser.add_argument('money_spent', metavar= "S", type=float, nargs=1, help='amount of host currency Spent')
        parser.add_argument('host_currency', metavar="H", nargs=1, help="abbreviated name of Host currency (e.g. 'eur', 'usd'")

        cg = CoinGeckoAPI()



        args = parser.parse_args()
        #Current price calculation
        #Current data
        cgdatac=cg.get_price(ids=args.crypto_token, vs_currencies = args.host_currency)

        print("token:", args.crypto_token)
        print("currency:", args.host_currency)
        print("amt bought:", args.amount_bought)

        #current value of purchase
        cvp = return_current_value(cgdatac, args.crypto_token[0], args.host_currency[0], args.amount_bought[0])

        print("Current value of purchase", cvp)
        profit = cvp - args.money_spent[0]
        print("Profit from purchase:", profit)
        percent_delta = profit/cvp
        print("Percent change:", percent_delta)
        
    else:
        
        with open('crypto.csv', 'r') as csvledger:
            #Inside a csv file...
            reader = csv.reader(csvledger,  skipinitialspace=True)
            for row in reader:
                #Coin name
                id = row[0]
                print("Coin name", id)

                #Amount
                amt = row[1]
                print("Amount purchased:", amt)

                #Date purchased
                dp = row[2]
                print("Date purchased:", dp)

                #Currency
                cry = row[4]
                print("Currency used:", cry)


                cg = CoinGeckoAPI()
                #Historical data
                cgdatah = cg.get_coin_history_by_id(id=id, date=dp)
                ms = return_money_spent(cgdatah, cry, amt)
                print("Money spent:", ms)

                #Current price calculation
                #Current data
                cgdatac=cg.get_price(ids=id, vs_currencies = cry)
                
                #current value of purchase
                cvp = return_current_value(cgdatac, id, cry, amt)
                
                print("Current value of purchase:", cvp)
                
                #Change in value
                cv = float(cvp) - ms
                print("Change in value:", cv)
                print()

'''
return_money_spent
@input: cgd - dictionary of data from CoinGecko, currency - string representing currency used in purchase
@output: money_spent - float representing money spent on purchase
'''
def return_money_spent(cgd, currency, amount):
    cg_md = cgd['market_data']
    price = cg_md['current_price']
    
    #Price of currency at date
    price_cry_dt = price[currency] 
    print("Crypto Price at Date Purchased:", price_cry_dt)

    #Money spent
    money_spent =  float(price_cry_dt) * float(amount)
    return money_spent

'''
return_current_value
@input: cgd - dictionary of data from CoinGecko, currency - string representing currency used in purchase
@output: money_spent - float representing current value of purchase
'''
def return_current_value(cgd, crypto, currency, amount):
    cid = cgd[crypto]

    #current price
    cpr = cid[currency]
    print("Current price:",cpr)

    #current value of purchase
    cvp = cpr * float(amount)

    return cvp

    
    
    
    
    

    
main()