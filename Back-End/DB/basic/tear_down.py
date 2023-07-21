import sqlite3

con = sqlite3.connect("test_db")
cur = con.cursor()

# Create Database

# Create Employee Status Table

cur.execute("""DROP TABLE employee_status(
    dbid    TEXT PRIMARY KEY,
    status  TEXT UNIQUE
);""")

# Create Employee Table

cur.execute("""CREATE TABLE employee(
    dbid            TEXT PRIMARY KEY,
    employee_id     UNIQUE, 
    first_name      TEXT,
    last_name       TEXT,
    preferred_name  TEXT,
    hire_date       TEXT,
    status          INTEGER,
    FOREIGN KEY(status) REFERENCES status(dbid)
);""")

# Create Job Class Table

cur.execute("""CREATE TABLE job_class(
    dbid            TEXT PRIMARY KEY,
    job_class_id    TEXT UNIQUE, 
    job_class_title TEXT UNIQUE
);""")

# Create Employee Job Class Table

cur.execute("""CREATE TABLE employee_job_class(
    dbid        TEXT PRIMARY KEY,
    job_class   INTEGER, 
    employee    INTEGER UNIQUE,
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
    primary_department  INTEGER,
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
    dbid                TEXT PRIMARY KEY,
    employee            TEXT,
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