# -*- coding: utf-8 -*-
# pylint: disable=

from rest_framework import routers

from backend import views

router = routers.DefaultRouter(trailing_slash='/')
router.register('photo', views.PhotoViewSet, base_name='photo')

urlpatterns = router.urls
