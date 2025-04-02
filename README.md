Recipes-App Setup Instructions

STEP 1: Open your terminal

STEP 2: Navigate to the directory where you want to clone the GitHub repository 

STEP 3: Copy the repository URL from GitHub. 

STEP 4: Run the git clone command followed by the URL you copied. 
        git clone https://github.com/dannyvasq/recipes-app.git

STEP 5: Press enter. Git will clone the repository into your specified directory

STEP 6: Install the required packages to run the application:
        pip3 install flask flask_sqlalchemy flask_login flask_bcrypt 
        pip3 install flask_wtf wtforms email_validator

STEP 7: Run the app.py file:
        python3 app.py

STEP 8: Copy the IP address that appears on the terminal

STEP 9: Paste the IP address into the address bar of your web browser
        http://127.0.0.1:5000

STEP 10: Press the link to Register as a new user.

STEP 11: Enter a username and a easy to remember password. 
         Min 4, Max 20 characters for both, the username and the password. 

STEP 12: Explore the recipes-app

STEP 13: Alternative, you can explore the recipes-app as one of the already 
         registered users.  

Registered Users:

  - First User:
    - Username: Danny
    - Password: 1234
    - Recipes: Spagetti Carbonara, Cheeseburger, and Lomo Saltado

  - Second User:
    - Username: Daniel
    - Password: 1234
    - Recipes: Macaroni and Cheese, Feijoada, Empanadas

