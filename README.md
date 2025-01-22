script.py opens the site and lets you log in and navigate to the course, joining and clicking automatically
auto.py does everything automatically in headless mode

To run auto.py: Create a .env file with key names email, password, course
Example:
email="j123smith@uwaterloo.ca"
password="abcd"
course="CS 135"
**_ Course name must contain same whitespace as course name on iClicker _**

Then run command "python3 script.py" or "python3 auto.py"
