### Task: 
## compare workflow of different types of databases

Let's take the example of an HR system that needs to process a resume.

To do this, we will create the entity user (login, password) and his resume (standard fields).

Write an application that will store entity data in ```relational```, ```document```, and ```graph``` databases.

Mandatory conditions:

- there must be one-to-many relationships
- there must be many-to-many relationships
- there must be different queries:
    - pick up resume
    - take away all the hobbies that exist in the resume
    - pick up all the cities found in the resume
    - take away the hobbies of all acquirers living in a given city
    - take away all applicants who worked in one institution (we do not specify the institution)