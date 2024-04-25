import numpy as np

entrada = np.array([[0.5, 0.8], [0.2, 0.4]])
saida = np.array([1, 0])
pesos = np.array([0.2, -0.1])
taxa_apr = 0.1
epocas = 1000

def stepFunction(soma):
    if soma >= 0:
        return 1
    else:
        return 0

def output(passado):
    s = passado.dot(pesos)
    return stepFunction(s)

def treinarPerceptron():
    erros_por_epoca = []  # Lista para armazenar o erro total de cada época
    for epoca in range(epocas):
        erroTotal = 0
        for i in range(len(entrada)):
            saidaCalculada = output(entrada[i])
            erro = saida[i] - saidaCalculada
            erroTotal += abs(erro)
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_apr * entrada[i][j] * erro)
        erros_por_epoca.append(erroTotal)  # Adiciona o erro total desta época à lista
        if erroTotal == 0:
            print("Pesos:", pesos, "Erro total:", erroTotal)
            break
        print("Época:", epoca+1, "Erro total:", erroTotal, "Pesos atualizados:", pesos)
    return erros_por_epoca

erros = treinarPerceptron()
