from helpers.uuid_helpers import getUUID

class SWMType:
    def __init__(self, swm_type, dbid=None):
        if dbid is None:
            self._dbid = getUUID()
        else:
            self._dbid = dbid
        
        self._swm_type = swm_type
    
    def get_dbid(self):
        return self._dbid
    def get_type(self):
        return self._swm_type

    def set_dbid(self, new_dbid):
        self._dbid = new_dbid
    def set_type(self, new_swm_type):
        self._swm_type = new_swm_type