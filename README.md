# microbiota-protocol-analysis
Scripts para llevar a cabo el análisis de microbiota con el pipeline del Dr Roberto para revista STAR Protocols.

Se debe comenzar descargando el archivo de metadatos del dataset de interés desde **SRA-NCBI** (.csv). De igual manera, se debe instalar la libreria **SRA toolkit** para poder descargar los FastQ del NCBI. 

1. Descargar versión desde el github (en este caso fue la versión de MacOS): 

`https://github.com/ncbi/sra-tools/wiki/02.-Installing-SRA-Toolkit` 

2. Descomprimir archivo descargado:

`tar -vxzf sratoolkit.current-mac64.tar.gz`

3. Exportar al PATH:

`export PATH=/Users/mpg/Downloads/sratoolkit.3.4.1-mac-x86_64/bin:$PATH`

4. En mi caso, corrí:

`xattr -dr com.apple.quarantine /Users/mpg/Downloads/sratoolkit.3.4.1-mac-x86_64/`

5. Para agregarlo al PATH global, no solo que esté activo en la terminal actual:

`sudo sh -c 'echo "export PATH=/Users/mpg/Downloads/sratoolkit.3.4.1-mac-x86_64/bin:\$PATH" >> /Users/mpg/.zshrc'

source ~/.zshrc`

6. Correr script `filtrar_metadata.py`

7. Correr script `descarga_fastq_SRA.sh`
El script primero descarga los archivos comprimidos en .sra colocándolos en subcarpeta 'sra' y después extrae y convierte los .sra a .fastq, dándonos los archivos FastQ (estos pueden llegar a pesar varios GB).
