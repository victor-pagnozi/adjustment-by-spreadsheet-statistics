import pandas as pd
from fuzzywuzzy import fuzz, process

df = pd.read_excel('bairros.xlsx')
fixed_neighbors_sheet = pd.read_excel('bairros_corrigidos.xlsx')
fixed_neighbors = fixed_neighbors_sheet['BAIRROS_CORRETOS'].dropna().unique().tolist()

def fix_neighbor_name(name):
    name = str(name)
    better_correspondence, _ = process.extractOne(name, fixed_neighbors, scorer=fuzz.token_sort_ratio)
    return better_correspondence

df['Bairro Corrigido'] = df['BAIRRO'].apply(fix_neighbor_name)

df.to_excel('bairros_depara_corrigido.xlsx', index=False)
