#This url file was specifically created
#dont confuse this one with the one insite the mysite file initially created
#used when multiple views

from django.urls import path
from . import views

urlpatterns=[
path("<int:id>",views.index,name="index"), #ANGLE BRACKETS TO CAPTURE VALUE FROM URL,goes to views and passed to function over there
path("",views.home,name="home"),
path("create/" , views.create , name="create"),

]