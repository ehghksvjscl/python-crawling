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
                drink = models.Drink.objects.get(id=row[0])
                allergy = models.Allergy.objects.get(id=row[2])
                models.Drink_Allergy(drink=drink, allergy=allergy).save()
            # models.Allergy(drink=row[4]).save()


# alter table nutrition convert to character set utf8;          테이블 encoding 변경 ..
# alter table menu auto_increment = 1; 아이디값 초기화
# select a.name,b.content,c.one_serving_kcal,sodium_mg,saturated_fat_g,sugars_g,protein_g,caffeine_mg
#     FROM drink AS a
#     LEFT JOIN detail AS b
#     ON a.id=b.drink_id
#     LEFT JOIN nutrition AS c
#     ON a.id=c.drink_id;


# one_serving_kcal
# sodium_mg
# saturated_fat_g
# sugars_g
# protein_g
# caffeine_mg

# SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s LEFT JOIN location AS l ON s.location_id = l.id;
