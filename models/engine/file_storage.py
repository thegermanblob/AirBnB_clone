#!usr/bin/python3
""" module contains file storage class """

class FileStorage:
    """ class that determines the file storage """
    from models.base_model import BaseModel
    from models.amenity import Amenity
    from models.city import City
    from models.state import State
    from models.place import Place
    from models.review import Review
    from models.user import User
    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}

    __file_path = "file.json"
    __objects = dict()
    def __init__(self):
        """ Init method for the class """

    def all(self):
        """ returns dictionary """
        return self.__objects

    def new(self, obj):
        """ sets obj """
        self.__objects[obj.__class__.__name__ +"."+ obj.id] = obj

    def save(self):
        """ saves to json """
        import json
        cur_dic = {}
        with open(self.__file_path, 'w') as save_file:
            for key, val in self.__objects.items():
                cur_dic[key] = val.to_dict()
            json.dump(cur_dic, save_file)


    def reload(self):
        """ deserializes json to __objects """
        import json

        try:
            with open(self.__file_path) as save_file:
                json_file = json.load(save_file)
            for key in json_file:
                self.__objects[key] = self.classes[
                        json_file[key]["__class__"]](**json_file[key])
        except:
            pass

