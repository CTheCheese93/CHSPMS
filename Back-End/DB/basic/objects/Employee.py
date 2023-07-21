from helpers.uuid_helpers import getUUID

class Employee:
    def __init__(self, dbid=None, employee_id=None, first_name=None, last_name=None,
    preferred_name=None, first_hire_date=None, most_recent_hire_date=None):
        if dbid is None:
            self._dbid = getUUID()
        else:
            self._dbid = dbid
        
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._preferred_name = preferred_name
        self._first_hire_date = first_hire_date
        self._most_recent_hire_date = most_recent_hire_date
    
    def get_dbid(self):
        return self._dbid
    def get_employee_id(self):
        return self._employee_id
    def get_first_name(self):
        return self._first_name
    def get_last_name(self):
        return self._last_name
    def get_preferred_name(self):
        return self._preferred_name
    def get_first_hire_date(self):
        return self._first_hire_date
    def get_most_recent_hire_date(self):
        return self._most_recent_hire_date

    def set_dbid(self, new_dbid):
        self._dbid = new_dbid
    def set_employee_id(self, new_employee_id):
        self._employee_id = new_employee_id
    def set_first_name(self, new_first_name):
        self._first_name = new_first_name
    def set_last_name(self, new_last_name):
        self._last_name = new_last_name
    def set_preferred_name(self, new_preferred_name):
        self._preferred_name = new_preferred_name
    def set_first_hire_date(self, new_first_hire_date):
        self._first_hire_date = new_first_hire_date
    def set_most_recent_hire_date(self, new_most_recent_hire_date):
        self._most_recent_hire_date = new_most_recent_hire_date