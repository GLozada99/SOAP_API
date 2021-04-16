import requests
import json
from suds.client import Client as CLI

class Client():
    def __init__(self,endpoint='http://localhost:7000/ws/EstudianteWebServices?wsdl'):
        self.endpoint = endpoint
        self.cli = CLI(self.endpoint)
    
    def findAll(self):
        req = requests.get(url = self.endpoint)
        data = req.json()
        for j in data:
            print(j)

    def find(self,id):
        req = requests.get(url = self.endpoint+id)
        data = req.text
        print(data)

    def delete(self,id):
        req = requests.delete(url = self.endpoint+id)
        
    def insert(self,id,name,major):
        data = {'matricula': id, 'nombre': name, 'carrera': major}
        js = json.dumps(data)
        req = requests.post(url = self.endpoint, data = js)
        

