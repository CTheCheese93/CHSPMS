import uuid

from helpers.uuid_helpers import getUUID
    
class PrimaryDepartment:
    def __init__(self, department_name, dbid=None):
        self._name = department_name
        if (dbid is None):
            self._dbid = getUUID()
        else:
            self._dbid = dbid

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_dbid(self):
        if (self._dbid):
            return self._dbid
        else:
            return False

    def set_dbid(self, dbid):
        self._dbid = dbid