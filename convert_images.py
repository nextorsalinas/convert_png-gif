import os
from PIL import Image

def convert_images(directory):
    for filename in os.listdir(directory):  # Itera sobre todos los archivos en el directorio 
        if filename.endswith('.png'):   # Verifica si el archivo tiene la extensión .png
            filepath = os.path.join(directory, filename) # Crea la ruta completa del archivo
            img = Image.open(filepath)     # Abre la imagen PNG usando PIL (Pillow)
            new_filename = filename.replace('.png', '.gif')  # Crea el nuevo nombre de archivo con extensión .gif
            new_filepath = os.path.join(directory, new_filename)  # Crea la ruta completa para el nuevo archivo GIF
            img.save(new_filepath, 'GIF')     # Guarda la imagen como GIF
            os.remove(filepath)  # Eliminar el archivo PNG original
            print(f'Converted and removed: {filename} -> {new_filename}')  # Imprimir un mensaje indicando que la conversión se realizó

if __name__ == "__main__":
    directory = r'C:\Users\nsalinas\Documents\numeros'   # Especifica el directorio que contiene las imágenes PNG (Reemplaza con la ruta a tu directorio)
    convert_images(directory)   # Llama a la función para convertir las imágenes


#  ejecuta en la terminal el scrip:  python rename_files.py

