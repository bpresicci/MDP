from matplotlib import pyplot as plt
import numpy as np
from utils import read_excels
from utils import desired_df
from utils import find_unique_values_per_given_column
from utils import subdf_given_column_value
from utils import to_excel_iterative, draw_graph
from check_null import check_null_changes

# inserire il nome del file salvato localmente; input1 è l'input con i soli id presenti in output
# ottenuto tramite SQL query input.Id = output.Id
# è meglio di input perchè ha molte meno righe -> read_excels non legge righe inutili

input_name = 'input1_null_normalizzati.xlsx'
output_name = 'output1_null_normalizzati.xlsx'

df_input, df_output = read_excels(input_name, output_name)


# definizione delle colonne che vogliamo analizzare
columns_of_interest = ['Id', 'Title', 'OriginalTitle', 'Year', 'Duration', 'Actors', 'Directors', 'Genres', 'AgeRating', 'Country', 'Distributor', 'ProducerName', 'ContentCategory', 'ContentType']
column = 'ContentType'
name = 'null_changes'
# desired_df RESTITUISCE DUE DATAFRAME CHE ABBIANO LE STESSE COLONNE NELLO STESSO ORDINE

df_i, df_o = desired_df(df_input, df_output, columns_of_interest)

# VALORI DI CONTENTTYPE


values_ContentType = find_unique_values_per_given_column(df_i, column)

# UN GRAFICO PER CONTENTTYPE

for value in values_ContentType:
    dfi, dfo = subdf_given_column_value(df_i, df_o, column, value)
    null_changes = check_null_changes(dfi, dfo)
    to_excel_iterative(null_changes, name, value, columns_of_interest)
    draw_graph(null_changes, name, value, columns_of_interest)
# null_changes è UNA MATRICE NUMPY DELLE STESSE DIMENSIONI DI df_i E df_o CHE CONTIENE 1, 0, -1
# SE: L'ELEMENTO IN QUELLA POSIZIONE (eg.  null_changes[0][0]) è 1 ALLORA
# IN INPUT ERA NULL ED IN OUTPUT è NON NULL; SE 0 ALLORA ERANO ENTRAMBI NULL O ENTRAMBI NON NULL;
# SE -1 IN INPUT ERA NON NULL ED IN OUTPUT ERA NULL
"""
null_changes = check_null_changes(df_i, df_o)
#df = pd.DataFrame(null_changes)
#df.to_excel('null_changes.xlsx')
# CREA UN GRAFICO A BARRE CHE MOSTRA PER OGNI COLONNA QUANTE RIGHE (CIRCA!!) SON PASSATE DA NULL A NON NULL
# DICO CIRCA PERCHè FA SOLO UNA SOMMA DEI VALORI DI TUTTE LE RIGHE PER CIASCUNA COLONNA, QUINDI
# NON SAPPIAMO CON ASSOLUTA PRECISIONE QUANTI +1 CI SONO E QUANTI -1, MA SAPPIAMO SOLO IN GENERALE
# SE L'ALGORITMO TENDE A RIEMPIRE I NULL O NO

#print(df_i.iloc[32:42, :4])
#print(df_o.iloc[32:42, :4])

plt.bar(np.arange(null_changes.shape[1]), np.sum(null_changes, axis = 0), tick_label = columns_of_interest)
plt.xticks(rotation = 45)
plt.savefig('null_changes.png', bbox_inches='tight')
"""

