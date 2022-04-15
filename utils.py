import pandas as pd
from os import path

def read_excels(input_name, output_name):
    """
    :param input_name: string
    :param output_name: string
    :return: dataframe, dataframe
    """
    i = pd.read_excel(path.abspath(path.abspath(input_name)))
    o = pd.read_excel(path.abspath(path.abspath(output_name)))
    return i, o

def convert_to_str (i, o):
    """
    :param i: dataframe
    :param o: dataframe
    :return: dataframe, dataframe (both of only strings)
    """
    i1 = i.astype(str)
    o1 = o.astype(str)
    return i1, o1

def extract_desired_subset(df1, df2, cols):
    """

    SERVE AD OTTENERE I DATAFRAME CON LE COLONNE DI INTERESSE
    E ANCHE LE RIGHE IN ORDINE

    :param df1: dataframe
    :param df2: dataframe
    :param cols: list of desired columns, strings
    :return: dataframe, dataframe
    """
    dfo1 = df1.loc[df1['Id'].isin(df2['Id'].tolist()), cols]
    df_o1 = dfo1.reindex(df2['Id'].tolist())
    df_o2 = df2[cols]
    return df_o1, df_o2