import pandas as pd

# 1. Cargar la tabla de metadatos descargada del SRA Run Selector
df = pd.read_csv("SraRunTable.csv", sep=",")

# 2. Estandarizar los encabezados: renombrar la columna de muestra a 'ID'
df = df.rename(columns={'Sample Name': 'ID', 'Run': 'SRA_Accession'})

# Explorar qué variables clínicas existen en el dataset
print("Diagnósticos disponibles en el estudio:", df['disease_state'].unique())

# 3. Filtrar para quedarnos solo con casos de cáncer pancreático (PC) y controles
# (Ajusta los términos exactos según lo que imprimió el paso anterior)
fenotipos_interes = ['gastric cancer', 'gastritis']
datos_filtrados = df[df['disease_state'].isin(fenotipos_interes)]

# (Opcional) Filtrar por otros metadatos clínicos en los documentos, ej. estatus NAG
# datos_filtrados = datos_filtrados[datos_filtrados['clinical_status'] == 'NAG']

# 4. Exportar una lista limpia solo con los identificadores de SRA para descargar
datos_filtrados['SRA_Accession'].to_csv("lista_descarga_sra.txt", index=False, header=False)

# Guardar la tabla de metadatos limpia con la columna 'ID'
datos_filtrados.to_csv("metadata.csv", index=False)
