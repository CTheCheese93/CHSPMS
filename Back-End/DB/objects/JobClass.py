from helpers.uuid_helpers import getUUID

class JobClass:
    def __init__(self, title, code=None, dbid=None):
        if dbid is None:
            self._dbid = getUUID()
        else:
            self._dbid = dbid
        
        self._title = title
        self._code = code
    
    def get_dbid(self):
        return self._dbid
    def get_title(self):
        return self._title
    def get_code(self):
        return self._code

    def set_dbid(self, new_dbid):
        self._dbid = new_dbid
    def set_title(self, new_title):
        self._title = new_title
    def set_code(self, new_code):
        self._code = new_code