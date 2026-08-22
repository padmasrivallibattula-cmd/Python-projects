
import requests
from bs4 import BeautifulSoup as bs

username = input()

url ="https://github.com/" + username

response = requests.get(url)

if response.status_code == 200:
      
      soup = bs(response.text,"html.parser")
      
      name = soup.find("span", class_ ="p-name")
      
      bio = soup.find("div",class_ ="p-note")
      
      image = soup.find("meta",property ="og:image")
      
      print("username : ",username)
      
      if name:
            print("Name:", name.text.strip())
            
      else:
            print("User not found")
            
      if bio:
            print("Bio:" ,bio.text.strip())
            
      else:
            print("Bio not found")
            
      if image:
            print("profile image:", image["content"])
            
      else:
            print("No Image")
            
else:
      print("user not found")
