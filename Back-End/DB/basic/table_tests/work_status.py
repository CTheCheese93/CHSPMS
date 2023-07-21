from objects.WorkStatus import WorkStatus

def create_work_statuses(connection):
    con = connection
    cur = con.cursor()

    work_statuses = [
        WorkStatus("Active"),
        WorkStatus("Terminated"),
        WorkStatus("On Leave"),
        WorkStatus("Fired")
    ]

    def get_query_parameters(work_status):
        return (work_status.get_dbid(), work_status.get_status())

    query_parameters = map(get_query_parameters, work_statuses)

    cur.executemany("INSERT INTO work_status(dbid, status) VALUES (?,?);", query_parameters)
    con.commit()

def get_work_status(status, connection):
    cur = connection.cursor()
    cmd = cur.execute("SELECT dbid, status FROM work_status WHERE status=?;", status)
    res = cmd.fetchall()

    work_status = map(lambda ws: WorkStatus(ws[1], ws[0]), res)
    
    return list(work_status)

def get_work_statuses(connection):
    cur = connection.cursor()
    cmd = cur.execute("SELECT dbid, status FROM work_status;")
    res = cmd.fetchall()

    work_statuses = map(lambda ws: WorkStatus(ws[1], ws[0]), res)
    
    return list(work_statuses)