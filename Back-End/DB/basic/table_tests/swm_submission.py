from datetime import datetime

from objects.SWMSubmission import SWMSubmission

from table_tests.employee import get_employees
from table_tests.swm_type import get_swm_types

def create_swm_submissions(connection):
    con = connection
    cur = con.cursor()

    bh = list(filter(lambda e: e.get_first_name() == "Brian", get_employees(con)))[0].get_dbid()
    rd = list(filter(lambda e: e.get_first_name() == "Rodger", get_employees(con)))[0].get_dbid()

    swm_type = list(filter(lambda st: "Full" in st.get_type(), get_swm_types(con)))[0].get_dbid()

    swm_submission = SWMSubmission(
        swm_type,
        rd,
        bh,
        datetime.now().isoformat(" ")
    )

    query_parameters = (
        swm_submission.get_dbid(),
        swm_submission.get_type(),
        swm_submission.get_employee(),
        swm_submission.get_trainer(),
        swm_submission.get_manager(),
        swm_submission.get_submission_date()
    )

    cur.execute("INSERT INTO swm_submission(dbid, type, employee, trainer, manager, submission_date) VALUES (?,?,?,?,?,?);", query_parameters)
    con.commit()


def get_swm_submissions(connection):
    con = connection
    cur = con.cursor()

    cmd = cur.execute("SELECT type, employee, trainer, submission_date, manager, dbid FROM swm_submission;")
    res = cmd.fetchall()

    swm_submission_data = list(map(lambda ss: SWMSubmission(*ss), res))

    def generate_swm_submission(ss):
        ss.set_type(list(filter(lambda t: t.get_dbid() == ss.get_type(), get_swm_types(con)))[0])
        ss.set_employee(list(filter(lambda e: e.get_dbid() == ss.get_employee(), get_employees(con)))[0])
        ss.set_trainer(list(filter(lambda t: t.get_dbid() == ss.get_trainer(), get_employees(con)))[0])
        if ss.get_manager() is not None:
            ss.set_manager(list(filter(lambda t: t.get_dbid() == ss.get_manager(), get_employees(con)))[0])
        
        return ss

    swm_submissions = list(map(generate_swm_submission, swm_submission_data))

    return swm_submissions