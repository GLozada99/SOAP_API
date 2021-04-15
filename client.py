import requests

class Client():
    def __init__(self,endpoint='http://localhost:7000/api/estudiante/'):
        self.endpoint = endpoint
        self.params = dict()
    
    def findAll(self):
        req = requests.get(url = self.endpoint)
        data = req.json()
        print(data)

    def find(self,id):
        req = requests.get(url = self.endpoint+'/'+id)
        data = req.json()
        print(data)

    def delete(self,id):
        req = requests.delete(url = self.endpoint, data = {'matricula': id})
        

    def insert(self,id,name,major):
        data = {'matricula': id, 'nombre': name, 'carrera': major}
        req = requests.post(url = self.endpoint, data = data)
        

