from sqlalchemy import create_engine, insert, select
from sqlalchemy.orm import Session

from objects.Base import Base
from objects.Employee import Employee
from objects.Injury import Injury

from helpers.generate_repr import generate_repr

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

session = Session(engine)

colby = Employee(first_name="Colby", last_name="Hunter")
brandon = Employee(first_name="Brandon", last_name="Rivera")

session.add_all([colby, brandon])

session.flush()

colby.manager_id = brandon.id
session.expire(colby, ['manager'])
session.expire(brandon, ['employees'])

injury = Injury(employee_dbid=colby.id, manager_dbid=colby.manager_id)

session.add(injury)

session.flush()

result = session.execute(select(Injury).where(Injury.employee_dbid == colby.id)).fetchall()

# print(result)

print(colby.injuries_had[0].manager)