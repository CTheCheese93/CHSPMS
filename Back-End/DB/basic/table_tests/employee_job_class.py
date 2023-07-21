from table_tests.employee import get_employees
from table_tests.job_class import get_job_classes

def create_employee_job_classes(connection):
    con = connection
    cur = con.cursor()

    employees = get_employees(con)
    job_classes = get_job_classes(con)

    bh = list(filter(lambda e: e.get_first_name() == "Brian", employees))[0].get_dbid()
    rd = list(filter(lambda e: e.get_first_name() == "Rodger", employees))[0].get_dbid()

    hr = list(filter(lambda jc: jc.get_title() == "Hourly", job_classes))[0].get_dbid()
    sup = list(filter(lambda jc: jc.get_title() == "Supervisor", job_classes))[0].get_dbid()

    query_parameters = [
        (bh, sup),
        (rd, hr)
    ]

    cur.executemany("INSERT INTO employee_job_class(employee, job_class) VALUES (?,?);", query_parameters)
    con.commit()
    

def get_employee_job_classes(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT job_class, employee FROM employee_job_class;")
    res = cmd.fetchall()

    employees = get_employees(con)
    job_classes = get_job_classes(con)

    def connect_employee_job_class(ejc):
        employee = list(filter(lambda e: e.get_dbid() == ejc[1], employees))[0]
        job_class = list(filter(lambda jc: jc.get_dbid() == ejc[0], job_classes))[0]
        return { "employee": employee, "job_class": job_class }

    employee_job_classes = list(map(connect_employee_job_class, res))

    return employee_job_classes