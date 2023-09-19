#import requests 
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

#set up the chrome driver
#THIS IS WHERE YOU NEED TO CHANGE THE PATH TO WHEREVER THE DRIVE IS ON YOUR COMPUTER
service = Service(executable_path='/Users/megmkr/linkedinenv/drivers/chromedriver-mac-arm64-2/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#direct the chrome driver to the linkedin page with all PLNU alum
driver.get('https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&schoolFilter=%5B19523%5D&sid=YOb')
input("Enter in Username and Password")
soup = BeautifulSoup(driver.page_source, 'html.parser')
#alumni_list = soup.find_all("div", class_="entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light")
alumni_list = soup.find_all("a", class_= "app-aware-link")

#print(alumni_list)

alum_dict = {}

for profile in alumni_list:
   #get info on each person from each page
   profile_link = profile.get("href")
   #link_getter = soup.find("a", class_= "app-aware-link")
   #profile_link = link_getter.get("href")
   alumni_name = profile.find("span", attrs={'aria-hidden': True})
   #bio = profile.find("div", class_="entity-result__primary-subtitle t-14 t-black t-normal")
  
   """try: 
     print(profile_link)
     print(alumni_name.get_text())
     print(bio.get_text())
   except:
     print("invalid data")  """
   
   #put it all into a dictionary
   try:
     if(len(profile_link) > 90): #this makes sure it is a profile link because I was getting other random links before
        #alum_dict.update({alumni_name.get_text(): [profile_link, bio.get_text()]})
        alum_dict.update({alumni_name.get_text(): profile_link})
   except:
     None
      

for key, value in alum_dict.items():
  driver.get(value)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  body = soup.find("body")
  print(type(body))
  print(body.find("div", class_="pvs_list__outer-container"))
  #bio = soup.find("div", class_="text-body-medium break-words")
  #alum_dict[key].append(bio.get_text())

#print out dictionary for testing      
for key, value in alum_dict.items():
  print(key, " : ", value, "\n")


#close chrome window
driver.quit()



