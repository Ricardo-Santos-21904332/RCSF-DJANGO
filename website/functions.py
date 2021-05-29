import math
from math import log10
from math import log
import matplotlib.pyplot as plt
import matplotlib
import json
import seaborn as sns

matplotlib.use('agg')


def atenuacaoEspacoLivre_grafico(f: "frequencia [GHz]", ptx: "potencia [dBm]", prx_min: "potencia minima [dBm]"):
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


def tamanho_minimo_cluster(c_i_db, n):
    c_i = 10 ** (c_i_db / 10)
    rcc = pow(c_i * 6, (1 / n))
    n_cp = int(math.ceil((rcc ** 2) / 3))
    return n_cp


def grafico_CI_NCP(n):
    n_cp = [3, 4, 7, 12, 13, 19]
    lista_c_i = []
    for i in n_cp:
        rcc = math.sqrt(3 * i)
        c_i = (rcc ** n) / 6
        c_i_db = 10 * math.log10(c_i)
        lista_c_i.append(c_i_db)
    plt.bar(n_cp, lista_c_i)
    plt.xlabel('N_CP')
    plt.ylabel('C/I [dB]')
    plt.title('C/I vs N_CP')
    plt.savefig('website/static/website/images/CIvsNCP.jpg')
    plt.close()


def cria_planeamento_hexagonal(n_pixels_x, n_pixels_y, R: 'raio em pixels', ptx, frequencia: 'GHz', pixel_size):
    """
    Para uma grelha de pixels e um raio de célula, cria um planeamento hexagonal de células
    retornando um JSON com coordenadas e configuração de cada célula

    :param n_pixels_x: numero de pixels no eixo dos x
    :param n_pixels_y: numero de pixels no eixo dos y
    :param R: Radio em pixels da célula
    :param ptx: potencia transmitida em dBm
    :param frequencia: frequencia de transmissão em GHz
    :param pixel_size: tamanho do pixel em metro

    :return: JSON com coordenadas e configuração de cada célula
    """

    r = int(math.sqrt(3) / 2 * R)
    celulas = {}
    n_celulas = 0

    x = 0
    y = 0

    while x <= n_pixels_x:
        y = 0
        while y <= n_pixels_y:
            i = str(n_celulas)
            celulas[i] = {'posicao': [x, y], 'ptx': ptx, 'frequencia': frequencia}
            n_celulas += 1
            y += 2 * r
        x += 3 * R

    x = 3 * R // 2
    y = r

    while x <= n_pixels_x:
        y = r
        while y <= n_pixels_y:
            i = str(n_celulas)
            celulas[i] = {'posicao': [x, y], 'ptx': ptx, 'frequencia': frequencia}
            n_celulas += 1
            y += 2 * r
        x += 3 * R

    config = {
        'celulas': celulas,
        'n_pixels_x': n_pixels_x,
        'n_pixels_y': n_pixels_y,
        'pixel_size': pixel_size,
    }

    nome_ficheiro = f'{n_pixels_x}x{n_pixels_y}-r{R}-{pixel_size}m-{ptx}dBm-{frequencia}GHz-{n_celulas}cells.json'
    with open('website/static/website/images/' + nome_ficheiro, 'w') as f:
        json.dump(config, f, indent=4)

    return f'{n_pixels_x}x{n_pixels_y}-r{R}-{pixel_size}m-{ptx}dBm-{frequencia}GHz-{n_celulas}cells.json'


def cria_mapas_celulas(ficheiro):
    with open('website/static/website/images/' + ficheiro) as fp:
        config = json.load(fp)

    mapa = cria_mapa_prx_dB_de_celulas(config)

    if True:
        mapa_best_server = cria_mapa_id_best_server(mapa, config)
        desenha_mapa(mapa_best_server, ficheiro, 'best_server')

    if True:
        mapa_cir = cria_mapa_cir(mapa, config)
        desenha_mapa(mapa_cir, ficheiro, 'cir')

    # if True:
    #   for celula in config['celulas'].keys():
    #        mapa_celula = extrai_mapa(mapa, celula)
    #        desenha_mapa(mapa_celula, ficheiro, celula)

    return


