script.py => Login and navigate to course are manual, Site opening and clicking are automatic

auto.py => Automatic everything, requires .env file

## To use auto.py

1. Create a file called .env in main folder
2. Paste in the three lines below
3. Modify the credentials to those of your own

** Keep the double quotation marks **

### .env file contents

email="j123smith@uwaterloo.ca"

password="abcd"

course="CS 135"

** Course name must contain same whitespace as course name on iClicker **

## Running the program

1. Using terminal, navigate into the project folder
2. Create .env file (if using auto.py)
3. Run command "python3 script.py" or "python3 auto.py"

### Troubleshooting

- The timeout for the program is 8 hours; the program will stop running 8 hours after start
- Chromedriver version is incorrect error message => Find the latest version of chromedriver online and replace the one in the src folder
