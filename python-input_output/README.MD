cat > README.md << 'EOF'
# Python - Input/Output

Este proyecto aborda cómo manejar archivos en Python y cómo utilizar los conceptos de entrada/salida. A través de varias tareas, se exploran temas como lectura de archivos, escritura, serialización con JSON, deserialización, y el uso de argumentos desde la línea de comandos.

## 📄 1-write_file.py

### Descripción
Este script define una función `write_file` que escribe una cadena de texto en un archivo de texto codificado en UTF-8. Si el archivo no existe, lo crea; si ya existe, sobrescribe su contenido.

### Prototipo de la función
```python
def write_file(filename="", text=""):

