import requests

class Student(object):
    def get_by_id(self, id):
        return requests.get(url="http://192.168.0.113:8080/student/" + str(id))

    def get_all(self):
        return requests.get(url="http://192.168.0.113:8080/student")

    def save(self, json_data):
        return requests.post(url="http://192.168.0.113:8080/student", json=json_data)

    def update(self, json_data):
        return requests.put(url="http://192.168.0.113:8080/student", json=json_data)

    def delete(self, id):
        return requests.delete(url="http://192.168.0.113:8080/student/" + str(id))