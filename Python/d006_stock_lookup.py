import requests
import csv

print("Welcome to the stock lookup!")

api_key = "------"
data_type = "csv"
type_of_time_series_data = "INTRADAY"

def retrieveLatestPrice(stock, data_file) -> str:
    result = ""
    reader = csv.reader(data_file.text.strip().split("\n"))
    for row in reader:
        if row[0] != "timestamp":
            result += f"\n{stock}, at {row[0]}: \nOpen: {row[1]} \nHigh: {row[2]} \nLow: {row[3]}\nClose: {row[4]} \nVolume: {row[5]}\n"
            break
    return result

def getStocksData(stocks) -> None:
    result = ""
    for stock in stocks:
        stock = stock.strip()

        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_{type_of_time_series_data}&symbol={stock}&interval=1min&outputsize=compact&apikey={api_key}&datatype={data_type}"
        
        stock_data = requests.get(url)
        result += retrieveLatestPrice(stock, stock_data)

    print(result)

while True:
    stocks = input("Enter stock ticker symbols separated by commas (Enter 0 to quit): ")
    if stocks.strip() != "0":
        stocks_list = stocks.split(",")
        print(f"Number of stocks: {len(stocks_list)}")
        getStocksData(stocks_list)
    else:
        break

print("Thanks for using this stock lookup script")
    
