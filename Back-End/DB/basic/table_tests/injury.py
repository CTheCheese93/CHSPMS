from datetime import datetime

from objects.Injury import Injury
from table_tests.employee import get_employees

def get_injuries(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT dbid, employee, manager, injury_date FROM injury;")
    res = cmd.fetchall()

    employees = get_employees(con)

    injuries = list(map(lambda i: Injury(
        dbid=i[0],
        employee=list(filter(lambda e: e.get_dbid() == i[1],employees))[0],
        manager=list(filter(lambda e: e.get_dbid() == i[2],employees))[0],
        injury_date=i[3]
    ), res))

    return injuries

def create_injuries(connection):
    con = connection
    cur = con.cursor()

    employees = get_employees(con)

    bh = list(filter(lambda e: e.get_first_name() == "Brian", employees))[0].get_dbid()
    rd = list(filter(lambda e: e.get_first_name() == "Rodger", employees))[0].get_dbid()

    injury = Injury(
        dbid=None,
        employee=rd,
        manager=bh,
        injury_date=datetime.now().isoformat(" ")
    )

    cur.execute("INSERT INTO injury(dbid, employee, manager, injury_date) VALUES(?,?,?,?);",[
        injury.get_dbid(),
        injury.get_employee(),
        injury.get_manager(),
        injury.get_injury_date()
    ])
    con.commit()