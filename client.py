import requests
import json
from zeep.client import Client as CLI
from student import Estudiante

class Client():
    def __init__(self,endpoint='http://localhost:7000/ws/EstudianteWebServices?wsdl'):
        self.endpoint = endpoint
        self.cli = CLI(self.endpoint)
    
    def findAll(self):
        students = self.cli.service.getListaEstudiante()
        for stu in students:
            print(stu)

    def find(self,id):
        student = self.cli.service.getEstudiante(id)
        print(student)

    def delete(self,id):
        self.cli.service.borrarEstudiante(id)
        
    def insert(self,id,name,major):
        data = {'matricula': id, 'nombre': name, 'carrera': major}
        js = json.dumps(data)
        self.cli.service.crearEstudiante(json.loads(str(js)))
        

