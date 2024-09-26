FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el contenido de la carpeta actual (.) al directorio de trabajo (/app) en el contenedor
COPY . /app

# Instalar las dependencias especificadas
RUN pip install --no-cache-dir flask redis

# Exponer el puerto 5000 para el tráfico HTTP
EXPOSE 5000

# Comando predeterminado para ejecutar la aplicación
CMD ["python", "app.py"]