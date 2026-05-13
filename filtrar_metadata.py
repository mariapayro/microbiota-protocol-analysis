import pandas as pd

# 1. Cargar la tabla de metadatos (asegúrate de que el nombre del archivo sea el correcto)
df = pd.read_csv("SraRunTable.csv", sep=",")

# 2. Renombrar 'Run' a 'SRA_Accession' y usarlo también como 'ID'
# Si no hay 'Sample Name', el número de Run (SRR...) es el identificador más robusto.
df = df.rename(columns={'Run': 'SRA_Accession'})
df['ID'] = df['SRA_Accession']

# 3. Filtrado para el estudio de Cáncer Pancreático (PC)
# Según los metadatos que observaste, 'pc' representa los casos de páncreas.
datos_filtrados = df[df['type'].str.lower() == 'pc'].copy()

# Verificación de seguridad:
print(f"Total de muestras en el archivo original: {len(df)}")
print(f"Muestras filtradas de Cáncer Pancreático (PC): {len(datos_filtrados)}")

# 4. Exportar la lista de accesiones (SRR...) para el SRA Toolkit
# Este archivo lo usarás en la terminal con: prefetch --option-file lista_descarga_sra.txt
datos_filtrados['SRA_Accession'].to_csv("lista_descarga_SRA.txt", index=False, header=False)

# 5. Guardar la tabla de metadatos limpia para tu análisis estadístico
# Esta tabla ya tiene el filtro de 'pc' y la columna 'ID' estandarizada.
datos_filtrados.to_csv("metadata_PC_final.csv", index=False)
