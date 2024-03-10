# Welcome to the AirBnB clone project!

Description:
This is the first step towards building your first full web application: the AirBnB clone.
This first step is very important because you will use what you build during this project
with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- Put in place a parent class (called BaseModel) to take care of the initialization,
  serialization and deserialization of your future instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine.

Command interpreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object.

Storage:
Persistency is crucial for a web application. This project will manipulate two types of storage: file and database.
The initial focus is on file storage.

The console:
- Create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

How to use it:
Our shell works like this in non-interactive mode:

$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 

In order to use the HBNB console in interactive mode, run the file console.py by itself:

$ ./console.py
While running in interactive mode, the console displays a prompt for input:

$ ./console.py
(hbnb) 

To quit the console, enter the command quit, or input an EOF signal (ctrl-D).

$ ./console.py
(hbnb) quit
$

$ ./console.py
(hbnb) EOF
$

How to test:
Unittests for the HBNB project are defined in the tests folder.

Run all tests:

$ python3 unittest -m discover tests

Run a specific single test:

$ python3 unittest -m tests/test_console.py

Development Environment:
Tested on Ubuntu 14.04 LTS, built in Python 3.4.3.

Authors:
Simangele Tutubala <Simangeletutubala>
