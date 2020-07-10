import requests
import csv
from bs4 import BeautifulSoup


def getInfo(li_list):
    rank = li_list.find("span", {"class": "chart-element__rank__number"}).string
    song_title = li_list.find(
        "span", {"class": "chart-element__information__song"}
    ).string
    detail = li_list.find(
        "span", {"class": "chart-element__information__artist"}
    ).string

    return {"rank": rank, "song_title": song_title, "detail": detail}


def csv_save(billboard_Info):
    f = open("billboard.csv", "w", encoding="utf-8", newline="")
    wr = csv.writer(f)
    wr.writerow([1, "순위", "제목", "아티스트 정보"])
    for Info in billboard_Info:
        wr.writerow([Info["rank"], Info["song_title"], Info["detail"]])
    f.close()


URL = "https://www.billboard.com/charts/hot-100"
billboard_Info = []

html_code = requests.get(URL).text
soup = BeautifulSoup(html_code, "html.parser")
li_lists = soup.find_all("li", {"class": "chart-list__element display--flex"})

for li_list in li_lists:
    billboard_Info.append(getInfo(li_list))

csv_save(billboard_Info)
