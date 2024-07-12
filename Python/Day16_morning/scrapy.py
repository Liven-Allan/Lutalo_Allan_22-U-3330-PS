# Libraries for web scraping
# Request, BeautifulSoup, lmxl, scrapy, Selenium
# API Keys
# Exercises, openweathermap.org UGX5000000

# Install required libraries
# pip install requests beautifulsoup4

# Step 1:
import requests 
from bs4 import BeautifulSoup
import csv
import json

# Step 2: # Base URL 
url = 'http://ryeko.org'
response = requests.get(url)
html_content = response.text

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 4:
data = []

for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title': title, 'link': link})

# Srep 5: Save data to a csv file
csv_file = 'scrapped_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)       

# Step 6: Save the data to a JSON file
json_file = "scrapped_data.json"
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


# Step 7: Save successfully to csv and json format
print(f"Data saved Successfully to {csv_file} and {json_file} format")


# Exercise 1:
# Scrap data from the https://openweathermap.org
# current weatherdata

# Step 1: Variable declaration
api_key = '011832ee1da7abce18c3d6894f3cf004'
city_name = 'Kampala'
weather_url = "http://api.openweathermap.org/data/2.5/weather"
weatherCity_url = f"{weather_url}?q={city_name}&appid={api_key}"

# Step 2: Make the request to the API
response_weather = requests.get(weatherCity_url)

# Step 3: Check if the request was successful
if response_weather.status_code == 200:
    html_weatherContent = response_weather.text
    soup_weather = BeautifulSoup(html_weatherContent, 'html.parser')

    # Step 4: Extract the required data
    weather_data = response_weather.json()
    main = weather_data['main']
    weather = weather_data['weather'][0]
    temperature = main['temp']
    description = weather['description']

    # Store the data in a list
    data = [{'city': city_name, 'temperature': temperature, 'description': description}]

    # Step 5: Save data to a CSV file
    csv_file = 'scraped_weather_data.csv'
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['city', 'temperature', 'description'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    
    # Step 6: Save the data to a JSON file
    json_file = "scraped_weather_data.json"
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    # Step 7: Save successfully to CSV and JSON format
    print(f"Data saved successfully to {csv_file} and {json_file} format")
else:
    print("Failed to retrieve data from OpenWeatherMap API")