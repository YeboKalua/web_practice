import uuid
import datetime
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.datetime.now()
    def to_dict(self):
        obj.__dict__[__class__] = self.__class__.__name__
        obj.__dict__[created_at] = datetime.now().isoformat()
        obj.__dict__[updated_at] = datetime.now().isoformat()
        return obj.__dict__
        