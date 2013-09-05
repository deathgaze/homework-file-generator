# homework-file-generator
A quick and easy utility for generating the proper file and folder structure to complete homework assignments for [Alexandra Stefan](http://vlm1.uta.edu/~alex/)'s CSE 1310 course taken at [UTA](http://www.uta.edu).

---

### Usage:

When its first run, regardless of what options its passed, hwfilegen will ask for the user's name and UTA ID (a unique ID number assigned to each student). It will then create a template and store it in the user's home folder. Then...

	python3 hwfilegen.py 1 3

Creates folder **hw01** and creates three Python source files with the naming scheme **hw01_task1.py**, **hw01_task2.py**, **hw01_task3.py**. Adds a template header to each file with the user's name, date, UTA ID and a blank description field.

	python3 hwfilegen.py -r

Wipes out the template and prompts the user to create a new one.

### Installation:

Copy the program somewhere convienient and add an alias appropriate to your OS.