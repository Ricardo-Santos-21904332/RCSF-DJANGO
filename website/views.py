from django.shortcuts import render

from . import functions
from .forms import FormEspacoLivre
from .forms import FormOkumuraHata
from .forms import FormWalfischIkegami
from .functions import atenuacaoEspacoLivre


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
        atenuacaoEspacoLivre(
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
            form.cleaned_data['tipoCidade']
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

    return render(request, "website/walfisch-ikegami.html", context)
