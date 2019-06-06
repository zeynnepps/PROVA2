#exercicio1

data = int(input('Digite uma data:'))
mes = str(input('Digite um mes:'))
ano = int(input('Digite um ano:'))

def verificar_ano(data, mes, ano):
    return ano
print(ano)

#exercicio2

with open('series.csv', 'r', encoding='utf-8') as file:
    for line in file:
        linha = line
        lista = linha.split(',')
        print(lista)
    if lista[5] and lista[6] == '10':
        serie = {'série': lista[0],
                 'episódio': lista[1] and lista[2],
                 'nota IMDB': lista[5],
                 'nota Netflix': lista[6]
                 }
        print(serie)

#exercicio3

with open('series.csv', 'r', encoding='utf-8') as file:
    lista_ate2009:[]
    lista_entre_2010_e_2019:[]

    def ano(lista[3]):
        if ano < 2009:
            lista_ate2009.append()
        elif ano > 2009 and ano < 2019:
            lista_entre_2010_e_2019.append()

    
    

    for line in arquivo.readlines():
        div = linha.split(',')
        




#exercicio4

with open('series.csv', 'r', encoding='utf-8') as file:
    for line in file:
        linha = line
        lista = linha.split(',')
        print(lista[0], ':', lista[5], '(IMDB)', lista[6], '(Netflix)')
        
