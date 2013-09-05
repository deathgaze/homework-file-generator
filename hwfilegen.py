################################################################################
program =       'HWFILEGEN'
version =       '1.01'
description =   'Creates and formats your homework files for CSE 1310'
example =       'Example Usage: python3 hwfilegen.py 1 5'
################################################################################

import os
import datetime
templatePath = os.path.expanduser("~/.cse1310-template.txt")

# Set up a template file for future usage. setting reset to true will remove
# the template file before creating a new one.
def setup(reset = False):
    if reset:
        # Wipe the config file
        os.remove(templatePath)
        print('-- Resetting Template... --')
    
    if not os.path.exists(templatePath):
        # Get personal information from user so we can generate a good template
        print           (program, version)
        print           ("No configuration file found!")
        print           ("hwfilegen needs some information from you before it can work its magic.")
        print           ("** Note: You can leave these blank if you want to fill them out manually for each assignment **")
        username = input("To start with, it needs you name. Enter your name         -> ")
        sid      = input("Next, it needs to know your unique student ID 1000 number -> ")
        print           ("-----------------------BEGIN------------------------------------------")
        
        # Create template text
        template  =     "# " + username + "\n"
        template +=     "# UTA ID " + sid + "\n"
        template +=     "# {date}" + "\n"  
        template +=     "# Description: double_click_here_and_write_a_brief_description_for_your_program\n\n"
        template +=     "print(\"Hello world!\")"
        
        # Spit out the formatted result and ask for confirmation
        print           (template.format(date=datetime.date.today().strftime('%m/%d/%y')))
        print           ("------------------------END-------------------------------------------")
        print           ("This is what your template will look like. (The date will always be updated to the current date.)")
        ans = input     ("Is this okay? (y/n) -> ")
        if ans.lower() == 'n':
            print       ("User cancelled template creation. Run the program again to create a template.")
            quit()
        elif ans.lower() == 'y':
            templateFile = open(templatePath, 'w')
            templateFile.write(template)
            templateFile.close()
            return template
        else:
            print       ("Invalid response. Cancelling template creation. Come back when you can type y or n. pwnd. out.")
            quit()
    else:
        # Just load the template
        return open(templatePath).read();

# Build a callback object that will reset the utility if the user passes -reset
import argparse
class ResetAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setup(True);
        
# We're only interested in args less than 21 and greater than 0 for hw and up to 9 for tasks
parser = argparse.ArgumentParser(prog=program, description=description, epilog=example)
parser.add_argument('assignment', help='Assignment Number, a number from 1 through 20', type=int, metavar='assignmentNumber', choices=range(1, 21))
parser.add_argument('tasks', help='Number of Tasks, a number from 1 through 9', metavar='numberOfTasks', type=int, choices=range(1, 10))
parser.add_argument('-reset', '-r', help='Wipe the template file and create another one.', action=ResetAction, required=False, nargs=0)
parser.add_argument('-version', '-v', help='Display version information', action='version', version=('{p} {v}'.format(p=program, v=version)))
args = parser.parse_args()

# Convert assignment to an appropriate string
assignment = args.assignment
if assignment < 10:
    assignment = '0' + str(assignment)
else:
    assignment = str(assignment)
hwString = 'hw' + assignment

# Check to see if the folder already exists
if os.path.exists(hwString):
    # Punch out with an error
    print("Error: Cannot create folder -", hwString, "already exists!")
    quit()

# Format the template with today's date.
template = setup().format(date=datetime.date.today().strftime('%m/%d/%y'))

# DO IT 
os.mkdir(hwString)
for i in range(1, args.tasks + 1):
    open(os.path.normpath(hwString + "/" + hwString + "_task" + str(i) + ".py"), 'w', encoding='utf-8').write(template)