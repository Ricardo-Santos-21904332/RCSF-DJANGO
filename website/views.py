from django.shortcuts import render

from . import functions
from .forms import FormEspacoLivre
from .forms import FormOkumuraHata
from .forms import FormWalfischIkegami
from .forms import FormTamanhoCluster
from .forms import FormGraficoCINcp
from .forms import FormGraficoPlaneamento
from .forms import FormProbabilidadeDeBloqueio
from .forms import FormQuantidadeDeCanais
from .forms import FormTrafegoOferecido
from .functions import atenuacaoEspacoLivre_grafico
from .functions import atenuacaoEspacoLivre
from .functions import tamanho_minimo_cluster
from .functions import grafico_CI_NCP
from .functions import cria_planeamento_hexagonal
from .functions import cria_mapas_celulas
from .functions import calculaProbabilidadeDeBloqueio
from .functions import calculaQuantidadeCanais
from .functions import calculaTrafegoOferecido


# Create your views here.
def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/about.html")


def gsm(request):
    functions.atenuacaoEspacoLivre(900)
    functions.atenuacaoEspacoLivre(1800)
    functions.propagacaoEspacoLivre(900)
    functions.propagacaoEspacoLivre(1800)
    return render(request, "website/gsm.html")


def gsmr(request):
    functions.atenuacaoEspacoLivre(880)
    functions.atenuacaoEspacoLivre(925)
    functions.propagacaoEspacoLivre(880)
    functions.propagacaoEspacoLivre(925)
    return render(request, "website/gsmr.html")


def cloud_ran(request):
    return render(request, "website/cloud-ran.html")


def espaco_livre(request):
    submetido = False
    form = FormEspacoLivre(request.POST or None)

    if form.is_valid():
        submetido = True
        atenuacaoEspacoLivre_grafico(
            form.cleaned_data['frequencia'],
            form.cleaned_data['potencia'],
            form.cleaned_data['prx_minima']
        )

    context = {'form': form, 'submetido': submetido}

    return render(request, "website/espaco-livre.html", context)


def okumura_hata(request):
    submetido = False
    result = 0
    form = FormOkumuraHata(request.POST or None)

    if form.is_valid():
        submetido = True
        result = functions.okumura_hata(
            form.cleaned_data['frequencia'],
            form.cleaned_data['distancia'],
            form.cleaned_data['hbe'],
            form.cleaned_data['hm'],
            form.cleaned_data['tipoAmbiente']
        )

    context = {'form': form, 'submetido': submetido, 'result': result}

    return render(request, "website/okumura_hata.html", context)


def walfisch_ikegami(request):
    submetido = False
    result = 0
    form = FormWalfischIkegami(request.POST or None)

    if form.is_valid():
        submetido = True
        result = functions.walfisch_ikegami(
            form.cleaned_data['frequencia'],
            form.cleaned_data['distancia']
        )

    context = {'form': form, 'submetido': submetido, 'result': result}

    return render(request, "website/walfisch_ikegami.html", context)


def tamanho_cluster(request):
    submetido = False
    result = 0
    form = FormTamanhoCluster(request.POST or None)

    if form.is_valid():
        submetido = True
        result = tamanho_minimo_cluster(
            form.cleaned_data['c_i_db'],
            form.cleaned_data['n']
        )

    context = {'form': form, 'submetido': submetido, 'result': result}

    return render(request, "website/tamanho_cluster.html", context)


def grafico_CI_Ncp(request):
    submetido = False
    form = FormGraficoCINcp(request.POST or None)

    if form.is_valid():
        submetido = True
        grafico_CI_NCP(
            form.cleaned_data['n']
        )

    context = {'form': form, 'submetido': submetido}

    return render(request, "website/graficoCINCP.html", context)


def grafico_Planeamento(request):
    submetido = False
    form = FormGraficoPlaneamento(request.POST or None)

    if form.is_valid():
        submetido = True
        ficheiro = cria_planeamento_hexagonal(
            form.cleaned_data['n_pixels_x'],
            form.cleaned_data['n_pixels_y'],
            form.cleaned_data['raio'],
            form.cleaned_data['ptx'],
            form.cleaned_data['frequencia'],
            form.cleaned_data['pixel_size']
        )
        cria_mapas_celulas(ficheiro)

    context = {'form': form, 'submetido': submetido}

    return render(request, "website/graficos_planeamento.html", context)


def Erlang_B(request):
    return render(request, "website/erlangB.html")


def probabilidade_bloqueio(request):
    submetido = False
    result = 0.0
    form = FormProbabilidadeDeBloqueio(request.POST or None)

    if form.is_valid():
        submetido = True
        result = calculaProbabilidadeDeBloqueio(
            form.cleaned_data['t'],
            form.cleaned_data['n']
        )

    context = {'form': form, 'submetido': submetido, 'result': result}

    return render(request, "website/probabilidade_bloqueio.html", context)


def quantidade_canais(request):
    submetido = False
    result = 0.0
    form = FormQuantidadeDeCanais(request.POST or None)

    if form.is_valid():
        submetido = True
        result = calculaQuantidadeCanais(
            form.cleaned_data['pb'],
            form.cleaned_data['t']
        )

    context = {'form': form, 'submetido': submetido, 'result': result}

    return render(request, "website/quantidade_canais.html", context)


def trafego_oferecido(request):
    submetido = False
    result = 0.0
    form = FormTrafegoOferecido(request.POST or None)

    if form.is_valid():
        submetido = True
        result = calculaTrafegoOferecido(
            form.cleaned_data['pb'],
            form.cleaned_data['n']
        )

    context = {'form': form, 'submetido': submetido, 'result': result}

    return render(request, "website/trafego_oferecido.html", context)
