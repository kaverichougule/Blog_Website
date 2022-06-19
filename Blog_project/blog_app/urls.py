from django.urls import path
from requests import post
from blog_app import views
from .views import home,post,category

urlpatterns = [
   path('',views.home),
   path('blog/<slug:url>',post),
   path('category/<slug:url',category)
]