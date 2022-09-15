from db import db


class TaskModel(db.Model): #Definicion de una clase
    __tablename__ = 'task' #para identificar la tabla en la db

    id = db.Column(db.Integer, primary_key=True)
    descrip = db.Column(db.String)
    status =db.Column(db.String)

    def __init__(self, id, descrip, status): #definicion de un constructor para una clase. Self en el objeto, seria el THIS de java
        self.id = id
        self.descrip = descrip
        self.status = status
    
    def json (self,depth =0):
        json ={
            'id' : self.id,
            'descrip' : self.descrip,
            'status' :self.status
        }
        return json
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() # el filter by lo que hace es recibir un parametro

