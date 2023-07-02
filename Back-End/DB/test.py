from datetime import datetime
import sqlite3

from table_tests.employee_work_status import create_employee_work_statuses, get_employee_work_statuses
from table_tests.primary_department import create_primary_departments, get_primary_departments
from table_tests.secondary_department import create_secondary_departments, get_secondary_departments
from table_tests.work_status import create_work_statuses, get_work_statuses
from table_tests.employee import create_employees, get_employees

stores = {
    "Employee": [],
    "Work Status": [],
    "Primary Department": [],
    "Secondary Department": []
}
def create_next_level_managers(connection):
    print("Need to create.")

def create_swm_types(connection):
    print("Need to create.")

def create_swm_submissions(connection):
    print("Need to create.")


def main():
    con = sqlite3.connect("test_db")
    cur = con.cursor()

    ################ WORKS ##########################

    # create_work_statuses(con)
    # for work_status in get_work_statuses(con):
    #     print("\n\
    #         dbid: {}\n\
    #         Status: {}".format(
    #             work_status.get_dbid(),
    #             work_status.get_status()
    #         ))
    
    # create_employees(con)
    # for emp in get_employees(con):
    #     print("\n\
    #         dbid: {}\n\
    #         Employee ID: {}\n\
    #         First Name: {}\n\
    #         Last Name: {}\n".format(
    #             emp.get_dbid(),
    #             emp.get_employee_id(),
    #             emp.get_first_name(),
    #             emp.get_last_name()
    #         ))

    # create_employee_work_statuses(con)
    # for ews in get_employee_work_statuses(con):
    #     print("{}: {}".format(ews["employee"].get_first_name(), ews["status"].get_status()))

    # create_primary_departments(con)
    # for pd in get_primary_departments(con):
    #     print("{}: {}".format(pd.get_name(), pd.get_dbid()))

    # create_secondary_departments(con)
    # print(get_secondary_departments(con))

    ################# WORKING ON IT #####################



    # print(res.fetchall())
    con.close()

main()