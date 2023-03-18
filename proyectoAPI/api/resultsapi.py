import pandas as pd
from sodapy import Socrata
import statistics
import numpy as np

def resultsModify(results):
    results['f_sforo_p_bray_ii_mg_kg'] = pd.to_numeric(results['f_sforo_p_bray_ii_mg_kg'], errors='coerce')
    results['f_sforo_p_bray_ii_mg_kg'] = results['f_sforo_p_bray_ii_mg_kg'].replace(np.nan, 3.87)
    medianaPH = results['ph_agua_suelo_2_5_1_0'].median()
    medianaP = results['f_sforo_p_bray_ii_mg_kg'].median()
    medianaK = results['potasio_k_intercambiable_cmol_kg'].median()
    # Selecciona las primeras 4 columnas y la primera fila utilizando el método .iloc[]
    slice_results = results.iloc[0, :3]
    # Muestra el slice del DataFrame resultante
    print(slice_results)
    # print(results.to_string(index=False))
    print("\nMEDIANA PH :" , medianaPH)
    print("\nMEDIANA POTASIO :" , medianaP)
    print("\nMEDIANA FÓSFORO :" , medianaK)

