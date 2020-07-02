import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

URL = "https://www.starbucks.co.kr/menu/drink_list.do"
star_menu = []

# 크롭 headless모드
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("-disable-gpu")
chrome_option.add_argument("lang-=ko_KR")

# 크룸 실행
dr = webdriver.Chrome("./chromedriver", chrome_options=chrome_option)

# URL 소스 가져오기
dr.get(URL)
html_code = dr.page_source

# 분석하기 쉽게 bs4로 변환
soup = BeautifulSoup(html_code, "html.parser")

# 매뉴 가져오기
def getMenuInfo(menu):
    name = menu.find("img")["alt"]
    img_Url = menu.find("img")["src"]

    return {"name": name, "img_Url": img_Url}

# csv로 변환
def csv_save(star_menu):
    f = open("star.csv", "w", encoding="utf-8", newline="")
    wr = csv.writer(f)
    wr.writerow(["이름", "URL"])
    for Info in star_menu:
        wr.writerow([Info["name"], Info["img_Url"]])
    f.close()


def main():
    # 방법 1
    # menu_lists = soup.select(".product_list dl dd ul li dl dt a")

    # 방법2
    menu_lists = soup.find_all("a", {"class": "goDrinkView"})
    for menu in menu_lists:
        star_menu.append(getMenuInfo(menu))

    csv_save(star_menu)


if __name__ == "__main__":
    main()
