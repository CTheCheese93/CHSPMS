## Employees
### Data
* Employee ID
* First Name, Last Name
* Preferred Name
* Hire Date
* Status

### End Points
#### `GET /employee`

> Gets all employees

**URL Parameters**
| Parameter | Description
|-|-
|`employee_id`|i.e. 7672934
|`first_name`|"James"
|`last_name`|"Jonas"
|`preferred_name`|"J.J."
|`hire_date`|"05/23/22"
|`status`|"Active", "Terminated", etc.

#### `POST /employee`

> Creates an employee

| Values | Required | Unique
|-|-|-
|`employee_id`|Yes|Yes
|`first_name`|Yes|No
|`last_name`|Yes|No
|`preferred_name`|No|No
|`hire_date`|No|No
|`status`|No (Defaults to Active)|No

#### `PUT /employee/:employee_id`

> Update an Employee

| Values
|-
|`first_name`
|`last_name`
|`preferred_name`
|`hire_date`
|`status`

#### `DELETE /employee/:employee_id`

> Delete an Employee

## Job Classes
* Job Class ID
* Job Class Title

### End Points

#### `GET /job_class`

> Get all Job Classes

#### `GET /job_class/:job_class_id`

> Get Job Class by ID

#### `POST /job_class`

| Values | Required | Unique
|-|-|-
|`job_class_id`|Yes|Yes
|`job_class_title`|Yes|Yes

#### `PUT /job_class/:job_class_id`

> Update job Class by ID

|Values|Example|Required|Unique
|-|-|-|-
|`job_class`|"Hub Manager"|No|Yes
|`job_class_id`| "0293"|No|Yes

#### `DELETE /job_class/:job_class_id`

> Delete Job Class from Database

## Employee Job Class
* Employee ID
* Job Class ID

### End Points

#### `GET /job_class/:employee_id`

> Get Job Class of Employee

#### `PUT /job_class/:employee_id/:job_class_id`

> Update Employee to new Job Class

*Developer Note: PUT will automatically create an entry if it doesn't already exist **and it is a valid `employee_id`.***

## Status
* Status

### Possible Values
* Active
* Terminated
* Fired
* On Leave

### End Points

#### `GET /status`

> Get all possible statuses

#### `GET /status/:employee_id`

> Get status of employee

#### `POST /status`

> Creates new status

|Values|Example|Required|Unique
|-|-|-|-
`status`|"Active", "Terminated", etc.|Yes|Yes

#### `PUT /status/:status_dbid`

> Updates name of status

|Values|Example|Required|Unique
|-|-|-|-
|`status`|"Not at Work"|Yes|Yes

#### `DELETE /status/:status_dbid`

> Deletes a specific status

## Primary Work Area (Outbound, Inbound, Processing, etc.)
* Department Name

### End Points

#### `GET /deparment/primary`

> Get all primary departments

#### `GET /department/primary/:department_dbid`

> Get a primary department by dbid

#### `POST /department/primary`

> Creates new primary department

|Values|Required|Unique
|-|-|-
|`department_name`|Yes|Yes

#### `PUT /department/primary/:department_dbid`

> Updates primary department name by dbid

|Values|Required|Unique
|-|-|-
|`department_name`|Yes|Yes

#### `DELETE /department/primary/:department_dbid`

> Deletes primary department by dbid

## Secondary Work Area (PD1, PD2, Unload, Mez, etc.)
* Primary Department
* Department Name

### End Points

#### `GET /deparment/secondary`

> Get all secondary departments

#### `GET /department/secondary/:department_dbid`

> Get a secondary department by dbid

#### `POST /department/secondary`

> Creates new secondary department

|Values|Required|Unique
|-|-|-
|`department_name`|Yes|Yes
|`primary_department`|No|No

#### `PUT /department/secondary/:department_dbid`

> Updates secondary department name by dbid

|Values|Required|Unique
|-|-|-
|`department_name`|Yes|Yes
|`primary_department`|No|No

#### `DELETE /department/secondary/:department_dbid`

