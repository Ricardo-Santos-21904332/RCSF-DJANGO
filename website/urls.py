from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gsm/', views.gsm, name='gsm'),
    path('gsmr/', views.gsmr, name='gsmr'),
    path('cloud_ran/', views.cloud_ran, name='cloud_ran'),
    path('espaco_livre', views.espaco_livre, name="espaco_livre"),
    path('okumura_hata/', views.okumura_hata, name='okumura_hata'),
    path('walfisch-ikegami/', views.walfisch_ikegami, name='walfisch-ikegami')
]
