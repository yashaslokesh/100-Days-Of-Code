import csv
import json
import datetime

def processCSV(csv_file):
    reader = list(csv.reader(csv_file))

    result_list = []
    header = reader[0]
    for row in reader[1:]:
        row_object = {}
        for num,col in enumerate(row):
            row_object[header[num]] = col
        result_list.append(row_object)
    data = {"data" : result_list}

    today = datetime.datetime.today().strftime("%m-%d-%Y")

    with open(f"results-{today}.json","w") as file:
        result = json.dumps(data, indent=3, sort_keys=False)
        file.write(result)

if __name__=="__main__":
    file = input("Enter path of CSV file: ")
    
    try:
        with open(file,"r") as f:
            processCSV(f)

    except FileNotFoundError:
        print("*" * 20)
        print(f"FileNotFoundError: The file on path {file} was not found, change your current directory or check the file name")
        print("*" * 20)
