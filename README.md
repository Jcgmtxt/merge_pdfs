# Combinador de PDFs con encabezados

Este script fue creado para resolver una necesidad puntual en mi trabajo: combinar múltiples archivos PDF agregando un encabezado a cada uno para diferenciarlos. Tal vez esto también pueda ser útil para algún compañero en el futuro.

## ¿Qué hace este script?
El script:
1. Busca todos los archivos PDF en la carpeta `./pdfs`.
2. Ordena los archivos numéricamente si el nombre contiene números.
3. Agrega un encabezado a cada archivo en el formato `Audio X`, donde `X` es el número de orden del archivo.
4. Une todos los PDFs en un único archivo llamado `audios_combinados.pdf`.

## Requisitos
Este script utiliza las siguientes bibliotecas de Python:
- `PyPDF2`
- `reportlab`

Puedes instalarlas con:
```sh
pip install PyPDF2 reportlab
```

## Cómo usarlo
1. Coloca los archivos PDF en la carpeta `./pdfs`.
2. Ejecuta el script:
   ```sh
   python script.py
   ```
3. Se generará un nuevo archivo `audios_combinados.pdf` con los PDFs combinados y sus respectivos encabezados.

## Notas
- Los archivos se ordenan numéricamente si contienen números en el nombre, de lo contrario, se mantienen en el orden predeterminado del sistema operativo.
- El encabezado se coloca en la parte superior de cada PDF antes de combinarse.
- Puedes cambiar la carpeta de entrada y el nombre del archivo de salida modificando las variables `pdf_folder` y `output_file` en el script.

Espero que esto sea útil en algún momento. ¡Buena suerte!

