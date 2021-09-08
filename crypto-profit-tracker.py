from pycoingecko import CoinGeckoAPI
import csv

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
        cgdata = cg.get_coin_history_by_id(id=id, date=dp)
        cg_md = cgdata['market_data']
        price = cg_md['current_price']
        
        #Price of currency at date
        price_cry_dt = price[cry] 
        print("Currency Price at Date Purchased:", price_cry_dt)

        #Money spent
        ms = float(price_cry_dt) * float(amt)
        print("Money spent:", ms)

        #Current price calculation
        cgdata=cg.get_price(ids=id, vs_currencies = cry)
        print(cgdata)
        cid = cgdata[id]

        #current price
        cpr = cid[cry]
        print("Current price:",cpr)

        #current value or purchase
        cvp = cpr * float(amt)
        print("Current value of purchase:", cvp)
        
        #Change in value
        cv = float(cvp) - ms
        print("Change in value:", cv)
        print()