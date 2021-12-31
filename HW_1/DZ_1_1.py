from abc import ABC, abstractmethod
import json
import pickle


class SerializationInterface(ABC):
    @abstractmethod
    def save_data(self, save_file):
        pass
    

class SaveJson(SerializationInterface):
    def save_data(self, data):
        with open('file.txt', 'rb') as file:
            json.dump(data, file)
    

class SaveBin(SerializationInterface):
    def save_data(self, data):
        with open('file.txt', 'rb') as file:
            pickle.dump(data, file)
            