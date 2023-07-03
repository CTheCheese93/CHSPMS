from table_tests.employee import get_employees

def create_next_level_managers(connection):
    con = connection
    cur = con.cursor()

    employees = get_employees(con)

    bh = list(filter(lambda e: e.get_first_name() == "Brian", employees))[0].get_dbid()
    rd = list(filter(lambda e: e.get_first_name() == "Rodger", employees))[0].get_dbid()

    query_parameters = [
        (rd, bh)
    ]

    cur.executemany("INSERT INTO next_level_manager(employee, manager) VALUES (?,?);", query_parameters)
    con.commit()
    

def get_next_level_managers(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT employee, manager FROM next_level_manager;")
    res = cmd.fetchall()

    employees = get_employees(con)

    def connect_next_level_manager(nlm):
        employee = list(filter(lambda e: e.get_dbid() == nlm[0], employees))[0]
        manager = list(filter(lambda e: e.get_dbid() == nlm[1], employees))[0]
        return { "employee": employee, "manager": manager }

    next_level_managers = list(map(connect_next_level_manager, res))

    return next_level_managers