import subprocess
import time
import matplotlib.pyplot as plt

def testar_funcao(executavel, tamanhos):
    """Testa uma função com diferentes tamanhos de entrada"""
    tempos = []
    
    for n in tamanhos:
        # Gera entrada com números de 1 a n
        entrada = f"{n}\n"
        entrada += " ".join(str(i % 10 + 1) for i in range(n))  # 1 a 10 repetindo
        
        inicio = time.perf_counter()
        
        processo = subprocess.run(
            [executavel],
            input=entrada,
            capture_output=True,
            text=True
        )
        
        fim = time.perf_counter()
        
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
        
        print(f"n={n}: {tempo_execucao:.4f}s")
    
    return tempos

# Teste com intervalos
tamanhos = []
for n in range(1000, 50001, 5000):  # 1000 a 50000, passo 5000
    tamanhos.append(n)

print("Testando Função 1...")
tempos1 = testar_funcao("./slow", tamanhos)

print("\nTestando Função 2...")
tempos2 = testar_funcao("./fast", tamanhos)

# Gráfico simples
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos1, 'ro-', label='Função 1 (vector/find)')
plt.plot(tamanhos, tempos2, 'bs-', label='Função 2 (map/set)')
plt.xlabel('Tamanho da entrada (n)')
plt.ylabel('Tempo de execução (s)')
plt.title('Comparação de desempenho')
plt.legend()
plt.grid(True)
plt.savefig('comparacao_simples.png')
plt.show()