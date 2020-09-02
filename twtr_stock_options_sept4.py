from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests

csv_create = open("twtr_options_sept4", "w", newline='')
csv_write = csv.writer(csv_create)

contract_url = []
contract = []
last_trade_date = []
strike = []
last_price = []
bid = []
ask = []
change = []
volume = []
open_interest = []


url = "https://finance.yahoo.com/quote/TWTR/options?p=TWTR"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

for conlink in soup.find_all("td", attrs={"class": "data-col0"}):
    link = conlink.find("a")["href"]
    contract_url.append(f"https://finance.yahoo.com{link}")
for cont in soup.find_all("a", attrs={"class": "Fz(s) Ell C($linkColor)"}):
    contract.append(cont.text)
for last in soup.find_all("td", attrs={"class":"data-col1"}):
    last_trade_date.append(last.text)
for hit in soup.find_all("a", attrs={"class": "C($linkColor) Fz(s)"}):
    strike.append(hit.text)
for pri in soup.find_all("td", attrs={"class":"data-col3"}):
    last_price.append(pri.text)
for bi in soup.find_all("td", attrs={"class":"data-col4"}):
    bid.append(bi.text)
for asks in soup.find_all("td", attrs={"class":"data-col5"}):
    ask.append(asks.text)
for chg in soup.find_all("td", attrs={"class":"data-col6"}):
    change.append(chg.text)
for vol in soup.find_all("td", attrs={"class":"data-col8"}):
    volume.append(vol.text)
for opens in soup.find_all("td", attrs={"class":"data-col9"}):
    open_interest.append(opens.text)

fin = pd.DataFrame({"Contract Link": contract_url,"Contract": contract, "Last Trade Date": last_trade_date, "Strike Price": strike,
"Last Price": last_price, "Bid Price":bid, "Ask Price": ask, "Change": change, "Volume": volume,
"Open Interest": open_interest})

fin.to_csv("twtr_options_sept4.csv")
csv_create.close()
