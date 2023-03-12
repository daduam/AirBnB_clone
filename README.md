<center>
    <img src="hbnb.png" width="306.75" height="129.5">
</center>

## Project Description

The project is a simple clone of the AirBnB website. It currently includes a command interpreter used for admin purposes.

## Command interpreter

The command interpreter is used to manage the objects of this project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc
- Do operations on objects (count, compute stats, etc)
- Update attributes of an object
- Destroy an object

### How to Start

The project requires python3. The command interpreter can be started running

```bash
python3 console.py
```

or simply

```bash
./console.py
```

or in non-interactive model, example

```bash
echo "help" | ./console.py
```

### Usage

The command interpreter exposes the following commands

| Command   | Usage                                               | Help                                                                               |
| --------- | --------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `quit`    | `quit`                                              | Exits the program. Also EOF.                                                       |
| `create`  | `create <class name>`                               | Creates an instance of class name, saves it and prints the id                      |
| `show`    | `show <class name> <id>`                            | Prints the string representation of an instance based on the class name and id     |
| `destroy` | `destroy <class name> <id>`                         | Deletes an instance based on the class name and id                                 |
| `all`     | `all` or `all <class name>`                         | Prints all string representation of all instances based or not on the class name   |
| `update`  | `update <class name> <id> <attr_name> <attr_value>` | Updates an instance based on the class name and id by adding or updating attribute |

### Examples

```bash

# Create new instance of BaseModel
(hbnb) create BaseModel

# Show instance of BaseModel with id 1234-1234-1234
(hbnb) show BaseModel 1234-1234-1234

# Delete instance of BaseModel with id 1234-1234-1234
(hbnb) destroy BaseModel 1234-1234-1234

# List all saved instances of BaseModel
(hbnb) all BaseModel

# List all saved instances
(hbnb) all

# Update BaseModel with id 1234-1234-1234 by setting the email attribute to aibnb@mail.com
(hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"

```
