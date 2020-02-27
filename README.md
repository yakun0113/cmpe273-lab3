# Lab 3

## Pre-requisites

* Install _Ariadne_

```
pip install ariadne
```

* Install _unicorn_

```
pipenv install unicorn
```
* Create the app.py .

* Finally run the server.


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

* Add students to a class

```
mutation{
  enroll(sid:1238125, cid:1122334)
}
```



