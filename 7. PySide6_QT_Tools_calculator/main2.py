import requests
from bs4 import BeautifulSoup

# Make a GET request to the HTML page
response = requests.get("https://nbu.uz/uz/exchange-rates/")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse HTML response
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the element containing exchange rate data
    exchange_rate_table = soup.find("table", class_="col-xs-12 col-md-8 main_exchange")
    if exchange_rate_table:
        # Extract and print the table rows
        rows = exchange_rate_table.find_all("tr")
        for row in rows:
            columns = row.find_all("td")
            if columns:
                print([column.text.strip() for column in columns])
    else:
        print("Exchange rate table not found on the page.")
else:
    print("Error:", response.status_code)
