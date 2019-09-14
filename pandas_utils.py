import pandas as pd
import glob
import os


# Criar dataframe
def create_df():
    return pd.DataFrame(columns = ['ID', 'DATA', 'NOME'])


# Nova linha no dataframe
def set_append(df, li):
    df = df.append({'ID':li[0], 'DATA':li[1], 'NOME':li[2]}, ignore_index=True)
    return df


# Altera ou insere valores em branco
def set_value(df, i, col, data):
    df.loc[i, col] = data
    return df


# Obtém um valor específico
def get_value(df, i, col):
    return df.iloc[i][col] # ex: 1, 'NOME'


# Obtém total de linhas
def get_lines(df, col):
    return df[col].count() # ex: 'ID'


# Deleta uma linha
def drop_line(df, value):
    df = df.drop([value])
    return df


# Deleta uma coluna
def drop_column(df, col, ax):
    df = df.drop(col, axis=ax) # ex: 'NOME', 1
    return df


# Importa vários CSVs de um único diretório
def import_all_csv(dir_csv):
    all_csv = glob.glob(dir_csv + '*.csv')
    li = []

    for csv in all_csv:
        df_temp = pd.read_csv(csv, encoding='ISO-8859-1', sep=',')
        li.append(df_temp)

    return pd.concat(li, sort=False)


# Cria arquivo CSV
def create_csv(df, dir_csv):
    df.to_csv(dir_csv)


if __name__ == '__main__':
    pass