from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.levels.fyi/internships/")
driver.maximize_window()

companies = driver.find_elements("xpath", "//tbody/tr/td/div/div[2]/h6")
salaries = driver.find_elements("xpath", "//tbody/tr/td[2]/div/div/h6")
for salary in salaries:
    print(salary.text)
