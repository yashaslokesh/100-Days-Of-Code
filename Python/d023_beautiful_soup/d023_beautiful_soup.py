import csv
from bs4 import BeautifulSoup

with open("onCall.html","r") as html:
    soup = BeautifulSoup(html, "html.parser")
    # data_table = soup.find_one("table", class_="confluenceTable")
    data_table = soup.select_one("table.confluenceTable")

    csv_header = [th.text.strip() for th in data_table.select("tr th")]

    with open("results.csv","w") as result:
        writer = csv.writer(result)
        writer.writerow(csv_header)
        for row in data_table.select("tr + tr"):
            writer.writerow(td.text.strip() for td in row.find_all("td"))
                


