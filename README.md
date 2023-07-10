# AirBnB clone project

- This is not a full implementation but just some features to cover the fundamental concepts of programming.

- This project will be completed on stages

1. A command line interpreter to manipulate the data without UI.
2. A web application as the GUI of the project.
3. A database to store the data.
4. An API that provides a communication between the web application and the server with simple CRUD implementation.

## Fundamentals Concepts

1. Unit testing
2. Python package concept
3. Serialization/Deserialization
4. \*args, \*\*kwargs, CMD module, datetime module, uuid module
5. and more...

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
