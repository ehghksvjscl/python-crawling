from django.core.management.base import BaseCommand, no_translations
from drink import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = "db/csv/allergy.csv"
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)

            for row in data_reader:
                if row[4] == "":
                    break
                else:
                    models.Allergy(name=row[4]).save()
            # models.Allergy(drink=row[4]).save()


# alter table nutrition convert to character set utf8;          테이블 encoding 변경 ..
# alter table menu auto_increment = 1; 아이디값 초기화
