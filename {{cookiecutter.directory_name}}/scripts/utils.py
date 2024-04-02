import os
import warnings
warnings.filterwarnings('ignore')

from pandas import read_gbq, read_csv
from plotly.graph_objects import Figure

def get_data(query : str, save_file : str, return_result : bool = True):
    '''
    Executa uma consulta (query) no Google BigQuery e salva o resultado em um arquivo CSV.

    Args:
        query (str): A consulta a ser executada no Google BigQuery. Deve ser uma string válida.
        save_file (str): O nome do arquivo CSV onde o resultado será salvo.
                         Certifique-se de fornecer o caminho completo ou o arquivo será salvo no diretório atual.
        return_result (bool, opcional): Indica se o DataFrame resultante deve ser retornado.
                                        O valor padrão é True.

    Returns:
        pandas.DataFrame or None: Se return_result for True, a função retornará o DataFrame
                                  resultante da consulta. Caso contrário, retorna None.

    Exemplo:
        >>> query = "SELECT * FROM minha_tabela WHERE coluna = 'valor';"
        >>> file_name = "resultado.csv"
        >>> df = get_data(query, file_name)
        # Executa a consulta, salva o resultado em "resultado.csv" e retorna o DataFrame df.

        >>> query2 = "SELECT COUNT(*) AS total FROM outra_tabela;"
        >>> file_name2 = "contagem.csv"
        >>> get_data(query2, file_name2, return_result=False)
        # Executa a consulta, salva o resultado em "contagem.csv" e não retorna o DataFrame.
    '''
    df = read_gbq(query, project_id='everest-bigquery')
    df.to_csv(save_file, index = False)
    if return_result: return df

def sql_query(query_file : str, return_result : bool = True,
              update_result : bool = True, output_path : str = '../data/raw/',
              query_path : str = '../sql/'):
    '''
    Executa uma consulta (query) armazenada em um arquivo, podendo salvar o resultado em um arquivo CSV
    e/ou retornar o DataFrame resultante.

    Args:
        query_file (str): O nome do arquivo contendo a query a ser executada.
                          O arquivo deve estar na pasta com os códigos compilados.
        return_result (bool, opcional): Indica se o DataFrame resultante deve ser retornado.
                                        O valor padrão é True.
        update_result (bool, opcional): Indica se o resultado da consulta deve ser atualizado,
                                        mesmo que já exista um arquivo de saída com o mesmo nome.
                                        O valor padrão é True.
        output_path (str, opcional): O caminho para a pasta onde o resultado será salvo.
                                     O valor padrão é '../data/raw/'.
        query_path (str, opcional): O caminho para a pasta contendo os arquivos com as queries.
                                    O valor padrão é '../sql/'.

    Returns:
        pandas.DataFrame or None: Se return_result for True, a função retornará o DataFrame
                                  resultante da consulta. Caso contrário, retorna None.

    Exemplo:
        >>> sql_file = "minha_consulta.sql"
        >>> df = sql_query(sql_file)
        # Executa a consulta armazenada em "minha_consulta.sql", salva o resultado em
        # "../data/raw/nome_do_arquivo_da_query.csv" e retorna o DataFrame df.

        >>> query_file = "outra_consulta.sql"
        >>> output_folder = "../data/output/"
        >>> sql_query(query_file, return_result=False, update_result=False, output_path=output_folder)
        # Executa a consulta armazenada em "outra_consulta.sql", salva o resultado em
        # "../data/output/nome_do_arquivo_da_query.csv" apenas se o arquivo ainda não existir, e não retorna o DataFrame.
    '''

    if '/' in query_file: query_file = query_file.split('/')[-1]
    query_file = query_path + query_file
    save_file = query_file.replace(query_path, '').replace('.sql', '.csv')

    if not update_result and return_result:
        if save_file in os.listdir(output_path):
            return read_csv(output_path + save_file)
    
    with open(query_file, 'r') as f: query = f.read()
    save_file = output_path + save_file

    if return_result: return get_data(query, save_file, True)
    else: get_data(query, save_file, False)

def show_fig(fig : Figure, static : bool = False):
    '''
    Exibe um gráfico do Plotly. Ideal para exibir gráficos de modo visualizável no GitHub.

    Args:
        fig (plotly.graph_objects.Figure): O gráfico a ser exibido.
        static (bool, opcional): Indica se o gráfico deve ser exibido em formato estático.
                                 O valor padrão é False.

    Exemplo:
        >>> import plotly.graph_objects as go
        >>> fig = go.Figure(data = go.Scatter(x = [1, 2, 3], y = [4, 5, 6]))
        >>> show_fig(fig)
        # Exibe o gráfico normalmente, permitindo interação.

        >>> fig2 = go.Figure(data = go.Scatter(x = [1, 2, 3], y = [4, 5, 6]))
        >>> show_fig(fig2, static = True)
        # Exibe o gráfico em formato estático, ideal para exibição no GitHub.
    '''
    fig.show(renderer="png" if static else None)

if __name__ == '__main__':
    from glob import glob
    for query in glob('../sql/*.sql'): sql_query(query, return_result = False)
