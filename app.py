from selenium import webdriver
import pandas as pd
import re
from IPython.display import display


def extractNum(string):
    list1 = []
    for i in range(len(string)):
        if string[i].isdigit() or string[i] == '.':
            list1.append(string[i])
    res = "".join(list1)
    return float(res)


# def extractCity(cityCountry):


def updateTable():
    driver = webdriver.Chrome()
    driver.get("https://www.levels.fyi/internships/")
    driver.maximize_window()
    # Scrap the data from the table
    companies = driver.find_elements("xpath", "//tbody/tr/td/div/div[2]/h6")
    salaries = driver.find_elements("xpath", "//tbody/tr/td[2]/div/div/h6")
    statuses = driver.find_elements("xpath", "//tbody/tr/td[4]/p/a")
    locations = driver.find_elements("xpath", "//tbody/tr/td[1]/div/div[2]/p")

    # Slice the companies with no salaries
    companies = companies[0:828]
    statuses = statuses[0:828]
    locations = locations[0:828]

    for i in range(len(companies)):
        companies[i] = companies[i].text
        salaries[i] = salaries[i].text
        statuses[i] = statuses[i].text
        locations[i] = locations[i].text

    dict = {'Company': companies, 'Salary': salaries,
            'Status': statuses, 'Location': locations}
    df = pd.DataFrame(dict)

    driver.close()
    df["Salary"] = df["Salary"].map(extractNum)

    # Filter 2023 jobs and open jobs
    df = df[df["Status"] == "Apply"]
    df = df[df.Location.str.endswith('2023')]
    df.to_excel('Excel_Sample.xlsx', sheet_name='Sheet1')
    display(df)


updateTable()
