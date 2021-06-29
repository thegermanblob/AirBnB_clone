#!/usr/bin/python3
""" Base model module contains the base class """


class BaseModel:
    """ defines all common attributes for other clases """

    def __init__(self, *args, **kwargs):
        import uuid
        from datetime import datetime
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    datestr = kwargs['created_at']
                    date = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date)
                elif key == "updated_at":
                    datestr = kwargs['updated_at']
                    date = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date)
                elif key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

    def save(self):
        """ makes the update_at the current time """
        from datetime import datetime
        now = datetime.now()
        self.updated_at = now

    def to_dict(self):
        """ returns dictionary """
        todict = self.__dict__.copy()
        todict["created_at"] = self.created_at.isoformat()
        todict["updated_at"] = self.updated_at.isoformat()
        todict["__class__"] = self.__class__.__name__
        return todict

    def __str__(self):
        """ returns string representation """
        name = self.__class__.__name__
        return "[{}]({}){}".format(name, self.id, self.__dict__)
