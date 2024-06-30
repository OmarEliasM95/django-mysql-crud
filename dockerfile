# Usa la imagen oficial de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt /code/

# Instala las dependencias del proyecto incluyendo mysqlclient y mysql-connector-python
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev build-essential \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia todo el contenido actual al directorio /code en el contenedor
COPY . /code/

# Comando por defecto para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
