from objects.JobClass import JobClass

def get_job_classes(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT title, code, dbid FROM job_class;")
    res = cmd.fetchall()

    job_classes = list(map(lambda jc: JobClass(*jc), res))

    return job_classes

def create_job_classes(connection):
    con = connection
    cur = con.cursor()

    job_classes = [
        JobClass("Hourly", "H02"),
        JobClass("Supervisor", "S01")
    ]

    def get_query_parameters(job_class):
        return (job_class.get_dbid(), job_class.get_title(), job_class.get_code())

    query_parameters = list(map(get_query_parameters, job_classes))

    cur.executemany("INSERT INTO job_class(dbid, title, code) VALUES (?,?,?)", query_parameters)
    con.commit()