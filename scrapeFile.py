from bs4 import BeautifulSoup
import pandas as pd 

test_df = pd.DataFrame(columns=['Company', 'Title', 'Job Length'])


with open("/Users/megmkr/Kimberly Kapella.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

city_info = soup.find("div", class_=["pv-text-details__left-panel mt2"])
city = city_info.find("span", class_=["text-body-small", "inline t-black--light", "break-words"]).get_text().strip()

experience_section = soup.find("div", id='experience').parent
experiences = experience_section.find_all("div", class_=["display-flex ","flex-row", "justify-space-between"])
alum_list = []
for experience in experiences:
    temp_list = []
    test = [tag for tag in experience.find_all("span", class_=["visually-hidden"]) if "t-black--light" not in tag.parent['class']]
    

    for tester in test:
        tester_text = tester.get_text()
        if("Full-time" == tester_text or "Part-time" == tester_text or "yr" in tester_text or "mo" in tester_text):
            test.remove(tester)

    if len(test) >= 3:
        for tester in test:
            temp_list.append(tester.get_text())
        alum_list.append(temp_list)
    if len(test) == 2:
        temp_list.append(test[1].get_text())
        temp_list.append(test[0].get_text())
        alum_list.append(temp_list)


print(alum_list)
print(city)

