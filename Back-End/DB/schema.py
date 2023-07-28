import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from DB.orm.objects.Employee import Employee as EmployeeModel
from DB.orm.objects.Injury import Injury as InjuryModel
from DB.orm.objects.JobClass import JobClass as JobClassModel
from DB.orm.objects.PrimaryDepartment import PrimaryDepartment as PrimaryDepartmentModel
from DB.orm.objects.SecondaryDepartment import SecondaryDepartment as SecondaryDepartmentModel
from DB.orm.objects.WorkStatus import WorkStatus as WorkStatusModel

class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

class Injury(SQLAlchemyObjectType):
    class Meta:
        model = InjuryModel
        interfaces = (relay.Node, )

class JobClass(SQLAlchemyObjectType):
    class Meta:
        model = JobClassModel
        interfaces = (relay.Node, )

class PrimaryDepartment(SQLAlchemyObjectType):
    class Meta:
        model = PrimaryDepartmentModel
        interfaces = (relay.Node, )

class SecondaryDepartment(SQLAlchemyObjectType):
    class Meta:
        model = SecondaryDepartmentModel
        interfaces = (relay.Node, )

class WorkStatus(SQLAlchemyObjectType):
    class Meta:
        model = WorkStatusModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    employee_search = graphene.List(
        Employee,
        employee_id=graphene.String(required=False),
        first_name=graphene.String(required=False),
        last_name=graphene.String(required=False),
        first_hire_date=graphene.String(required=False),
        most_recent_hire_date=graphene.String(required=False),
        job_class=graphene.String(required=False),
        manager_first_name=graphene.String(required=False),
        manager_last_name=graphene.String(required=False),
        manager_employee_id=graphene.String(required=False),
        primary_department=graphene.String(required=False),
        secondary_department=graphene.String(required=False),
        work_status=graphene.String(required=False),
    )

    all_employees = SQLAlchemyConnectionField(Employee.connection)
    all_injuries = SQLAlchemyConnectionField(Injury.connection)
    all_job_classes = SQLAlchemyConnectionField(JobClass.connection)
    all_primary_departments = SQLAlchemyConnectionField(PrimaryDepartment.connection)
    all_secondary_departments = SQLAlchemyConnectionField(SecondaryDepartment.connection)
    all_work_statuses = SQLAlchemyConnectionField(WorkStatus.connection)

    def resolve_employee_search(self, info,
        employee_id="", first_name="", last_name="", first_hire_date="",
        most_recent_hire_date="", job_class="", manager_first_name="",
        manager_last_name="", manager_employee_id="", primary_department="",
        secondary_department="", work_status=""
    ):
        employee_query = Employee.get_query(info)
        work_status_query = WorkStatus.get_query(info)

        job_class_query = JobClass.get_query(info)
        job_class_query_result = job_class_query.filter(JobClassModel.title == job_class).all()
        job_class_id = job_class_query_result[0].id if len(job_class_query_result) != 0 else ""

        work_status_class_query = WorkStatus.get_query(info)
        work_status_query_result = work_status_query.filter(WorkStatusModel.status == work_status).all()
        work_status_id = work_status_query_result[0].id if len(work_status_query_result) != 0 else ""

        manager_query_result = employee_query.filter(
            (EmployeeModel.first_name == manager_first_name) |
            (EmployeeModel.last_name == manager_last_name) |
            (EmployeeModel.employee_id == manager_employee_id)
        ).all()
        manager_id = manager_query_result[0].id if len(manager_query_result) != 0 else ""

        primary_department_query = PrimaryDepartment.get_query(info)
        primary_department_query_result = primary_department_query.filter(PrimaryDepartmentModel.name == primary_department).all()
        primary_department_id = primary_department_query_result[0].id if len(primary_department_query_result) != 0 else ""
        
        secondary_department_query = SecondaryDepartment.get_query(info)
        secondary_department_query_result = secondary_department_query.filter(SecondaryDepartmentModel.name == secondary_department).all()
        secondary_department_id = secondary_department_query_result[0].id if len(secondary_department_query_result) != 0 else ""

        employees = employee_query.filter(
            (EmployeeModel.employee_id == employee_id) |
            (EmployeeModel.first_name == first_name) |
            (EmployeeModel.last_name == last_name) |
            (EmployeeModel.first_hire_date == first_hire_date) |
            (EmployeeModel.most_recent_hire_date == most_recent_hire_date) |
            (EmployeeModel.job_class_id == job_class_id) |
            (EmployeeModel.manager_id == manager_id) |
            (EmployeeModel.primary_department_id == primary_department_id) |
            (EmployeeModel.secondary_department_id == secondary_department_id) |
            (EmployeeModel.work_status_id == work_status_id)
        ).all()
        return employees
        

schema = graphene.Schema(query=Query)