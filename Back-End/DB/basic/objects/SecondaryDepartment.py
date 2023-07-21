import uuid

from helpers.uuid_helpers import getUUID

from objects.PrimaryDepartment import PrimaryDepartment

class SecondaryDepartment(PrimaryDepartment):
    def __init__(self, department_name, dbid=None, primary_department=None):
        if (dbid is None):
            super().__init__(department_name, getUUID())
        else:
            super().__init__(department_name, dbid)
        
        self._primary_department = primary_department
    
    def get_primary_department(self):
        return self._primary_department

    def set_primary_department(self, new_primary_department):
        self._primary_department = new_primary_department