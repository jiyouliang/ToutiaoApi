from django.db import models
import sys
import pymysql
import json


# Create your models here.

class NewsTech(models.Model):
    # _id = models.AutoField
    datetime = models.DateTimeField
    json = models.TextField

    class Meta:
        db_table = "news_tech"


