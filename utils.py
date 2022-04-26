import pandas as pd
import numpy as np
from os import path
from matplotlib import pyplot as plt

def read_excels(input_name, output_name):
    """
    :param input_name: string
    :param output_name: string
    :return: dataframe, dataframe

    NB: CERCA IL PATH ASSOLUTO LOCALE
    """
    i = pd.read_excel(path.abspath(path.abspath(input_name)))
    o = pd.read_excel(path.abspath(path.abspath(output_name)))
    return i, o

def to_excel_iterative(matrix, name, column_value, columns):
    """
    :param matrix: matrix to turn into an excel file
    :param name: string, name of excel file
    :param column_value: string to concatenate to the name, basically
    :param columns: list of columns
    :return: None
    """
    df = pd.DataFrame(matrix)
    txt = name + '_' + column_value + '.xlsx'
    df.to_excel(txt, header = columns)
    return None

def draw_graph(matrix, name, column_value, columns):
    """
    :param matrix: matrix from which use data to draw the graph
    :param name: string, file name
    :param column_value: string to concatenate to the name, basically
    :param columns: list of columns
    :return: None

    CREA UN GRAFICO A BARRE CHE MOSTRA PER OGNI COLONNA QUANTE RIGHE (CIRCA!!) SON PASSATE DA NULL A NON NULL
    DICO CIRCA PERCHè FA SOLO UNA SOMMA DEI VALORI DI TUTTE LE RIGHE PER CIASCUNA COLONNA, QUINDI
    NON SAPPIAMO CON ASSOLUTA PRECISIONE QUANTI +1 CI SONO E QUANTI -1, MA SAPPIAMO SOLO IN GENERALE
    SE L'ALGORITMO TENDE A RIEMPIRE I NULL O NO
    """
    plt.bar(np.arange(matrix.shape[1]), np.sum(matrix, axis=0), tick_label=columns)
    plt.xticks(rotation=45)
    file = name + '_' + column_value + '.png'
    plt.savefig(file, bbox_inches='tight')
    plt.clf()
    return None

def find_unique_values_per_given_column(df, column):
    """
    :param df: dataframe, from which we want to extract the values
    :param column: string, column of the dataframe from which we want to extract the values
    :return: set of the type of the values extracted from the desired column and dataframe

    SERVE AD ESTRARRE I VALORI UNICI DI UNA COLONNA IN UNA MATRICE (PANDAS)
    """
    return set(df[column].tolist())

def subdf_given_column_value(df_i, df_o, column, value):
    """
    :param df_i: dataframe
    :param df_o: dataframe
    :param column: string, desired column
    :param value: desuired value in the column
    :return: dfi, dfo dataframes (input and output) which are formed by all the columns of, respectively,
                      df_i and df_o and the rows characterized by value "value" in the column "column"
    """
    dfi = df_i.loc[df_i[column] == value]
    dfo = df_o.loc[df_o[column] == value]
    return dfi, dfo

def convert_to_str (i, o):
    """
    :param i: dataframe
    :param o: dataframe
    :return: dataframe, dataframe (both of only strings)
    """
    i1 = i.astype(str)
    o1 = o.astype(str)
    return i1, o1

def desired_df(df1, df2, cols):
    """
    SERVE AD OTTENERE I DATAFRAME CON LE COLONNE DI INTERESSE
    E ANCHE LE RIGHE IN ORDINE

    :param df1: dataframe
    :param df2: dataframe
    :param cols: list of desired columns, strings
    :return: dataframe, dataframe same types as df1 (for df_o1) and df2 (for df_o2)
    """
    # dfo1 = df1.loc[df1['Id'].isin(df2['Id'].tolist()), cols] questo serve se l'input ha più righe dell'output
    df_o1 = df1[cols] # riordina le colonne secondo l'ordine della lista in input cols
    df_o2 = df2[cols]
    return df_o1, df_o2