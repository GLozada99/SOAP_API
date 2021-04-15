import requests

class Client():
    def __init__(self,endpoint='http://localhost:7000/api/estudiante/'):
        self.endpoint = endpoint
        self.params = dict()
    
    def findAll(self):
        req = requests.get(url = self.endpoint, params = self.params)
        data = req.json()
        print(data)
        pass

    def find(self,id):
        req = requests.get(url = self.endpoint+'/'+id, params = self.params)
        data = req.json()
        print(data)
        pass

    def delete(self,id):
        pass

    def insert(self,id,name,major):
        pass

