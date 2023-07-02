import sqlite3
import uuid

con = sqlite3.connect("test_db")
cur = con.cursor()

def getUUID():
    return str(uuid.uuid4())

# Create Database

# Create Employee Status Table

cur.execute("""CREATE TABLE work_status(
    dbid    TEXT PRIMARY KEY,
    status  TEXT UNIQUE NOT NULL
);""")

work_statuses = [
    (getUUID(), "Active"),
    (getUUID(), "Terminated"),
    (getUUID(), "On Leave"),
    (getUUID(), "Fired")
]

# cur.executemany("INSERT INTO work_status(dbid, status) VALUES (?,?)", work_statuses)
# con.commit()

# Create Employee Table

cur.execute("""CREATE TABLE employee(
    dbid                    TEXT PRIMARY KEY,
    employee_id             TEXT UNIQUE, 
    first_name              TEXT,
    last_name               TEXT,
    preferred_name          TEXT,
    first_hire_date         TEXT,
    most_recent_hire_date   TEXT
);""")

cur.execute("""CREATE TABLE employee_work_status(
    employee    TEXT NOT NULL UNIQUE,
    status      TEXT NOT NULL,
    FOREIGN KEY(employee) REFERENCES employee(dbid),
    FOREIGN KEY(status) REFERENCES status(dbid),
    UNIQUE(employee, status)
);""")

# cur.execute("""INSERT INTO employee_work_status (employee, status) VALUES 
#     SELECT employee.dbid, work_status.dbid 
#     FROM employee, work_status 
#     WHERE employee.employee_id=? AND work_status.status =?
# ));""", ("7872934", "Active"))
# con.commit()

# print(cur.execute("SELECT * from employee;").fetchall())
# print(cur.execute("SELECT * from work_status;").fetchall())
# print(cur.execute("SELECT * from employee_work_status;").fetchall())

# Create Job Class Table

cur.execute("""CREATE TABLE job_class(
    dbid            TEXT PRIMARY KEY,
    job_class_title TEXT UNIQUE
);""")

# Create Employee Job Class Table

cur.execute("""CREATE TABLE employee_job_class(
    job_class   TEXT, 
    employee    TEXT UNIQUE,
    FOREIGN KEY(employee) REFERENCES employee(dbid),
    FOREIGN KEY(job_class) REFERENCES job_class(dbid)
);""")

# Create Primary Work Area Table

cur.execute("""CREATE TABLE primary_department(
    dbid            TEXT PRIMARY KEY,
    department_name TEXT UNIQUE
);""")

# Create Secondary Work Area Table

cur.execute("""CREATE TABLE secondary_department(
    dbid                TEXT PRIMARY KEY,
    department_name     TEXT UNIQUE,
    primary_department  TEXT,
    FOREIGN KEY(primary_department) REFERENCES primary_department(dbid)
);""")

# Create Injury Table

cur.execute("""CREATE TABLE injury(
    dbid                TEXT PRIMARY KEY,
    employee            TEXT,
    injury_date         TEXT,
    manager             TEXT,
    FOREIGN KEY(employee) REFERENCES employee(dbid),
    FOREIGN KEY(manager) REFERENCES employee(dbid)
);""")

# Create Next Level Manager Table

cur.execute("""CREATE TABLE next_level_manager(
    employee            TEXT UNIQUE,
    manager             TEXT,
    FOREIGN KEY(employee) REFERENCES employee(dbid),
    FOREIGN KEY(manager) REFERENCES employee(dbid)
);""")

# Create SWM Type Table

cur.execute("""CREATE TABLE swm_type(
    dbid    TEXT PRIMARY KEY,
    type    TEXT UNIQUE
);""")

# Create SWM Submission Table

cur.execute("""CREATE TABLE swm_submission(
    dbid                TEXT PRIMARY KEY,
    type                TEXT,
    employee            TEXT,
    trainer             TEXT,
    manager             TEXT,
    submission_date     TEXT,
    FOREIGN KEY(type) REFERENCES swm_type(dbid),
    FOREIGN KEY(employee) REFERENCES employee(dbid),
    FOREIGN KEY(trainer) REFERENCES employee(dbid),
    FOREIGN KEY(manager) REFERENCES employee(dbid)
);""")

# Create DOK Type Table

# Create DOK Submission Table

con.close()