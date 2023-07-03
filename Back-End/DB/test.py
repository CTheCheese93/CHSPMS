from datetime import datetime
import sqlite3

from table_tests.employee_work_status import create_employee_work_statuses, get_employee_work_statuses
from table_tests.primary_department import create_primary_departments, get_primary_departments
from table_tests.secondary_department import create_secondary_departments, get_secondary_departments
from table_tests.work_status import create_work_statuses, get_work_statuses
from table_tests.employee import create_employees, get_employees
from table_tests.injury import create_injuries, get_injuries
from table_tests.job_class import create_job_classes, get_job_classes
from table_tests.employee_job_class import create_employee_job_classes, get_employee_job_classes
from table_tests.next_level_manager import create_next_level_managers, get_next_level_managers

stores = {
    "Employee": [],
    "Work Status": [],
    "Primary Department": [],
    "Secondary Department": []
}

def create_ready_data(connection):
    con = connection

    created = lambda s: print("{} Created".format(s))

    create_work_statuses(con)
    created("Work Status")
    create_employees(con)
    created("Employees")
    create_employee_work_statuses(con)
    created("Employee Work Statuses")
    create_primary_departments(con)
    created("Primary Departments")
    create_secondary_departments(con)
    created("Secondary Departments")
    create_injuries(con)
    created("Injuries")
    create_job_classes(con)
    created("Job Classes")
    create_employee_job_classes(con)
    created("Employee Job Classes")

def display_ready_data(connection):
    con = connection

    def title_bar(title):
        print("\n\n############### {} ###############\n\n".format(title))

    title_bar("Work Status")
    for work_status in get_work_statuses(con):
        print("\n\
            dbid: {}\n\
            Status: {}".format(
                work_status.get_dbid(),
                work_status.get_status()
            ))
    
    title_bar("Employee")
    for emp in get_employees(con):
        print("\n\
            dbid: {}\n\
            Employee ID: {}\n\
            First Name: {}\n\
            Last Name: {}\n".format(
                emp.get_dbid(),
                emp.get_employee_id(),
                emp.get_first_name(),
                emp.get_last_name()
            ))
    
    title_bar("Employee Work Status")
    for ews in get_employee_work_statuses(con):
        print("{}: {}".format(ews["employee"].get_first_name(), ews["status"].get_status()))

    title_bar("Primary Department")
    for pd in get_primary_departments(con):
        print("{}: {}".format(pd.get_name(), pd.get_dbid()))
    
    title_bar("Secondary Department")
    print(get_secondary_departments(con))

    title_bar("Injury")
    for i in get_injuries(con):
        print("""
        Employee: {}
        Manager: {}
        Injury Date: {}
        """.format(i.get_employee().get_first_name(), i.get_manager().get_first_name(), i.get_injury_date()))
    
    title_bar("Job Class")
    for jc in get_job_classes(con):
        print("dbid: {}\ntitle: {}\ncode: {}\n".format(
            jc.get_dbid(), jc.get_title(), jc.get_code()
        ))

    title_bar("Employee Job Class")
    for ejc in get_employee_job_classes(con):
        print("\nEmployee: {}\nJob Class: {}\n".format(
            ejc["employee"].get_first_name(),
            ejc["job_class"].get_title()
        ))

    title_bar("Next Level Manager")

def main():
    con = sqlite3.connect("test_db")
    cur = con.cursor()

    # create_ready_data(con)
    # display_ready_data(con)

    # create_next_level_managers(con)
    for nlm in get_next_level_managers(con):
        print("\nEmployee: {}\nManager: {}\n".format(
            nlm["employee"].get_first_name(),
            nlm["manager"].get_first_name()
        ))

    con.close()

main()