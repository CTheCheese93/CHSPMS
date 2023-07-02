import sqlite3
from objects.Employee import Employee

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
        Employee(
            None,
            "7872934",
            "Brian",
            "Hunter",
            "Colby",
            "2021-11-15",
            "2022-03-15"
        ),
        Employee(
            None,
            "5753517",
            "Rodger",
            "Dodger",
            "Rabbi",
            "2021-11-12",
            "2022-03-15"
        )
    ]

    def get_query_parameters(employee):
        return (
                employee.get_dbid(),
                employee.get_employee_id(),
                employee.get_first_name(),
                employee.get_last_name(),
                employee.get_preferred_name(),
                employee.get_first_hire_date(),
                employee.get_most_recent_hire_date()
            )
            

    query_parameters = map(get_query_parameters, employees)

    cur.executemany("""INSERT INTO employee(
        dbid, employee_id, first_name, last_name, preferred_name, first_hire_date, most_recent_hire_date
    ) VALUES (?,?,?,?,?,?,?);""", query_parameters)
    con.commit()

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