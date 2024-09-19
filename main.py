from collections import Counter
from typing import List
def q1a(nums: List[int]) -> bool:
    for i in nums:
        if nums.count(i) > 1:
            return True
        else:
            return False

def q1b(nums: List[int]) -> bool:
    dicionario = {
        "Repete": True,
        "n_Repete": False
    }
    for i in nums:
        if nums.count(i) > 1:
            return dicionario['Repete']
        else:
            return dicionario['n_Repete']



def q2(s: str,t: str) -> bool:
    lista_s = []
    lista_t = []
    for i in s:
        lista_s.append(i)
    for i in t:
        lista_t.append(i)
    organizada_s = sorted(lista_s)
    organizada_t = sorted(lista_t)
    if organizada_s == organizada_t:
        return True
    else:
        return False

def q3() -> int:
    # import csv
    # with open('estoque.csv', 'r') as estoque_csv:
    #     dicionario = csv.DictReader(estoque_csv)
    #     for linha in dicionario:
    #         print(linha['PreÃ§o'])
    # with open('estoque_csv', w) as estoqueM_csv:
    pass

def q4():
    def ler_valores():
        lista = []
        while True:
            num = int(input())
            if num == 0:
                break
            else: 
                lista.append(num)
        return lista
    def processa_lista(lista):
        pares = []
        impares = []
        mais_antigo_pares = 0
        mais_antigo_impares = 0
        for i in lista:
            if i % 2 == 0:
                if len(pares) == 5:
                    print(mais_antigo_pares)
                    pares[mais_antigo_pares] = i
                    mais_antigo_pares += 1
                    
                else:
                    pares.append(i)
                
            if i % 2 != 0:
                if len(impares) == 5:
                    print(mais_antigo_impares)
                    impares[mais_antigo_impares] = i
                    mais_antigo_impares += 1
                    
                else:
                    impares.append(i)


        return pares, impares
    
    
    
    
    # lista = ler_valores()
    # pares, impares = processa_lista(lista)
    # print(pares, impares)



if __name__=="__main__":
    # teste sua questão manualmente aqui
    q3()
    pass
