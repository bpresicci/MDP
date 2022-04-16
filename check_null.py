import pandas as pd

def check_null_changes(input, output):
    """
    :param input: dataframe
    :param output: dataframe
    :return: numpy matrix of integers, with possible values 1, 0, -1
    """
    """
    CONTROLLA SE VALORI NULL INPUT SON DIVENTATI NON NULL (E VICEVERSA)
    PD.ISNA() RESTITUISCE TRUE SE è NULL, ELSE FALSE
    r: SE (1-0) = 1 -> IL NULL è STATO SOSTITUITO
       SE (0-1) = -1 -> DA NON NULL è PASSATO A NULL
       SE (0-0) O (1-1) = 0 -> NON CI SONO STATI CAMBIAMENTI
       
    LA MATRICE r RISULTANTE SARà DELLE STESSE DIMENSIONI DI BOOL_I E BOOL_O E OGNI SUO ELEMENTO
    CONTERRà LA DIFFERENZA FRA L'ELEMENTO NELLA STESSA POSIZIONE DELL'INPUT - L'ELEMENTO
    NELLA STESSA POSIZIONE DELL'OUTPUT: SE +1 L'ALGORITMO HA FUNZIONATO, SE -1 è UN 
    PROBLEMA (PERDITA DI DATI), SE 0 NON CI SON STATE Nè RICONCILIAZIONE Nè PERDITA DI DATI
       
    NB: INPUT E OUTPUT DEVONO AVERE LE STESSE DIMENSIONI E DEVONO ESSERE ORDINATI PER
    RIGHE E COLONNE NELLO STESSO MODO
    """
    bool_i = pd.isna(input)
    bool_o = pd.isna(output)
    #df = pd.DataFrame(bool_i)
    #df.to_excel('bool_i.xlsx')
    #df = pd.DataFrame(bool_o)
    #df.to_excel('bool_o.xlsx')
    r = bool_i.values.astype(int) - bool_o.values.astype(int)

    # il metodo values restituisce un np.array del dataframe, che sarebbe di booleani, quindi converto in int
    # per poter fare la differenza tra gli elementi

    return r

