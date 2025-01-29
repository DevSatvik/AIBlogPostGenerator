from django.urls import path
from . import views

# list of URL patterns for the blog_generator app
urlpatterns = [
    path('',views.index, name='index'),
]