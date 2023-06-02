# CHSPMS
## CHSPMS in a Nutshell
CHSPMS is a Management System being built to improve the tracking of employees, their injuries, and managing routine trainings.

It is meant to be tracking oriented instead of detail oriented.

Meaning the solution allows you to see that a training was done but not the details of the training.

The only exception to this is one particular type of training that asks 7-8 questions. In this case, you are able to see whether an employee answered a question correctly, but not what their specific answer was.

The reasoning behind this is that we incorporate retesting into our training methodology and require a 100% by the end of every month.

## The Technical Stuff

### Back-End

|Technology|Reason for Use|
|-|-
|Python|Drives a local webserver that hosts an API to the database
|Flask|Web Framework to build API Endpoints
|PostgreSQL|Development Database, being used at home for testing
|Access DB|The actual database I'm stuck with at work

### Front-End
|Technology|Reason for Use|
|-|-
|NodeJS|Drives a local webserver that hosts the website
|React|Allows for easy and modern user interfacing

### Why two different technologies to host webservers?
I'm more comfortable with Node when it comes to interacting with Databases and hosting webservers. But there is not a good solution for communicating with an Access Database using Javascript, however there is for Python.

### Why are you stuck with Access at work?
1. Because I'm not a hired developer and I'm working under restrictive privledges.

I need a solution that doesn't require installing anything. Fortunately NodeJS and Python are both obtainable tools, but databases are not.

However, nearly every company with the Office Suite has Access

2. I need to hide complexity while offering an easy backdoor

The more technology I add to the solution, the more complexity I have to hide. By the end, a user will click on an icon (a .bat file) that will run the Python and NodeJS servers in the background.

To stop the services, they will either click on a different icon (another .bat file), or click on a button somewhere on the website.

For the most part, this is how they will acccess the information. But if all else fails, they can access the information by opening the Access Database File.

I plan on going into the file and building some basic reports to help in these cases, but it should be considered emergency use in a read-only environment.

## Broad Overview of Goals
### Get a functional back-end and front-end running
### Personal Testing
### Hide the complexity
### Build fail-safes
### User Testing
### Optimization?
