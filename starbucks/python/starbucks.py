import requests
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver

URL = "https://www.starbucks.co.kr/menu/drink_list.do"
star_menu = []

# # 크롭 headless모드
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("-disable-gpu")
chrome_option.add_argument("lang-=ko_KR")

# 크룸 실행
dr = webdriver.Chrome(
    "/home/spectre/바탕화면/Python/crawling/starbucks/python/chromedriver",
    chrome_options=chrome_option,
)

# URL 소스 가져오기
dr.get(URL)
html_code = dr.page_source

# 분석하기 쉽게 bs4로 변환
soup = BeautifulSoup(html_code, "html.parser")


# 음료 정보 가져오기
def getMenuInfo(menu):
    name = menu.find("img")["alt"]
    img_Url = menu.find("img")["src"]

    return {"name": name, "img_Url": img_Url}


def getDrinkInfo(id):
    URL = f"https://www.starbucks.co.kr/menu/drink_view.do?product_cd={id}"
    drink_zoomimg = "http:"
    dr.get(URL)
    html_code = dr.page_source
    soup = BeautifulSoup(html_code, "html.parser")
    drink_name = soup.find("a", {"class": "this"}).text
    drink_en_name = soup.find("div", {"class": "myAssignZone"}).find("span").text
    drink_content = soup.find("p", {"class": "t1"}).text
    drink_zoomimg += soup.find("img", {"class": "zoomImg"})["src"]
    drink_nutrition_info = soup.find("div", {"class": "selectTxt2"}).text
    kcal = soup.find("li", {"class": "kcal"}).find("dd").text
    fat = soup.find("li", {"class": "sat_FAT"}).find("dd").text
    protein = soup.find("li", {"class": "protein"}).find("dd").text
    sodium = soup.find("li", {"class": "sodium"}).find("dd").text
    sugars = soup.find("li", {"class": "sugars"}).find("dd").text
    caffeine = soup.find("li", {"class": "caffeine"}).find("dd").text
    allaegy = soup.find("div", {"class": "product_factor"}).find("p").text

    return {
        "drink_name": drink_name,
        "drink_en_name": drink_en_name,
        "drink_content": drink_content,
        "drink_zoomimg": drink_zoomimg,
        "drink_nutrition_info": drink_nutrition_info,
        "kcal": kcal,
        "fat": fat,
        "protein": protein,
        "sodium": sodium,
        "sugars": sugars,
        "caffeine": caffeine,
        "allaegy": allaegy,
    }


# csv로 변환
def csv_save(star_menu):
    f = open("star2.csv", "w", encoding="utf-8", newline="")
    wr = csv.writer(f)
    wr.writerow(
        [
            "drink_name",
            "drink_en_name",
            "drink_content",
            "drink_zoomimg",
            "drink_nutrition_info",
            "kcal",
            "fat",
            "protein",
            "sodium",
            "sugars",
            "caffeine",
            "allaegy",
        ]
    )
    for Info in star_menu:
        wr.writerow(
            [
                Info["drink_name"],
                Info["drink_en_name"],
                Info["drink_content"],
                Info["drink_zoomimg"],
                Info["drink_nutrition_info"],
                Info["kcal"],
                Info["fat"],
                Info["protein"],
                Info["sodium"],
                Info["sugars"],
                Info["caffeine"],
                Info["allaegy"],
            ]
        )

    f.close()


def main():
    # 방법 1
    # menu_lists = soup.select(".product_list dl dd ul li dl dt a")

    # 방법2
    menu_lists = soup.find_all("a", {"class": "goDrinkView"})
    # # 카테고리 가져오기
    # menu_lists = soup.select(".product_list dl dt")
    # for dt in menu_lists:
    #     if dt.find("a").string != None:
    #         drink_list = soup.select(".product_list dl dd ul li dl dt a")
    #         print(dt.find("a").string)

    # menu_lists = soup.select(".product_list dl dd ul li dl dt a")
    for menu in menu_lists:
        star_menu.append(getDrinkInfo(menu["prod"]))

    csv_save(star_menu)


if __name__ == "__main__":
    main()
