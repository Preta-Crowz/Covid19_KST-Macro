from selenium import webdriver
import json, sys
config = json.load(open('./config.json', 'r'))

options = webdriver.ChromeOptions()
if config["headless"]:
    options.add_argument('headless')
options.add_argument('window-size=800x450')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)

url = "https://eduro.dge.go.kr/stv_cvd_co00_000.do?k="+config['key']
driver.get(url)

if driver.current_url != url: sys.exit(1)

for btnName in ["rspns011", "rspns02", "rspns070", "rspns080", "rspns090"]:
    driver.find_element_by_id(btnName).click()

driver.find_element_by_id("btnConfirm").click()

if driver.find_element_by_class_name("content_box").text.find("자가진단 참여를 완료하였습니다.") != -1:
    driver.close()
    sys.exit(0)
else: sys.exit(2)