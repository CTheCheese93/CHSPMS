import sqlite3

from table_tests.work_status import get_work_statuses
from table_tests.employee import get_employees

def get_employee_work_statuses(connection):
    con = connection
    cur = con.cursor()

    work_statuses = get_work_statuses(con)
    employees = get_employees(con)

    cmd = cur.execute("SELECT employee, status FROM employee_work_status;")
    res = cmd.fetchall()

    results = []

    for r in res:
        results.append({
            "employee": list(filter(lambda e: e.get_dbid() == r[0], employees))[0],
            "status": list(filter(lambda ws: ws.get_dbid() == r[1], work_statuses))[0]
        })

    return results

def create_employee_work_statuses(connection):
    con = connection
    cur = con.cursor()

    work_statuses = get_work_statuses(con)
    employees = get_employees(con)

    active_work_status = list(filter(lambda ws: ws.get_status() == "Active", work_statuses))[0].get_dbid()
    on_leave_work_status = list(filter(lambda ws: ws.get_status() == "On Leave", work_statuses))[0].get_dbid()

    bh = list(filter(lambda e: e.get_first_name() == "Brian", employees))[0].get_dbid()
    rd = list(filter(lambda e: e.get_first_name() == "Rodger", employees))[0].get_dbid()

    employee_work_statuses = [
        (bh, active_work_status),
        (rd, on_leave_work_status)
    ]

    cur.executemany("INSERT INTO employee_work_status(employee, status) VALUES (?,?);", employee_work_statuses)
    con.commit() 