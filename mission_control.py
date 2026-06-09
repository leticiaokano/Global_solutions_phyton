# ==================================
# MISSION CONTROL AI
# ==================================

missao = "Fiap - Espaçial 2"
equipe = "Equipe GS 3"

dados_missao = [
    [22, 95, 90, 98, 92],
    [25, 85, 78, 95, 88],
    [29, 70, 65, 92, 80],
    [33, 55, 48, 88, 68],
    [37, 35, 25, 84, 52],
    [32, 60, 40, 86, 60]
]

areas = [
    "Temperatura",
    "Comunicacao",
    "Bateria",
    "Oxigenio",
    "Estabilidade"
]

# Funções

def analisar_temperatura(valor):
    if valor > 35:
        return 2
    elif valor > 30 or valor < 18:
        return 1
    else:
        return 0

def analisar_comunicacao(valor):
    if valor < 30:
        return 2
    elif valor < 60:
        return 1
    else:
        return 0

def analisar_bateria(valor):
    if valor < 20:
        return 2
    elif valor < 50:
        return 1
    else:
        return 0

def classificar_ciclo(risco):
    if risco <= 2:
        return "ESTAVEL"
    elif risco <= 5:
        return "ATENCAO"
    else:
        return "CRITICA"

def analisar_tendencia(inicio, fim):
    if fim > inicio:
        return "PIOROU"
    elif fim < inicio:
        return "MELHOROU"
    else:
        return "ESTAVEL"

# Variáveis para armazenar resultados

riscos = []
pontos_area = [0, 0, 0, 0, 0]

# Análise dos ciclos

for i, ciclo in enumerate(dados_missao):

    risco_temp = analisar_temperatura(ciclo[0])
    risco_com = analisar_comunicacao(ciclo[1])
    risco_bat = analisar_bateria(ciclo[2])

    # Oxigênio
    if ciclo[3] < 80:
        risco_oxi = 2
    elif ciclo[3] < 90:
        risco_oxi = 1
    else:
        risco_oxi = 0

    # Estabilidade
    if ciclo[4] < 40:
        risco_est = 2
    elif ciclo[4] < 70:
        risco_est = 1
    else:
        risco_est = 0

    risco_total = (
        risco_temp +
        risco_com +
        risco_bat +
        risco_oxi +
        risco_est
    )

    riscos.append(risco_total)

    pontos_area[0] += risco_temp
    pontos_area[1] += risco_com
    pontos_area[2] += risco_bat
    pontos_area[3] += risco_oxi
    pontos_area[4] += risco_est

    print("\nCICLO", i + 1)
    print("Risco:", risco_total)
    print("Classificacao:", classificar_ciclo(risco_total))

# Relatório Final

print("\n========== RELATORIO FINAL ==========")

print("Missao:", missao)
print("Equipe:", equipe)

print("Tendencia:", analisar_tendencia(riscos[0], riscos[-1]))

indice = pontos_area.index(max(pontos_area))

print("\nArea mais afetada:", areas[indice])

print("\nPontuacao das areas:")

for i in range(len(areas)):
    print(areas[i], "-", pontos_area[i], "pontos") 
