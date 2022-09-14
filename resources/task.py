from models.task import TaskModel
from flask_restful import Resource, reqparse
from flasgger import swag_from

class Task(Resource):

    parser = reqparse.RequestParser() #manejador de peticiones de http
    parser.add_argument('id',type=int)
    parser.add_argument('description', type = str)
    
    @swag_from('../swagger/get_task.yaml')
    def get(self, id): # el objetivo es que si yo hago un id 1 con la tarea que me lo traiga
        tarea = TaskModel(1, "Hola Mundo") #objeto de prueba
        if tarea:
            return tarea.json() #traeme el json que representa el id de mi tarea
        return {'mensaje': "No se encuentra la tarea"},404  #codigos de error
        