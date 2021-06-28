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
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            print('hi')
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

    def save(self):
        """ makes the update_at the current time """
        from datetime import datetime
        now = datetime.now()
        self.updated_at = str(now)

    def to_dict(self):
        """ returns dictionary """
        from datetime import datetime
        todict = self.__dict__
        todict['__class__'] = self.__class__
        cdatestr = str(todict['created_at'])
        udatestr = str(todict['updated_at'])
        cdate = datetime.strptime(cdatestr, '%Y-%m-%d %H:%M:%S.%f')
        udate = datetime.strptime(udatestr, '%Y-%m-%d %H:%M:%S.%f')
        print(type(udate))
        todict['created_at'] = cdate.isoformat("T")
        todict['updated_at'] = udate.isoformat("T")
        return todict

    def __str__(self):
        """ returns string representation """
        return "[{}]({}){}".format(self.__class__, self.id, self.__dict__)
