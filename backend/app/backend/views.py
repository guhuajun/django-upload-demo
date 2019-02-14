# -*- coding: utf-8 -*-
# pylint: disable=

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from backend import models, serializers


class PhotoViewSet(viewsets.ModelViewSet):

    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
