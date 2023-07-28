from DB.orm.objects.Employee import Employee
from DB.orm.objects.Injury import Injury
from DB.orm.objects.JobClass import JobClass
from DB.orm.objects.PrimaryDepartment import PrimaryDepartment
from DB.orm.objects.SecondaryDepartment import SecondaryDepartment
from DB.orm.objects.WorkStatus import WorkStatus
from DB.orm.objects.Base import Base

from DB.orm.db_session import engine, db_session as session


def build_up():
    Base.metadata.create_all(bind=engine)

    mngr = JobClass(title="Manager", code="M")
    sup = JobClass(title="Supervisor", code="S")
    hrly = JobClass(title="Hourly", code="H")

    active = WorkStatus(status="Active")
    terminated = WorkStatus(status="Terminated")

    inbound = PrimaryDepartment(name="Inbound")
    outbound = PrimaryDepartment(name="Outbound")

    colby = Employee(first_name="Colby", last_name="Hunter")
    brandon = Employee(first_name="Brandon", last_name="Rivera")
    ronald = Employee(first_name="Ronald", last_name="Venegas")

    session.add_all([
        colby, brandon, mngr, ronald,
        sup, hrly, inbound,
        outbound, active, terminated
    ])

    session.flush()

    pd1 = SecondaryDepartment(name="PD1", primary_department_id=outbound.id)
    pd2 = SecondaryDepartment(name="PD1", primary_department_id=outbound.id)

    unload = SecondaryDepartment(name="Unload", primary_department_id=inbound.id)
    metros = SecondaryDepartment(name="Metros", primary_department_id=inbound.id)

    colby.work_status_id = active.id
    brandon.work_status_id = active.id
    ronald.work_status_id = terminated.id

    colby.manager_id = brandon.id
    colby.job_class_id = sup.id
    brandon.job_class_id = mngr.id
    session.expire(colby, ['manager', 'job_class', 'work_status'])
    session.expire(brandon, ['employees', 'job_class', 'work_status'])
    session.expire(ronald, ['work_status'])

    injury = Injury(employee_dbid=colby.id, manager_dbid=colby.manager_id)

    session.add_all([injury, pd1, pd2, unload, metros])

    session.flush()

    session.commit()