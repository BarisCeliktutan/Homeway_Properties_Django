from django.urls import path
from . import views

urlpatterns = [
    path("o_ses_turkiye/", views.o_ses, name="O Ses Türkiye"),
    path("o_ses_turkiye/sezon_ekle", views.sezon_ekle, name="sezon_ekle"),
    path("o_ses_turkiye/<str:yil>_juriler/", views.juriler, name="o_ses_turkiye_juriler"),
    path("o_ses_turkiye/<str:yil>_juriler/juri_ekle", views.juri_ekle, name="o_ses_turkiye_juri_ekle"),
    path("o_ses_turkiye/<str:yil>_juriler/<str:juri>", views.juri, name="o_ses_turkiye_juri"),
    path("o_ses_turkiye/<str:yil>_juriler/<str:juri>/yarismaci_ekle", views.yarismaci_ekle, name="o_ses_turkiye_yarismaci_ekle"),
]
