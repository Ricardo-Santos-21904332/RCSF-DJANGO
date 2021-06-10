from django import forms


class FormEspacoLivre(forms.Form):
    frequencia = forms.IntegerField(label="Frequência [MHz]")
    potencia = forms.IntegerField(label="Potência [dBm]")
    prx_minima = forms.IntegerField(label="Potencia mínima [dBm]")


class FormOkumuraHata(forms.Form):
    cidades = (
        ("pequena", "Pequena"),
        ("media", "Média"),
        ("grande", "Grande"),
    )
    frequencia = forms.IntegerField(label="Frequência [MHz]")
    hbe = forms.IntegerField(label="Altura efectiva da estação base (Hbe) [m]")
    distancia = forms.IntegerField(label="Distância do móvel à base [Km]")
    hm = forms.IntegerField(label="Altura do móvel ao solo (Hm) [m]")
    tipoCidade = forms.TypedChoiceField(label="Tipo de Cidade", choices=cidades)


class FormWalfischIkegami(forms.Form):
    frequencia = forms.IntegerField(label="Frequência [MHz]")
    distancia = forms.FloatField(label="Distância [Km]")


class FormTamanhoCluster(forms.Form):
    c_i_db = forms.FloatField(label="C/I [dB]")
    n = forms.FloatField(label="Coeficiente de Atenuação (n)")


class FormGraficoCINcp(forms.Form):
    n = forms.FloatField(label="Coeficiente de Atenuação (n)")


class FormGraficoPlaneamento(forms.Form):
    n_pixels_x = forms.IntegerField(label="Número de pixels (eixo X)")
    n_pixels_y = forms.IntegerField(label="Número de pixels (eixo Y)")
    raio = forms.IntegerField(label="Raio em pixels")
    ptx = forms.IntegerField(label="Potência transmitida")
    frequencia = forms.FloatField(label="Frequência [GHz]")
    pixel_size = forms.IntegerField(label="Tamanho do pixel")


class FormProbabilidadeDeBloqueio(forms.Form):
    t = forms.IntegerField(label="Tráfego Oferecido (T)")
    n = forms.IntegerField(label="Quantidade De Canais (N)")


class FormQuantidadeDeCanais(forms.Form):
    t = forms.IntegerField(label="Tráfego Oferecido (T)")
    pb = forms.FloatField(label="Probabilidade De Bloqueio (Pb)")


class FormTrafegoOferecido(forms.Form):
    n = forms.IntegerField(label="Quantidade De Canais (N)")
    pb = forms.FloatField(label="Probabilidade De Bloqueio (Pb)")
