# Employee group selector 
This repository contains an algorithm for selecting employee groups for a given task that requires a set of skills that
the members of the group cover with the groups being not bigger than needed.


## Running the algorithm locally
The prerequisites for running this project locally is having Python3.8+ installed along with python3-venv and pip:
```
apt install python3-venv
apt install python3-pip
```
After that, navigate to the root of the project and start the `setup.sh` script:
```
bash setup.sh
```
This will create a virtual environment and download the necessary packages.

To run the algorithm for a given set of required skills, use the following command (note: the skills do not need to be
in alphabetical order):
```
python3 run_selection.py a b 
```
The output for this will be the following:
```
A
F
G H
```

## Run tests
In order to run the tests, run the following commands in the root of the project:
```
python3 -m unittest tests.selector
```