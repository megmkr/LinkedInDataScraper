from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome

import pandas as pd

def scrape_search(page_number):
    i = 2
    for i in range(page_number):
      soup = BeautifulSoup(driver.page_source, 'html.parser')
      #get each profile on the page
      alumni_list = (soup.find_all("a", class_= "app-aware-link"))
      for profile in alumni_list:
        #get info from each profile on the page
        profile_link = profile.get("href")
        alumni_name = profile.find("span", attrs={'aria-hidden': True})
        try:
          if(len(profile_link) > 90): #this makes sure it is a profile link because I was getting other random links before
            alum_dict.update({alumni_name.get_text(): profile_link})
        except:
          None
      #getting to the next page
      #next_button = driver.find_element(By.CSS_SELECTOR, "span.artdeco-button__text")
      #next_button.click()
      new_link = link[:75]+str(i)+link[76:]
      driver.get(new_link)
    return alumni_list

if __name__ == '__main__':

  #set up the chrome driver
  driver = webdriver.Chrome()

  alum_df = pd.DataFrame(columns=['Name', 'City', 'Occupation'])

  alumni_list = []
  alum_dict = {}

  #direct the chrome driver to the linkedin page with all PLNU alum
  link= 'https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&page=1&schoolFilter=%5B19523%5D&sid=rl*'
  driver.get(link)

  input("Enter in Username and Password")
  #loop scrapes first 9 pages, for range(n) n = last page nmber + 1
  scrape_search(10)    
 
  #writing html to file
  for key, value in alum_dict.items():
    print(key, value)
    driver.get(value)
    html_content = driver.page_source
    file_name = key + ".html"
    alum_file = open(file_name, "w", encoding='utf-8')
    alum_file.write(html_content)
    
    alum_file.close()
  
  #close chrome window
  driver.quit()



