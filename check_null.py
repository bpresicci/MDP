import pandas as pd

def check_null_changes(input, output):
    """
    :param input: dataframe
    :param output: dataframe
    :return: numpy matrix
    """
    """
    CONTROLLA SE VALORI NULL INPUT SON DIVENTATI NON NULL (E VICEVERSA)
    PD.ISNA() RESTITUISCE TRUE SE è NULL, ELSE FALSE
    r: SE (1-0) = 1 -> IL NULL è STATO SOSTITUITO
       SE (0-1) = -1 -> DA NON NULL è PASSATO A NULL
       SE (0-0) O (1-1) = 0 -> NON CI SONO STATI CAMBIAMENTI
       
    NB: INPUT E OUTPUT DEVONO AVERE LE STESSE DIMENSIONI E DEVONO ESSERE ORDINATI PER
    RIGHE E COLONNE NELLO STESSO MODO
    """
    bool_i = pd.isna(input)
    bool_o = pd.isna(output)
    r = bool_i.values.astype(int) - bool_o.values.astype(int)
    return r

