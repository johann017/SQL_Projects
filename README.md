# SQL_Projects

## Setup
- Install [GitHub CLI](https://cli.github.com/) and connect it with GitHub account
- Open up Git CMD
- Run `gh repo clone johann017/API_Projects` in the command line

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

## Description
- ### `MySQLPractice.py`
  The purpose of this program was to experiment with working with MySQL. This program will create a table, read a list of users and add their position to the table. There will be one query statement that will be used to add each name in a loop as they are read. Before the end of the file, the program will print the contents of the table. At the end of this program, the table and its contents will be dropped so that if this program is run again, the table wont exit.

- ### `Sign_In_Sign_Up_GUI.py`
    This program creates a GUI that will allow users to sign in or sign up. 
  <p align="center">
    <img src="https://user-images.githubusercontent.com/57604319/125364574-994b2300-e327-11eb-9126-1a0655cf2d33.PNG" />
  </p> 
    If user chooses to sign up, there will be three fields to enter a name, a username and a password.
  <p align="center">
    <img src="https://user-images.githubusercontent.com/57604319/125364677-c0a1f000-e327-11eb-8a85-06d52236c761.PNG" />
  </p>
    From there, this information will be stored in a table without the user knowing. If the user chooses to sign in, there will be a username and a password field for them to fill out. The user input will then be used to check if the username and password is in the table.
  <p align="center">
    <img src="https://user-images.githubusercontent.com/57604319/125364694-c992c180-e327-11eb-824b-1bcec3cdd035.PNG" />
  </p> 
    Depending if the input matched or not, there will be a message displayed according to the outcome. This program scrubs the user input by checking if it contains any key SQL commands as a way to prevent the user from doing a basic SQL injection.
