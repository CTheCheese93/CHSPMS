from helpers.uuid_helpers import getUUID

from table_tests.employee import get_employees
from table_tests.swm_type import get_swm_types

class SWMSubmission:
    def __init__(self, swm_type, employee, trainer,
    submission_date, manager=None, dbid=None):
        if dbid is None:
            self._dbid = getUUID()
        else:
            self._dbid = dbid

        self._type = swm_type
        self._employee = employee
        self._trainer = trainer
        self._submission_date = submission_date
        self._manager = manager

    def get_dbid(self):
        return self._dbid
    def get_type(self):
        return self._type
    def get_employee(self):
        return self._employee
    def get_trainer(self):
        return self._trainer
    def get_submission_date(self):
        return self._submission_date
    def get_manager(self):
        return self._manager

    def set_dbid(self, new_dbid):
        self._dbid = new_dbid
    def set_type(self, new_type):
        self._type = new_type
    def set_employee(self, new_employee):
        self._employee = new_employee
    def set_trainer(self, new_trainer):
        self._trainer = new_trainer
    def set_submission_date(self, new_submission_date):
        self._submission_date = new_submission_date
    def set_manager(self, new_manager):
        self._manager = new_manager