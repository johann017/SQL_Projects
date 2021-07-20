# SQL_Projects

## Description
- ### `MySQLPractice.py`
  - #### Overview: 
    - This program creates a table, reads user list and adds their progressive rank to the table. 
  - #### Details: 
    - A query statement is used to add each name in a loop as they are read. Before the end of the file, the program prints the contents of the table. At the end of this program, the table and its contents will be dropped so that if this program is run again, the table wont exist.

- ### `Sign_In_Sign_Up_GUI.py`
  - #### Overview:
    - This program creates an application that features an interactive interface which gives users an option to sign in or to sign up and handle either event appropriately. 
  
  - #### Details:
    - If user chooses to sign up, three fields to enter a name, a username and a password is displayed. From there, this information is stored in a table in the background. If the user chooses to sign in, a username and password field is displayed to be filled out. The user's input is then used to check if the username and password is in the table. Depending if the input matched or not, there is a message displayed according to the outcome. This program cleans the user input by checking if it contains any key SQL commands as a way to prevent the user from doing a basic SQL injection.

<h3 align="center">Main Page</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/57604319/125364574-994b2300-e327-11eb-9126-1a0655cf2d33.PNG" height = 300 width = 300/>
</p> 
  
<h3 align="center">Sign Up</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/57604319/125364677-c0a1f000-e327-11eb-8a85-06d52236c761.PNG" height = 300 width = 300/>
</p>

<h3 align="center">Sign In</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/57604319/125364694-c992c180-e327-11eb-824b-1bcec3cdd035.PNG" height = 300 width = 300/>
</p>

## Setup
- Install [GitHub CLI](https://cli.github.com/) and connect to GitHub account
- Open Git CMD
- Run `gh repo clone johann017/SQL_Projects` in the command line

`MySQLPractice.py`:
To run this, type the following in to the command line:
  ```
  python MySQLPractice.py
  ```


`Sign_In_Sign_Up_GUI.py`:
To run this, type the following in to the command line:
  ```
  python Sign_In_Sign_Up_GUI.py
  ```
