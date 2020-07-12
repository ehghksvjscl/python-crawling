from django.core.management.base import BaseCommand, no_translations
from drink import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = "db/csv/drink.csv"
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)

            for row in data_reader:
                print(row[0], row[1])
                # menu = models.Menu.objects.get(pk=row[0])
                # name = row[1]
                # models.Category(menu=menu, name=name).save()


# alter table menu convert to character set utf8;          테이블 encoding 변경 ..
# alter table menu auto_increment = 1; 아이디값 초기화
