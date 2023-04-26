import os
import warnings
warnings.filterwarnings('ignore')

from pandas import read_gbq, read_csv

def getData(query : str, saveFile : str, returnResult : bool = True):
    '''
    Recebe uma query em uma string e salva seu conteúdo no arquivo saveFile.
    Caso desejado, também retorna o DataFrame resultante.
    '''
    df = read_gbq(query)
    df.to_csv(saveFile, index = False)
    if returnResult: return df

def sql_query(queryFile : str, returnResult : bool = True, updateResult : bool = True):
    '''
    Recebe o nome de um arquivo com uma query e, caso updateResult, salva o resultado
    da query na pasta ../data/raw/ com o mesmo nome do arquivo que contém a query.
    Caso returnResult, retorna o DataFrame resultante.
    '''
    if '../sql/' not in queryFile: queryFile = '../sql/' + queryFile
    saveFile = queryFile.replace('../sql/', '').replace('.sql', '.csv')
    if saveFile in os.listdir('../data/raw') and not updateResult and returnResult:
        return read_csv('../data/raw/' + saveFile)
    elif updateResult:
        with open(queryFile, 'r') as f: query = f.read()
        if returnResult: return getData(query, '../data/raw/' + saveFile, True)
        getData(query, '../data/raw/' + saveFile, False)