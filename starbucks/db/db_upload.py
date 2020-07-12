import os
import csv
import sys

# 장고 앱에서 외부 파이썬 파일을 인익 할 수 있도록 설정을 해준다.
os.environ["DJANGO_SETTINGS_MODULE"] = "drink.settings"
import django

django.setup()

from drink.models import Menu

# csv파일 경로 선언
CSV_PATH_DRINK = "./csv/menu.csv"

with open(CSV_PATH_DRINK) as in_file:
    data_reader = csv.reader(in_file)
    for row in data_reader:
        print(row)
