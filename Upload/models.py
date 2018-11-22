import datetime
import os
import random

from django.core.files.storage import FileSystemStorage
from django.db import models


# 图片+ 图片的格式
class ImageFilesStorage(FileSystemStorage):
    # /upload_to/img/图片的名字
    def _save(self, name, content):
        old_name = name.split('/')[-1]
        # 获取图片后缀名
        suffix_name = old_name.split('.')[-1]
        prefix_name = f"IMG_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{str(random.randint(100000,999999))}"
        image_path = os.path.dirname(name)
        name = os.path.join(image_path, f'{prefix_name}.{suffix_name}')
        return super()._save(name, content, )


class Shop(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    # 框架自动配置了media
    # img = models.ImageField(upload_to='shop/img/', storage=ImageFilesStorage(), max_length=255)

    class Meta:
        db_table = 'shop'


class Img(models.Model):
    img = models.ImageField(upload_to='shop/img', storage=ImageFilesStorage(), max_length=255)
    type = models.SmallIntegerField()
    name = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'
