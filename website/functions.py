import math
from math import log10
from math import log
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('agg')


def atenuacaoEspacoLivre(f: "frequencia [GHz]", ptx: "potencia [dBm]", prx_min: "potencia minima [dBm]"):
    l_d = []
    l_prx = []
    l_prx_min = []

    d = 0
    l = 0
    while (ptx - l > prx_min - 2):
        d += 1
        l = 32.44 + 20 * math.log10(d / 1000000) + 20 * math.log10(f * 1000)
        l_prx.append(ptx - l)

    l_d = list(range(1, d + 1))
    l_prx_min = [prx_min for i in range(1, d + 1)]

    plt.style.use('seaborn-bright')
    plt.plot(l_d, l_prx, label="Prx")
    plt.plot(l_d, l_prx_min, label="Prx_min")

    plt.xlabel('distância [m]')
    plt.ylabel('Potência recebida [dBm]')
    plt.title(f'Nível de sinal recebido (Ptx = {ptx} dBm e f = {f} GHz)')
    plt.legend()
    plt.savefig('website/static/website/images/free-space.jpg')
    plt.close()


def l_free_space(d: 'km', f: 'MHz'):
    return 32.44 + 20 * log10(d) + 20 * log10(f)


def atenuacaoEspacoLivre(freq):
    lista_d = []
    lista_free_space = []
    for d in range(1, 1000 + 1):
        lista_d.append(d)
        lista_free_space.append(l_free_space(d / 1000, freq))
    plt.plot(lista_d, lista_free_space)
    plt.title(f"{freq} MHz")
    plt.xlabel('Distância [m]')
    plt.ylabel('Atenuacao em Espaço livre [dB]')
    plt.grid()
    # criar nome para o novo gráfico
    nome_grafico = f"plot_atenuacao_{freq}_MHz_.jpg"
    plt.savefig('website/static/website/images/' + nome_grafico)
    plt.close()
    return nome_grafico


def propagacaoEspacoLivre(freq):
    Pe = 100  # mW
    Ge = 0  # dBi
    Gr = 0  # dBi
    lista_d = []
    lista_pr = []
    lista_prx_min = []
    pe = 10 * log10(Pe)  # dBm
    for d in range(1, 1000 + 1):
        lista_d.append(d)
        lista_prx_min.append(-70)
        pr = pe + Ge - l_free_space(d / 1000, freq) + Gr
        lista_pr.append(pr)
    plt.plot(lista_d, lista_pr)
    plt.title(f"{freq} MHz")
    plt.xlabel('Distância [m]')
    plt.ylabel('Potência recebida [dBm]')
    plt.grid()
    # criar nome para o novo gráfico
    nome_grafico = f"plot_propagacao_{freq}_MHz_.jpg"
    plt.savefig('website/static/website/images/' + nome_grafico)
    plt.close()


def hmu(hm, f, tipoCidade):
    if tipoCidade == "pequena":
        return (1.10 * log(f) - 0.70) * hm - (1.56 * log(f) - 0.80)
    elif tipoCidade == "media":
        return 8.29 * (log(1.54 * hm) ** 2) - 1.10
    elif tipoCidade == "grande":
        return 3.20 * (log(11.75 * hm) ** 2) - 4.97
    else:
        return


def okumura_hata(f, d, hbe, hm, tipoCidade):
    """
    Esta função recebe:
        -Frequência em MHz
        -Hbe em m
        -Distância em Km
        -Hm em metros
        -tipoCidade (pequena, média ou grande)
    E retorna a mediana da atenuação em dB
    """
    
    if 150 < f < 1500 and 1 < d < 20 and 30 < hbe < 200 and 1 < hm < 10:
        try:
            Hmu = hmu(hm, f, tipoCidade)
            lp = 69.55 + 26.16 * log(f) - 13.82 * log(hbe) + (44.90 - 6.55 * log(hbe)) * log(d) - Hmu
            return "{:.2f}".format(lp)
        except:
            return "Erro ao calcular!"
    elif f < 150 or f > 1500 and 1 < d < 20 and 30 < hbe < 200 and 1 < hm < 10:
        return "Frequência inválida!"
    elif 150 < f < 1500 and d < 1 or d > 20 and 30 < hbe < 200 and 1 < hm < 10:
        return "Distância inválida!"
    elif 150 < f < 1500 and 1 < d < 20 and hbe < 30 or hbe > 200 and 1 < hm < 10:
        return "Hbe inválido!"
    elif 150 < f < 1500 and 1 < d < 20 and 30 < hbe < 200 and hm < 1 or hm > 10:
        return "Hm inválido!"
    else:
        return "Parâmetros inválidos!"


def walfisch_ikegami(f, d):
    if d <= 0.02 and f < 800 or f > 2000:
        return "Parâmetros inválidos!"
    elif d <= 0.02 and 800 < f < 2000:
        return "Distância inválida!"
    elif d > 0.02 and 800 < f < 2000:
        lp = 42.6 + 26 * log10(d) + 20 * log10(f)
        return "{:.2f}".format(lp)
    else:
        return "Frequência inválida!"
