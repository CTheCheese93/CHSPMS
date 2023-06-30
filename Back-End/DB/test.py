import sqlite3
import uuid

from datetime import datetime

def getUUID():
    return str(uuid.uuid4())

def create_work_statuses(connection):
    con = connection
    cur = con.cursor()

    work_statuses = [
        (getUUID(), "Active"),
        (getUUID(), "Terminated"),
        (getUUID(), "On Leave"),
        (getUUID(), "Fired")
    ]

    cur.executemany("INSERT INTO work_status(dbid, status) VALUES (?,?);", work_statuses)
    con.commit()

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
    
def get_employees(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT dbid, employee_id, first_name, last_name FROM employee;")
    res = cmd.fetchall()

    def generate_employee_data(result):
        return {
            "dbid": result[0],
            "employee_id": result[1],
            "first_name": result[2],
            "last_name": result[3]
        }

    def generate_employee(employee_data):
        return Employee(
            employee_data["dbid"],
            employee_data["employee_id"],
            employee_data["first_name"],
            employee_data["last_name"],
        )

    employee_data = map(generate_employee_data, res)

    return list(map(generate_employee, employee_data))

def create_employees(connection):
    con = connection
    cur = con.cursor()

    employees = [
        (
            getUUID(),
            "7872934",
            "Brian",
            "Hunter",
            "Colby",
            "2021-11-15",
            "2022-03-15"
        ),
        (
            getUUID(),
            "5753517",
            "Rodger",
            "Dodger",
            "Rabbi",
            "2021-11-12",
            "2022-03-15"
        )
    ]

    cur.executemany("""INSERT INTO employee(
        dbid, employee_id, first_name, last_name, preferred_name, first_hire_date, most_recent_hire_date
    ) VALUES (?,?,?,?,?,?,?);""", employees)
    con.commit()

def get_work_status(status, connection):
    cur = connection.cursor()
    cmd = cur.execute("SELECT dbid, status FROM work_status WHERE status=\"{}\";".format(status))
    res = cmd.fetchall()

    results = []

    for r in res:
        results.append({
            "dbid": r[0],
            "status": r[1]
        })
    
    return results

def get_work_statuses(connection):
    cur = connection.cursor()
    cmd = cur.execute("SELECT dbid, status FROM work_status;")
    res = cmd.fetchall()

    results = []

    for r in res:
        results.append({
            "dbid": r[0],
            "status": r[1]
        })
    
    return results

def get_basic_employees(connection):
    cur = connection.cursor()
    cmd = cur.execute("SELECT dbid, first_name, last_name FROM employee;")
    res = cmd.fetchall()

    results = []

    for r in res:
        results.append({
            "dbid": r[0],
            "first_name": r[1],
            "last_name": r[2]
        })

    return results

def get_employee_work_statuses(connection):
    con = connection
    cur = con.cursor()

    work_statuses = get_work_statuses(con)
    employees = get_basic_employees(con)

    cmd = cur.execute("SELECT employee, status FROM employee_work_status;")
    res = cmd.fetchall()

    results = []

    for r in res:
        results.append({
            "employee": list(filter(lambda e: e["dbid"] == r[0], employees))[0],
            "status": list(filter(lambda ws: ws["dbid"] == r[1], work_statuses))[0]
        })

    return results

def create_employee_work_statuses(connection):
    con = connection
    cur = con.cursor()

    work_statuses = get_work_statuses(con)

    active_work_status = list(filter(lambda ws: ws["status"] == "Active", work_statuses))[0]["dbid"]
    on_leave_work_status = list(filter(lambda ws: ws["status"] == "On Leave", work_statuses))[0]["dbid"]

    employees = get_employees(con)

    employee_work_statuses = [
        (employees[0]["dbid"], active_work_status),
        (employees[1]["dbid"], on_leave_work_status)
    ]

    cur.executemany("INSERT INTO employee_work_status(employee, status) VALUES (?,?);", employee_work_statuses)
    con.commit() 

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


def get_primary_departments(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT dbid, department_name FROM primary_department;")
    res = cmd.fetchall()

    primary_departments = list(map(lambda pd: PrimaryDepartment(pd[1], pd[0]), res))

    return primary_departments

def create_primary_departments(connection):
    con = connection
    cur = con.cursor()

    primary_departments = [
        PrimaryDepartment("Load"),
        PrimaryDepartment("Unload")
    ]

    query_parameters = []

    for pd in primary_departments:
        query_parameters.append((pd.get_dbid(), pd.get_name()))

    for qp in query_parameters:
        print("{}: {}".format(qp[1], qp[0]))

    cur.executemany("INSERT INTO primary_department(dbid, department_name) VALUES (?,?);", query_parameters)
    con.commit()

def get_secondary_departments(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT dbid, department_name, primary_department FROM secondary_department;")
    res = cmd.fetchall()

    return res

def create_secondary_departments(connection):
    con = connection
    cur = con.cursor()

    secondary_departments = {
        "PD1": SecondaryDepartment("PD1"),
        "Mezzanine": SecondaryDepartment("Mezzanine")
    }

    primary_departments = get_primary_departments(con)

    secondary_departments["PD1"].set_primary_department(
        list(filter(lambda pd: pd.get_name() == "Load", primary_departments))[0])
    
    secondary_departments["Mezzanine"].set_primary_department(
        list(filter(lambda pd: pd.get_name() == "Unload", primary_departments))[0])

    query_parameters = []

    for sd in secondary_departments.keys():
        fp = (
            secondary_departments[sd].get_dbid(),
            secondary_departments[sd].get_name(),
            secondary_departments[sd].get_primary_department().get_dbid()
        )
        query_parameters.append(fp)
    
    cur.executemany("INSERT INTO secondary_department(dbid, department_name, primary_department) VALUES (?, ?, ?);", query_parameters)
    con.commit()

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

def create_injuries(connection):
    con = connection
    cur = con.cursor()

    employees = get_employees(con)


def create_next_level_managers(connection):
    print("Need to crate.")

def create_swm_types(connection):
    print("Need to create.")

def create_swm_submissions(connection):
    print("Need to create.")


def main():
    con = sqlite3.connect("test_db")
    cur = con.cursor()

    # create_work_statuses(con)
    # res = cur.execute("SELECT * from work_status;")
    
    # create_employees(con)
    # res = cur.execute("SELECT * from employee;")

    # create_employee_work_statuses(con)
    # print(get_employee_work_statuses(con))

    # create_primary_departments(con)
    # for pd in get_primary_departments(con):
    #     print("{}: {}".format(pd.get_name(), pd.get_dbid()))

    # create_secondary_departments(con)
    # print(get_secondary_departments(con))

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

    # print(res.fetchall())
    con.close()

main()