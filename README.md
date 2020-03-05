# Lab 3

## Pre-requisites

* Install Pipenv

```
pip install pipenv
```

* Install Flask

```
pipenv install flask==1.1.1
```
* Create the app.py.

* run the app.py from a shell/terminal

  ```
pipenv shell
env FLASK_APP=app.py flask run
  ```
* Open this URL in a web browser or run this CLI to see the output
```
curl -i http://127.0.0.1:5000/graphql
```

## Test & Output

* Mutate a new student

```
mutation {
  students(name:"Bob Smith") 
}
```

* Quety an existing student

_Request_

```
{
  students(sid:1238125) {
    name
  }  
}
```

_Response_

```
{
  "data": {
    "students": {
      "name": "Bob Smith"
    }
  }
}
```

* Mutate a class

```
mutation{
  classes(name:"CMPE273")
}
```

* Add students to a class

```
mutation{
  enroll(sid:1238125, cid:1122334)
}
```

* Query a class

```
{
  classes(cid:1122334) {
    name
    studentinfo{
      name
      id
    }
  }
  
}
```

_Response_

```
{
  "data": {
    "classes": {
      "name": "CMPE273",
      "studentinfo": [
        {
          "id": 1238125,
          "name": "Bob Smith"
        }
      ]
    }
  }
}
```




