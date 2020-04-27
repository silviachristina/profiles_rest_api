from django.conf.urls import url
from django.conf.urls import include # viewset

from rest_framework.routers import DefaultRouter # viewset

from . import views

router = DefaultRouter() # viewset
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') # viewset

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)) # viewset
]