# coding-assignment

1. First need to download and install anaconda from https://www.anaconda.com/products/distribution
2. Then have to create a virtualenvironment using the command - conda create --name myenv
3. Then on that virtualenvironment have to install django using the command - conda install -c anaconda django
4. Also django rest framework need to be installed on the virtualenvironment and which can be done by using the command - conda install -c conda-forge djangorestframework
5. Git need to be installed in order to clone the repository
6. After completing the above steps a folder need to be created (can be on any drive) where the project will be cloned by using the command - git clone https://github.com/shafiqulislam561/coding-assignment.git
7. Then need to navigate to to the folder containing manage.py file
8. After navigating to the folder a super user need to be created by using the command - python manage.py createsuperuser (for doing CRUD operations of the app)
9. Alternatively Parent User can be created by using the following rest api http://127.0.0.1:8000/app/parent/create and providing json data as:  
    {
        "first_name": "Robert",
        "last_name": "Jack",
        "street": "example street",
        "city": "example city",
        "state": "example state",
        "zip": "1"
    }
    If the Parent User is created the server will response with HTTP 200 OK
10. Using the following rest api http://127.0.0.1:8000/app/parent/list created Parent Users data can be retrieved from the server
11. The above Parent User data can be updated by using the following rest api http://127.0.0.1:8000/app/parent/update/5 and providing json data as:
     {
        "first_name": "Updated Robert",
        "last_name": "Updated Jack",
        "street": "Updated example street",
        "city": "Updated example city",
        "state": "Update example state",
        "zip": "Update 1"
     }
    If the above Parent User is updated the server will response with HTTP 200 OK
12. The above Parent User can be deleted by using the following rest api http://127.0.0.1:8000/app/parent/update/5 and when the Parent User data will be deleted the server will response with HTTP 200 OK
13. Alternatively Child User can be created by using the following rest api http://127.0.0.1:8000/app/child/create and providing json data as:  
    {
        "first_name": "Little Robert",
        "last_name": "Jack",
        "parent": 5
    }
    If the Child User is created the server will response with HTTP 200 OK
14. Using the following rest api http://127.0.0.1:8000/app/child/list created Child Users data can be retrieved from the server
15. The above Child User can be updated by using the following rest api http://127.0.0.1:8000/app/child/update/5 and providing json data as:
    {
        "first_name": "Updated Little Robert",
        "last_name": "Updated Jack",
        "parent": 5
    }
    If the above Child User data is updated the server will response with HTTP 200 OK
16. The above Child User can be deleted by using the following rest api http://127.0.0.1:8000/app/child/update/5 and when the Child User data will be deleted the server will response with HTTP 200 OK