def cria_mapa_vazio(size_x, size_y):
    return [[{} for _ in range(size_y)] for _ in range(size_x)]


def calcula_distancia(c_x, c_y, x, y, pixel_size):
    # cálculo da distancia entre dois pontos
    # usando o teorema de Pitágoras e a dimensão do pixe

    distancia = math.sqrt((c_x - x) ** 2 + (c_y - y) ** 2) * pixel_size

    return distancia if distancia != 0 else pixel_size


def free_space(f: "frequencia [GHz]", d: "distancia [m]") -> "atenuação [dB]":
    """
        esta função recebe:
          - f:"frequencia [GHz]"
          - d:"distancia [m]"
        esta função retorna a atenuação de propagação em espaço livre [dB]
    """
    return 32.44 + 20 * math.log10(d / 1000) + 20 * math.log10(f * 1000)


def cria_mapa_prx_dB_de_celulas(config):
    """Cria mapa de potencia recebida em dB de um conjunto de celulas"""

    mapa = cria_mapa_vazio(config['n_pixels_x'], config['n_pixels_y'])

    for y in range(0, config['n_pixels_y']):
        for x in range(0, config['n_pixels_x']):

            for celula, info in config['celulas'].items():
                c_x = info['posicao'][0]
                c_y = info['posicao'][1]

                distancia = calcula_distancia(c_x, c_y, x, y, config['pixel_size'])
                path_loss = free_space(info['frequencia'], distancia)
                prx = info['ptx'] - path_loss
                mapa[x][y][celula] = prx

    return mapa


def cria_mapa_id_best_server(mapa, config):
    mapa_cobertura = [[{} for _ in range(config['n_pixels_y'])] for _ in range(config['n_pixels_x'])]

    cor = {}
    for i, item in enumerate(list(config['celulas'])):
        cor[item] = i

    for y in range(0, config['n_pixels_y']):
        for x in range(0, config['n_pixels_x']):
            p = mapa[x][y]
            celula = max(list(p.items()), key=lambda e: e[1])
            mapa_cobertura[x][y] = cor[celula[0]]

    return mapa_cobertura


def cria_mapa_cir(mapa, config):
    mapa_cir = [[None for _ in range(config['n_pixels_y'])] for _ in range(config['n_pixels_x'])]

    for y in range(0, config['n_pixels_y']):
        for x in range(0, config['n_pixels_x']):
            mapa_cir[x][y] = cir(mapa[x][y])

    return mapa_cir


def cir(p):
    """
    calcula CIR de dicionario de prx[dBm] de celulas num ponto. considera C o melhor dos sinais.
    """

    lista_prx_dB_cells = list(p.values())
    lista_prx_dB_cells.sort(reverse=True)

    c_dB = lista_prx_dB_cells[0]  # best server signal strength
    lista_prx_dB_i_cells = lista_prx_dB_cells[1:]  # remaining received power levels

    soma_i_linear = 0
    for prx_dB_i_cell in lista_prx_dB_i_cells:
        soma_i_linear += 10 ** (prx_dB_i_cell / 10)  # soma linear de px das celulas interferences
    soma_i_dB = 10 * log10(soma_i_linear)

    cir_dB = c_dB - soma_i_dB

    return cir_dB


def extrai_mapa(mapa, celula):
    mapa_celula = []
    for linha in mapa:
        linha_celula = []
        for elemento in linha:
            linha_celula.append(elemento[celula])
        mapa_celula.append(linha_celula.copy())

    return mapa_celula


def desenha_mapa(mapa, nome, tipo):
    plt.clf()
    ax = sns.heatmap(mapa)
    # f'{nome[:-5]}-{tipo}
    plt.savefig(f'website/static/website/images/{tipo}.png')
