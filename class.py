#Importando as bibliotecas
import sqlite3
import re
print("=========================================")
print("Sistema De Controle Da Produção De Leite\n")
n = int(input("1 - buscar vaca\n2 - Cadastrar vaca\n=========================================\nDigite uma opção: "))

#Criando a matriz
ordenhadas = []
#Conectando ao Sqlite
conn = sqlite3.connect('vaca.db')
cursor = conn.cursor()
#Buscando as vacas cadastradas
cursor.execute("SELECT codigo FROM vaca")
#Criando a matriz com o código de cada vaca cadastrada
resultado = cursor.fetchall()
for linha in resultado:
    z = str(linha)
    regex_syntax = r"\D"
    num_str = re.sub(regex_syntax, "", z)
    a = int(num_str)
    ordenhadas.append(a)
#Verificar se o usuário escolheu buscar 
if n == 1:
    codigo = int(input("Digite o código da vaca: "))
    #Criando a função busca binária
    def busca_binaria(lista, codigo):
            minimo = 0 
            maximo = len(lista)-1
            encontrado = False
        
            while minimo <= maximo and not encontrado:
                meio_lista = (minimo + maximo)//2
                if lista[meio_lista] == codigo:
                    encontrado = True
                else:
                    if codigo < lista[meio_lista]:
                        maximo = meio_lista-1
                    else:
                        minimo = meio_lista+1
            #Verificar se foi feita a ordenha do animal escolhido
            if encontrado == True:
                print("-----------------------------------------")
                print("PROCESSO DE ORDENHA REALIZADO")
                input()
            else:
                print("-----------------------------------------")
                print("PROCESSO DE NÃO ORDENHA REALIZADO")
                input()
    #Executando a função de busca
    print(busca_binaria(ordenhadas, codigo))
#erificar se o usuário escolheu cadastrar
elif n == 2:
    ordenhado = int(input("Digite o código da vaca: "))
    data = input("Digite a data: ")
    #Conectando ao Sqlite e fazendo um INSERT
    conn = sqlite3.connect('vaca.db')
    cursor = conn.cursor()
    insert = """
    INSERT INTO vaca
    (codigo, data)
    VALUES ({}, {})
    """.format(ordenhado, data)
    count = cursor.execute(insert)
    conn.commit()
    print("cadastro realizado")
    cursor.close()
    input()
