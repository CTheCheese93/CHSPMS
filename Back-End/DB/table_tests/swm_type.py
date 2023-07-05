from objects.SWMType import SWMType

def create_swm_types(connection):
    con = connection
    cur = con.cursor()

    swm_types = [
        SWMType("Annual (Full)"),
        SWMType("Risk Based"),
        SWMType("Annual (Risk Based)")
    ]

    query_parameters = list(map(lambda st: (st.get_dbid(), st.get_type()), swm_types))

    cur.executemany("INSERT INTO swm_type(dbid, type) VALUES(?,?);", query_parameters)
    con.commit()

def get_swm_types(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT type, dbid FROM swm_type;")
    res = cmd.fetchall()

    swm_types = list(map(lambda st: SWMType(*st), res))

    return swm_types