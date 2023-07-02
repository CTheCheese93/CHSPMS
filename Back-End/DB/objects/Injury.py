import uuid

from helpers.uuid_helpers import getUUID

class Injury:
    def __init__(self, dbid=None, employee=None, injury_date=None, manager=None):
        if dbid is None:
            self._dbid = getUUID()
        else:
            self._dbid = dbid
        self._employee = employee
        self._injury_date = injury_date
        self._manager = manager

    def get_dbid(self):
        return self._dbid
    
    def set_dbid(self, new_dbid):
        self._dbid = new_dbid
    
    def get_employee(self):
        return self._employee
    
    def set_employee(self, new_employee):
        self._employee = new_employee
    
    def get_injury_date(self):
        return self._injury_date

    def set_injury_date(self, new_injury_date):
        self._injury_date = new_injury_date
    
    def get_manager(self):
        return self._manager

    def set_manager(self, new_manager):
        self._manager = new_manager