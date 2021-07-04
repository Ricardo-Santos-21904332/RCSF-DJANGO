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
    path('walfisch_ikegami/', views.walfisch_ikegami, name='walfisch_ikegami'),
    path('tamanho_cluster/', views.tamanho_cluster, name='tamanho_cluster'),
    path('grafico_CI_Ncp/', views.grafico_CI_Ncp, name='grafico_CI_Ncp'),
    path('grafico_Planeamento/', views.grafico_Planeamento, name='grafico_Planeamento'),
    path('probabilidade_bloqueio/', views.probabilidade_bloqueio, name='probabilidade_bloqueio'),
    path('quantidade_canais/', views.quantidade_canais, name='quantidade_canais'),
    path('trafego_oferecido/', views.trafego_oferecido, name='trafego_oferecido'),
    path('Erlang_B/', views.Erlang_B, name='Erlang_B'),
    path('digrama_radicao_antena', views.digrama_radicao_antena, name='digrama_radicao_antena'),
    path('heatmap_antena', views.heatmap_antena, name='heatmap_antena')
]
