from django.conf.urls import url
from django.conf.urls import include # viewset

from rest_framework.routers import DefaultRouter # viewset

from . import views

router = DefaultRouter() # viewset
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') # viewset
router.register('profile', views.UserProfileViewSet) #when you registrer a model viewset you don't need to specify the base name django automatically
router.register('login', views.LoginViewSet, base_name='login') 
router.register('feed', views.UserProfileFeedViewSet) 

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)) # viewset
]