import requests
from bs4 import BeautifulSoup


def getData(index):
    states = ['Andhra-Pradesh', 'Arunachal-Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Delhi',
              'Goa', 'Gujarat', 'Haryana', 'Himachal-Pradesh', 'Jammu-and-Kashmir', 'Jharkhand', 'Karnataka',
              'Kerala', 'Madhya-Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
              'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
              'Uttar-Pradesh', 'Uttarakhand', 'West-Bengal']

    url = "https://market.todaypricerates.com/" + states[int(index)] + "-vegetables-price"
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        vegetable_data = []

        table = soup.find('div', class_='Table')

        rows = table.find_all('div', class_='Row')

        for row in rows:
            cells = row.find_all('div', class_='Cell')

            if len(cells) == 5:
                vegetable_name = cells[0].text.strip()
                unit = cells[1].text.strip()
                market_price = cells[2].text.strip().replace('₹', '').strip()
                retail_price = cells[3].text.strip().replace('₹', '').strip()
                shopping_mall = cells[4].text.strip().replace('₹', '').strip()

                vegetable = {
                    'Vegetable-Name': vegetable_name,
                    'Unit': unit,
                    'Market-Price': market_price,
                    'Retail-Price': retail_price,
                    'Shopping-Mall': shopping_mall
                }

                vegetable_data.append(vegetable)

        return vegetable_data
    else:
        print("Failed to retrieve the webpage")
        return None
