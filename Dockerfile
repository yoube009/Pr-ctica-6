Para la parte del Docker sería: 
# Paso 1: Usar la imagen Oficial de postgres de la pagina de Docker https://hub.docker.com/_/postgres

# Paso 2. Copiar e instalar la imagen desde la terminal para tener la imagen en el Docker Desktop

# Paso 3. Instalar dependecias
run pip install -r requirements.txt

# Paso 4: Crear y correr el contenedor en Docker con los siguientes datos:
Nombre del contenedor=my_collections
Puertos: 5432:5432
La contraseña es privada
docker run --name nombre -e POSTGRES_PASSWORD=secreto -p 5432:5432 -d postgres

