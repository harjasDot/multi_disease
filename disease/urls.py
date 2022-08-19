from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('breastCancer',views.cancerPage,name="cancerPage"),
    path('diabetes',views.diabetesPage,name='diabetesPage'),
    path('heart',views.heartPage,name='heartPage'),
    path('kidney',views.kidneyPage,name='kidneyPage'),
    path('liver',views.liverPage,name='liverPage'),
    path('malaria',views.malariaPage,name='malariaPage'),
    path('pneumonia',views.pneumoniaPage,name='pneumoniaPage'),
    path('predict',views.predictPage,name='predictPage'),
    path('pneumonia',views.pneumoniapredictPage,name='pneumoniapredictPage'),
    path('malaria',views.malariapredictPage,name='malariapredictPage'),


]