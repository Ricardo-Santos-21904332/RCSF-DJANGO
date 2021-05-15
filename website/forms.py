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
