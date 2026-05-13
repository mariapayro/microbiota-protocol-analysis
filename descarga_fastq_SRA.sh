# 1. Crear las carpetas destino (si no existen, las crea)
mkdir -p sra_PC
mkdir -p fastq_PC

# 2. Descargar los archivos comprimidos (.sra) directamente en la subcarpeta sra_PC
echo "Iniciando descarga de archivos .sra..."
# La bandera --output-directory fuerza la descarga a tu carpeta local en lugar del caché
prefetch --option-file lista_descarga_sra.txt --output-directory sra_PC

# 3. Extraer y convertir los .sra a .fastq y guardarlos en fastq_PC
echo "Iniciando conversión a FASTQ..."
while read -r SRR_ID; do
    # Limpiamos el texto para evitar errores si el .txt tiene formatos de salto de línea de Windows
    SRR_ID=$(echo "$SRR_ID" | tr -d '\r')
    
    # Evita líneas en blanco
    if [[ -n "$SRR_ID" ]]; then
        echo "Procesando $SRR_ID..."
        
        # Le indicamos a fasterq-dump la ruta donde prefetch guardó la carpeta de la muestra
        # prefetch crea una subcarpeta por cada ID (ej. sra_PC/SRR123456/SRR123456.sra)
        # fasterq-dump es lo suficientemente listo para procesarlo pasándole el directorio
        fasterq-dump "sra_PC/${SRR_ID}" --split-files --outdir fastq_PC
    fi
done < lista_descarga_sra.txt

echo "¡Proceso terminado! Tus archivos crudos (.sra) están seguros en ./sra_PC/ y tus FASTQ listos para el QC están en ./fastq_PC/"
