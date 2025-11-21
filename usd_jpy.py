import requests
from bs4 import BeautifulSoup

def get_usd_jpy_rate():
    url = "https://www.x-rates.com/calculator/?from=USD&to=JPY&amount=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    rate = soup.find("span", class_="ccOutputRslt").text
    return rate

if __name__ == "__main__":
    rate = get_usd_jpy_rate()
    print(f"1 USD = {rate}")
