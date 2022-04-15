from matplotlib import pyplot as plt
import numpy as np
from utils import convert_to_str
from utils import read_excels
from utils import extract_desired_subset
from check_null import check_null_changes

# inserire il nome del file salvato localmente

input_name = 'input.xlsx'
output_name = 'output.xlsx'

df_input, df_output = read_excels(input_name, output_name)

#conversione a stringhe per semplicità (evitare TypeError)
#input_str, output_str = convert_to_str(df_input, df_output)

# definizione delle colonne che vogliamo analizzare
columns_of_interest = ['Id', 'Title', 'OriginalTitle', 'Year', 'Duration', 'Actors', 'Directors', 'Genres', 'AgeRating', 'Country', 'Distributor', 'ProducerName', 'ContentCategory']

df_i, df_o = extract_desired_subset(df_input, df_output, columns_of_interest)
null_changes = check_null_changes(df_i, df_o)

plt.bar(np.arange(null_changes.shape[1]), np.sum(null_changes, axis = 0), tick_label = columns_of_interest)
plt.xticks(rotation = 45)
plt.savefig('null_changes.png', bbox_inches='tight')


