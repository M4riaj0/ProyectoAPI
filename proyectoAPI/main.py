import api.fileapi
import ui.fileui
import api.resultsapi

# print(results_df.to_string(index=False))

limite = ui.fileui.pedirNumRegistros()
departamento = ui.fileui.pedirDepartamento()
municipio = ui.fileui.pedirMunicipio()
cultivo = ui.fileui.pedirCultivo()
columnas = ["departamento", "municipio", "cultivo" , "ph_agua_suelo_2_5_1_0" , "f_sforo_p_bray_ii_mg_kg" , "potasio_k_intercambiable_cmol_kg"]

results_df = api.fileapi.consultaEspecifica(limite, departamento, municipio, cultivo, columnas)
api.resultsapi.resultsModify(results_df)
