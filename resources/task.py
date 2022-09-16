from models.task import TaskModel
from flask_restful import Resource, reqparse
from flasgger import swag_from
from utils import paginated_results, restrict
from flask import request

class Task(Resource):

    parser = reqparse.RequestParser() #manejador de peticiones de http
    parser.add_argument('id',type=int)
    parser.add_argument('descrip', type = str)
    parser.add_argument('status', type = str)
    
    @swag_from('../swagger/get_task.yaml')
    def get(self, id): # el objetivo es que si yo hago un id 1 con la tarea que me lo traiga
        tarea = TaskModel.find_by_id (id)
        if tarea:
            return tarea.json() #traeme el json que representa el id de mi tarea
        return {'Message': "No se encuentra la tarea"},404  #codigos de error
#definir el metodo para actualizar el registro
    @swag_from('../swagger/put_task.yaml')
    def put(self, id):
        tarea = TaskModel.find_by_id (id)
        print(tarea)
        if tarea:
            newdata = Task.parser.parse_args() 
            tarea.from_reqparse(newdata)
            tarea.save_to_db()
            return tarea.json()
##definir el metodo para eliminar el registro
    @swag_from('../swagger/delete_task.yaml')
    def delete(self, id):
        tarea = TaskModel.find_by_id (id)
        if tarea:
            tarea.delete_from_db()#metodo de sql
        return {'message': 'Se ha borrado la tarea'}

class  TaskList(Resource):
    @swag_from('../swagger/list_task.yaml')
    def get(self):
       query = TaskModel.query
       return paginated_results(query) #def post(self) #se suelen utilizar para crear los nuevos registros como los insert en db
    @swag_from('../swagger/post_task.yaml')
    def post(self):
        data = Task.parser.parse_args()

        tarea = TaskModel(**data)
        
        try:
            tarea.save_to_db() #guardar el nuevo registro en la base de datos
        except Exception as e:
            print(e)
            return {'message':'Ocurrio un error al crear la tarea'} , 500
        return tarea.json(), 201 #codigo 201 

#clase para las listas

class TaskSearch(Resource):
    @swag_from('../swagger/search_task.yaml')
    def post(self):
        query = TaskModel.query
        if request.json:
            filtros = request.json
            query = restrict(query, filtros, 'id', lambda x: TaskModel.id == x) #metodo de la logica para el filtro
            query = restrict(query, filtros, 'descrip', lambda x: TaskModel.descrip.contains(x))  #contains para filtrar de forma que no necesariamente la cadena sea exactamente como define la variable sino que pueda volver igual si no esta escritp de la misma mañera
            query = restrict(query, filtros, 'status', lambda x: TaskModel.status == x) 
         #logica de datos
        return paginated_results(query)

