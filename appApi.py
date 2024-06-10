from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import psycopg2, json

app = FastAPI()

db_params = {
    'dbname' : 'postgres',
    'user' : 'postgres',
    'password' : '1234',
    'host' : 'localhost',
    'port' : '5432'
}


conn = psycopg2.connect(**db_params)
print("Conexion exitosa")


class Movies(BaseModel):
    table_name: str
    id: int
    autor: str
    descripcion: str
    fechadeestreno: str



@app.get('/obtenerTodos')
def obtenerMovies():
    temporal_list = []

    with conn.cursor() as cursor:
        try:
            get_data_query = '''
            SELECT * FROM my_movies
        '''
            cursor.execute(get_data_query)

            rows = cursor.fetchall()

            for row in rows:
                print(row)
                temporal_list.append(row)
        except:
            print("Error con la consulta GET")

    return {"message": temporal_list}



@app.post('/crearPelicula')
def crearMovie(peli:Movies):

    with conn.cursor() as cursor:
        
        try:
            insert_data_query = f'''
            INSERT INTO {peli.table_name} (autor, descripcion, fechadeestreno) VALUES (%s, %s, %s);
            '''

            data_to_insert = (peli.autor, peli.descripcion, peli.fechadeestreno)
            cursor.execute(insert_data_query,data_to_insert )
            conn.commit()

        except Exception as e:
            print(e)
            print("Error con la consulta POST")

    return {"message": "Creado correctamente2"}

       


@app.put('/editarPelicula/{id}')
def editarMovie(peli:Movies):

    with conn.cursor() as cursor:
        
        try:

            actual_data_query = f'''
            UPDATE {peli.table_name} SET autor=%s, descripcion=%s, fechadeestreno=%s WHERE id=%s;
            '''

            data_to_actual = (peli.autor, peli.descripcion, peli.fechadeestreno, peli.id)
            cursor.execute(actual_data_query,data_to_actual )
            conn.commit()

        except Exception as e:
            print(e)
            print("Error con la consulta PUT")

    return {"message": "Actualizado correctamente"}



@app.delete('/eliminar/{id}')
def deleteMovie(peli:Movies):
     with conn.cursor() as cursor:
        print("ingreso a with")
        try:
            print("ingreso al trycatch")

            actual_data_query = f'''
            DELETE FROM {peli.table_name} WHERE id=%s;
            '''
            print("ingreso el query")
            cursor.execute(actual_data_query,(peli.id,))
            print("ejecuto el query")
            conn.commit()

        except Exception as e:
            print(e)
            print("Error con la consulta DELETE")

     return {"message": "Eliminado correctamente"}






# @app.delete('/eliminar/{id}')
# def deleteMovie(peli:Movies):
#     for movie_item in Movies:
#         if movie_item['id'] == peli.id:
#             Movies.remove(movie_item)
#             return {"message": "Task borrada correctamente"}
#         else:
#             return {"message": "Id no encontrado"}