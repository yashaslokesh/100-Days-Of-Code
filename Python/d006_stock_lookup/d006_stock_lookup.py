import requests
import csv
import sys
import os

print("Welcome to the stock lookup!")

"""
    Add values to all three of these fields before using. For most people, they might just add the api key and use this
    script. If you change the data_type field, this script will not work, you will have to add functionality for json
    parsing. Look at the Alpha Vantage api if you would like to change the type of time series data.
"""
api_key = os.environ.get("ALPHA_VANTAGE_KEY")
data_type = "csv" 
type_of_time_series_data = "INTRADAY"

def retrieveLatestPrice(stock, data_file) -> str:
    reader = csv.reader(data_file.text.strip().split("\n"))

    row = list(reader)[1]
    try:
        result = (f"\n{stock}, at {row[0]}: \nOpen: {row[1]} \nHigh: {row[2]} "
        f"\nLow: {row[3]}\nClose: {row[4]} \nVolume: {row[5]}\n")
    except IndexError:
        print(f"The stock data for symbol {stock} failed in retrieval. This might be due to a mispelling of the" 
        " stock symbol or if the api_key, data_type, or type_of_time_series_data fields are mispelled or incorrect. "
        "If none of these are problems, then contact me on Github or, I think you can also raise an issue on "
        "the repo, but I'm not sure. Just contact me however you please so I can try to fix errors :)")
        
    return result

def getStocksData(stocks) -> None:
    result = []
    for stock in stocks:
        stock = stock.strip().upper()

        url = (f"https://www.alphavantage.co/query?function=TIME_SERIES_{type_of_time_series_data}&symbol={stock}"
               f"&interval=1min&outputsize=compact&apikey={api_key}&datatype={data_type}")
        
        stock_data = requests.get(url)
        try:
            result.append(retrieveLatestPrice(stock, stock_data))
        except:
            sys.exit(f"This is the url:\n{url}\n for the stock: {stock}, failure to retrieve")

    print(''.join([_ for _ in result]))

def main():
    while True:
        stocks = input("Enter stock ticker symbols separated by commas (Enter 0 to quit): ")
        if "0" not in stocks:
            stocks_list = stocks.split(",")
            print(f"Number of stocks: {len(stocks_list)}")
            getStocksData(stocks_list)
        else:
            break

if __name__ == '__main__':
    main()

print("Thanks for using this stock lookup script")
    
