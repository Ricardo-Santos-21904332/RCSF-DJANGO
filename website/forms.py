from django import forms


class FormEspacoLivre(forms.Form):
    frequencia = forms.IntegerField(label="Frequência [MHz]")
    potencia = forms.IntegerField(label="Potência [dBm]")
    prx_minima = forms.IntegerField(label="Potencia mínima [dBm]")


class FormOkumuraHata(forms.Form):
    ambientes = (
        ("rural", "Rural"),
        ("suburbano", "Suburbano"),
        ("urbano", "Urbano"),
    )
    frequencia = forms.IntegerField(label="Frequência [MHz]")
    hbe = forms.IntegerField(label="Altura efectiva da estação base (Hbe) [m]")
    distancia = forms.IntegerField(label="Distância do móvel à base [Km]")
    hm = forms.IntegerField(label="Altura do móvel ao solo (Hm) [m]")
    tipoAmbiente = forms.TypedChoiceField(label="Tipo de Ambiente", choices=ambientes)


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


class FormHeatmapAntena(forms.Form):
    antenas = (
        ("729265_0948_X_CO.msi", "729265_0948_X_CO.msi"),
        ("739633_0948_X_CO_P45.msi", "739633_0948_X_CO_P45.msi"),
        ("741785_0948_X_CO_P45.msi", "741785_0948_X_CO_P45.msi"),
    )
    ptx = forms.IntegerField(label="Potência Transmitida")
    f = forms.IntegerField(label="Frequência [MHz]")
    j_antena = forms.IntegerField(label="Coordenada j da antena")
    i_antena = forms.IntegerField(label="Coordenada i da antena")
    azimute = forms.IntegerField(label="Azimute")
    antena = forms.TypedChoiceField(label="Antena", choices=antenas)
    ganho_recepcao = forms.IntegerField(label="Ganho de recepção")
    pixel = forms.IntegerField(label="Pixel")


class FormDiagramaRadiacaoAntena(forms.Form):
    antenas = (
        ("729265_0948_X_CO.msi", "729265_0948_X_CO.msi"),
        ("739633_0948_X_CO_P45.msi", "739633_0948_X_CO_P45.msi"),
        ("741785_0948_X_CO_P45.msi", "741785_0948_X_CO_P45.msi"),
    )
    ganho_minimo = forms.IntegerField(label="Ganho de mínimo")
    antena = forms.TypedChoiceField(label="Antena", choices=antenas)