> Deletes secondary department by dbid

## Injuries
* Employee ID
* Injury Date

#### `GET /injury`

> Gets all injuries within given parameters, none results in all

**URL Parameters**

|Parameters|Description|If Omitted
|-|-|-
|`start_date`| Start date of search | Starts at earliest dated injury
|`end_date`| End date of search | Ends at current date

#### `GET /injury/:injury_dbid`

> Get injury based on injury_dbid

#### `GET /injury/employee/:employee_id`

> Get injuries for a specific employee

#### `POST /injury/:employee_id`

> Create injury for an employee

|Values|Required
|-|-
|`employee_id`|Yes
|`injury_date`|Yes
|`manager_id`|No

#### `PUT /injury/:injury_dbid`

> Update injury based on injury dbid

#### `DELETE /injury/:injury_dbid`

> Delete injury based on dbid

#### `DELETE /injury/employee/:employee_id`

> Delete all injuries for an employee based on employee id

## Next Level Manager
* Employee ID
* NLM Employee ID

#### `GET /manager`

> Get all managers

#### `GET /manager/:employee_id`

> Get manager for employee based on employee id

#### `PUT /manager/:employee_id/:nlm_employee_id`

> Updates or Creates NLM relationship with employee

|Values|Description|Required
|-|-|-
|`employee_id`|Employee getting a manager|Yes
|`nlm_employee_id`|Next Level Manager for target employee|Yes

#### `DELETE /manager/:employee_id`

> Removes manager/employee relation for specific employee, typically only being used when completely removing an employee.

## SWM Types
* SWM Type

## SWM Submissions
* Employee ID
* Trainer Employee ID
* Management Employee ID
* Submission Date
* SWM Type

### End Points

#### `GET /swm`

> Gets all SWMs based on provided parameters

**URL Parameters**
|Parameter|Description
|-|-
|`swm_type`|Filters SWMs by type using `dbid`, default to all and can only filter by one type
|`employee_id`|Filters SWMs by who was trained
|`trainer_id`|Filters SWMs by who performed the SWM
|`management_id`|Filters SWMs by manager who rostered the training
|`year`|Gets all SWMs for a given year
|`month`|Gets all SWMs for a given month, on it's own it will provide multiple years
|`day`|Gets all SWMs for a given day

#### `GET /swm/:swm_dbid`

> Gets SWM based on its dbid

#### `POST /swm`

|Value|Required
|-|-
|`swm_type`|Yes
|`employee_id`|Yes
|`trainer_id`|Yes
|`management_id`|No
|`submission_date`|Yes

#### `POST /swm/:employee_id`

|Value|Required
|-|-
|`swm_type`|Yes
|`trainer_id`|Yes
|`management_id`|No
|`submission_date`|Yes

#### `PUT /swm/id/:swm_dbid`

> Updates SWM based on it's dbid

|Value|Required
|-|-
|`swm_type`|No
|`employee_id`|No
|`trainer_id`|No
|`management_id`|No
|`submission_date`|No

#### `DELETE /swm/id/:swm_dbid`

> Deletes SWM based on it's dbid

## DOK Types (Management, Non-Management)
* DOK Type

## DOK Submissions
* DOK Type
* Employee ID
* Trainer Employee ID
* Q1
* Q2
* Q3
* Q4
* Q5
* Q6
* Q7
* Q8
* Submission Date

## Event Tracking

### Critical
* Creation of Employees
* Deletion of Employees
* Name change of Employee
* Preferred Name Change of Employee
* Job Class Change of Employee
* Status Change of Employees
* Hire Date Change of Employee
* Department Change of Employee
* Next Level Manager Change for Employee
* SWM Submitted for Employee
* SWM Deleted
* SWM Updated
* DOK Submitted for Employee
* DOK Deleted
* DOK Updated
* Injury Creation
* Injury Update
* Injury Deletion

### Important
* DOK Type Creation
* DOK Type Update
* DOK Type Deletion
* SWM Type Creation
* SWM Type Deletion
* SWM Type Update