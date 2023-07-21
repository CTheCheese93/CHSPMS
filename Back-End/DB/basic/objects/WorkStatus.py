from helpers.uuid_helpers import getUUID

class WorkStatus:
    def __init__(self, status, dbid=None):
        if dbid is None:
            self._dbid = getUUID()
        else:
            self._dbid = dbid

        self._status = status
    
    def get_dbid(self):
        return self._dbid
    def get_status(self):
        return self._status

    def set_dbid(self, new_dbid):
        self._dbid = new_dbid
    def set_status(self, new_status):
        self._status = new_status