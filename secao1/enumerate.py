"""
enumerate - enumera iteráveis (índices)
"""

nomes = ['Maria', 'Carlos', 'João']
nomes.append('Luis')

for indice, nome in enumerate(nomes):
    print(indice, nome)