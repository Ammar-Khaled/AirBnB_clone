# AirBnB clone project

![HBnB Logo](hbnb_logo.png)

## Contents

- [Description]()
- [Future Stages]()
- [Environment]()
- [Fundamental Concepts]()
- [Repo Contents]()
- [Installation]()
- [Usage]()
- [Built with]()
- [AUTHORS]()

## Description
- This is not a full implementation but just some features to cover the fundamental concepts of programming.

- This is the first phase of a four phase project, to create a basic clone of the AirBnB web app.

- This project will be completed on four stages:
1. A command line interpreter to manipulate the data without UI.
In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

## Future Stages
2. A web application as the GUI of the project.
3. A database to store the data.
4. An API that provides a communication between the web application and the server with simple CRUD implementation.

## Environment
The console was developed in Ubuntu 20.04LTS using python3 (version 3.8.5).

## Fundamental Concepts

1. Unit testing
2. Python package concept
3. Serialization/Deserialization
4. \*args, \*\*kwargs, CMD module, datetime module, uuid module
5. and more...

## Repo Contents
This repository constains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |
|[utils.py](./utils.py) | set of utility functions |

## Installation
Clone the repository and run the console.py
``` sh
$ git clone https://github.com/------/AirBnB_clone.git
$ cd AirBnB_clone
$ ./console.py
```

## Usage

|   **Command**   |   **Description**   |
| -------------- | --------------------- |
| `create <class_name>` | Creates an instance of given class, saves it and prints its id |
| `show <class_name> <id>` or `<class_name>.show(<id>)` | Prints the string representation of an instance based on the class name and id |
| `all` or `all <class_name>` or `<class_name>.all()` | Prints all string representation of all instances based or not on the class name |
| `update <class_name> <id> <attribute_name> "<attribute_value>"` | Updates an instance based on the class name and id by adding or updating attribute (save the change into the storage) |
| `<class_name>.update(<id>, <attribute_name>, <attribute_value>)` | Updates an instance based on the class name and id by adding or updating attribute (save the change into the storage) |
| `<class_name>.update(<id>, <dictionary_representation>)` |  update an instance based on his ID with a dictionary |
| `destroy <class_name> <id>` or `<class_name>.destroy(<id>)` | Deletes an instance based on the class name and id (save the change into the storage) |
| `<class_name>.count()` | Retrieve the number of instances of a class |
| `help <command>` | Prints information about specific command |
| `quit` | Exit the program |
| `EOF` | Exit the program |

## The command line interpreter

- The entry point to manipulate the data using the command line.

```sh
# to start
$ ./console.py
(hbnb)
```

- use the command `help` to show all commands and a help message for every command.

```sh
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create  help  quit

(hbnb) quit
$
```

- Also you can use the interpreter in non-interactive mode.

```sh
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  create  help  quit

(hbnb)
$
```
## Authors
Fadi Asaad <firon1222@gmail.com>
Ammar-Khaled <ammar.khaled.github@gmail.com>
