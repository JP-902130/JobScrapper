from selenium import webdriver
import pandas as pd
from IPython.display import display
import dfProcessor


def extractNum(string):
    list1 = []
    for i in range(len(string)):
        if string[i].isdigit() or string[i] == '.':
            list1.append(string[i])
    res = "".join(list1)
    return float(res)


def updateTable(year, season):
    driver = webdriver.Chrome()
    driver.get("https://www.levels.fyi/internships/")

    # Scrap the data from the table
    companies = driver.find_elements("xpath", "//tbody/tr/td/div/div[2]/h6")
    salaries = driver.find_elements("xpath", "//tbody/tr/td[2]/div/div/h6")
    statuses = driver.find_elements("xpath", "//tbody/tr/td[4]/p/a")
    locations = driver.find_elements("xpath", "//tbody/tr/td[1]/div/div[2]/p")
    links = driver.find_elements("xpath", "//tbody/tr/td[4]/p/a")
    # Slice the companies with no salaries
    companies = companies[0:len(salaries)]
    statuses = statuses[0:len(salaries)]
    locations = locations[0:len(salaries)]
    links = links[0:len(salaries)]
    for i in range(len(companies)):
        companies[i] = companies[i].text
        salaries[i] = salaries[i].text
        statuses[i] = statuses[i].text
        locations[i] = locations[i].text
        links[i] = links[i].get_attribute("href")

    dict = {'Company': companies, 'Salary': salaries,
            'Status': statuses, 'Location': locations, 'Link': links}
    df = pd.DataFrame(dict)

    driver.close()
    df["Salary"] = df["Salary"].map(extractNum)

    # Filter 2023 jobs and open jobs
    df = df[df["Status"] == "Apply"]
    df = df[df.Location.str.endswith(season + " / " + year)]
    df = dfProcessor.addCityAndCountryToRawDF(df)
    df.to_excel('Jobs.xlsx', sheet_name='Jobs')
