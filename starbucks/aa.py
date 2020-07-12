import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


from drink.models import Menu

print("aaaa")
