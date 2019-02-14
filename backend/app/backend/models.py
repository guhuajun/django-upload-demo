# -*- coding: utf-8 -*-
# pylint: disable=

from django.db import models

class Photo(models.Model):

    photo = models.FileField(verbose_name='photo', upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.photo.name
