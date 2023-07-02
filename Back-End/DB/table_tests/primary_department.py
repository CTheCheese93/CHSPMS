from objects.PrimaryDepartment import PrimaryDepartment

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

    cur.executemany("INSERT INTO primary_department(dbid, department_name) VALUES (?,?);", query_parameters)
    con.commit()