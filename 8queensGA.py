import numpy as np
import random

def converte_tabuleiro(VT):
    N = len(VT)
    T = [[0] * N for _ in range(N)]
    for col in range(N):
        lin = VT[col] - 1
        T[lin][col] = 1
    return T

def conta_ataques_linhas(VT):
    ataques = 0
    N = len(VT)
    for col1 in range(N):
        lin1 = VT[col1]
        for col2 in range(col1 + 1, N):
            lin2 = VT[col2]
            if lin1 == lin2:
                ataques += 1
    return ataques

def conta_ataques_diagonais(VT):
    ataques = 0
    N = len(VT)
    for col1 in range(N):
        lin1 = VT[col1]
        for col2 in range(col1 + 1, N):
            lin2 = VT[col2]
            if abs(lin1 - lin2) == abs(col1 - col2):
                ataques += 1
    return ataques

def conta_ataques(VT):
    ataques = conta_ataques_linhas(VT) + conta_ataques_diagonais(VT)
    return ataques

def gera_vizinhos(VT):
    N = len(VT)
    vizinhos = []
    for col in range(N):
        for lin in range(1, N + 1):
            if lin != VT[col]:
                vizinho = VT.copy()
                vizinho[col] = lin
                vizinhos.append(vizinho)
    return vizinhos

def gera_tuplas_custos(Populacao):
    return [(conta_ataques(individuo), individuo) for individuo in Populacao]

def mutacao(VT, p_mutacao=0.20):
    VT_mutated = VT.copy()
    N = len(VT)
    if np.random.rand() < p_mutacao:
        col = np.random.randint(N)
        linha = np.random.randint(1, N + 1)
        VT_mutated[col] = linha
    return VT_mutated

def crossover(Parent1, Parent2):
    N = len(Parent1)
    c = np.random.randint(1, N - 1)
    child1 = Parent1[:c] + Parent2[c:]
    child2 = Parent2[:c] + Parent1[c:]
    return child1, child2

def selecao(Populacao):
    Candidato1 = random.choice(Populacao)
    Candidato2 = random.choice(Populacao)
    return Candidato1 if conta_ataques(Candidato1) <= conta_ataques(Candidato2) else Candidato2

def gera_individuo(n_cols):
    return np.random.randint(1, n_cols + 1, size=n_cols).tolist()

def gera_populacao_inicial(N, tam_pop):
    return [gera_individuo(N) for _ in range(tam_pop)]

def algoritmo_genetico(N=8, tam_pop=10, p_mutacao=0.20, max_geracoes=1000):
    populacao = gera_populacao_inicial(N, tam_pop)
    fitness = gera_tuplas_custos(populacao)
    geracao = 0

    while geracao < max_geracoes:
        nova_populacao = []
        while len(nova_populacao) < tam_pop:
            p1 = selecao(populacao)
            p2 = selecao(populacao)
            child1, child2 = crossover(p1, p2)
            child1 = mutacao(child1, p_mutacao)
            child2 = mutacao(child2, p_mutacao)
            nova_populacao.extend([child1, child2])

        populacao = nova_populacao[:tam_pop]
        fitness = gera_tuplas_custos(populacao)
        melhor_fitness = min(fitness)[0]
        if melhor_fitness == 0:
            break
        geracao += 1

    melhor_solucao = min(fitness, key=lambda x: x[0])[1]
    return melhor_solucao, conta_ataques(melhor_solucao), geracao

# Exemplo de execução
melhor_solucao, num_ataques, geracao = algoritmo_genetico()
print(f'Melhor solução encontrada: {melhor_solucao} com {num_ataques} ataques em {geracao} gerações')
