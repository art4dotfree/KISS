# filename urls
# author hardh
# datetime 27.03.2017 - 0:23
from django.urls import path

from mysite import views

urlpatterns = [
    path('', views.post_list, name='post_list')
]