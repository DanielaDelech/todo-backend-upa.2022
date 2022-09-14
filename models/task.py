class TaskModel (): #Definicion de una clase


    #definicion de los atributos de una clase
    id = int
    description = str

    def __init__(self, id, description): #definicion de un constructor para una clase. Self en el objeto, seria el THIS de java
        self.id = id
        self.description = description
    
    def json (self,depth =0):
        json ={
            'id' : self.id,
            'description' : self.description
        }
        return json
