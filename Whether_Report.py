import requests
from bs4 import BeautifulSoup

search = input("Enter the city name to know the weather: ")

url = f"https://www.google.com/search?&q=weather+in+{search}"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

weather_info = soup.find("div",class_="BNEawe").text

print(f"The weather in {search} is: {weather_info}")
