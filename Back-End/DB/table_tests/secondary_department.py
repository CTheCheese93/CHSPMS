from objects.SecondaryDepartment import SecondaryDepartment

from table_tests.primary_department import get_primary_departments

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