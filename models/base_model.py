#!/usr/bin/python3
""" Base model module contains the base class """


class BaseModel:
    """ defines all common attributes for other clases """

    def __init__(self, *args, **kwargs):
        import uuid
        from datetime import datetime
        if kwargs is None:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now
        else:
            for key in kwargs:
                if key == "created_at":
                    datestr = kwargs['created_at']
                    date = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date)
                elif key == "updated_at":
                    datestr = kwargs['updated_at']
                    date = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date)
                else:
                    setattr(self, key, kwargs[key])

    def save(self):
        """ makes the update_at the current time """
        from datetime import datetime
        now = datetime.now()
        self.updated_at = str(now)

    def to_dict(self):
        """ returns dictionary """
        todict = self.__dict__
        todict['__class__'] = self.__class__
        todict['created_at'] = todict['created_at'].isoformat()
        todict['updated_at'] = todict['updated_at'].isoformat()
        return todict

    def __str__(self):
        """ returns string representation """
        return "[{}]({d}){}".format(self.__class__, self.id, self.__dict__)
