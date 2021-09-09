'''Text-based cryptocurrency profit tracker that culaculates profits based off of info from CSV file'''
from pycoingecko import CoinGeckoAPI
import csv

def main():
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
            cry = row[3]
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
            cvp = return_current_value(cgdatac, cry, amt)
            
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
def return_current_value(cgd, currency, amount):
    
    cid = cgd[id]

    #current price
    cpr = cid[currency]
    print("Current price:",cpr)

    #current value of purchase
    cvp = cpr * float(amount)

    return cvp

    
    
    
    
    

    
main()