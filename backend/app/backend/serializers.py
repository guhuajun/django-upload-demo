# -*- coding: utf-8 -*-
# pylint: disable=


from rest_framework import serializers

from backend import models


class PhotoSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Photo
        fields = '__all__'
