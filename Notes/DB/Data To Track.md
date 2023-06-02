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

#### `GET /deparment/primary`

> Get all primary departments

#### `GET /department/primary/:department_dbid`

## Secondary Work Area (PD1, PD2, Unload, Mez, etc.)
* Primary Work Area
* Department Name

## Injuries
* Employee ID
* Injury Date

## Next Level Manager
* Employee ID
* NLM Employee ID

## SWM Types
* SWM Type

## SWM Submissions
* Employee ID
* Management Employee ID
* Submission Date
* SWM Type

## DOK Types
* DOK Type

## DOK Submissions
* DOK Type
* Employee ID
* Management Employee ID
* Submission Date

## Event Tracking



## Critical
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

## Important
* DOK Type Creation
* DOK Type Update
* DOK Type Deletion
* SWM Type Creation
* SWM Type Deletion
* SWM Type Update