# Descargar los archivos FASTQ usando la lista filtrada
prefetch --option-file lista_descarga_sra.txt
fasterq-dump --split-files --outdir ./datos_fastq/ $(cat lista_descarga_sra.txt)
