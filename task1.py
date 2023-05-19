import re
from settings import mysql_connection


## write a function to check if a number has string or  not
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
 
# write a function for for validating an Email
def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # pass the regular expression
    # and the string into the fullmatch() method
    
    #return Boolean Value
    return re.match(pattern, email) is not None


## form to validate
def register(registration_form): 

    #your input from your input string (assume from front end , json)
    name = registration_form['name']
    username = registration_form['username']
    email = registration_form['email']
    dob = registration_form['dob']
    password = registration_form['password']
    
    #name lenth should be greater than 3 and should not have any digits
    ## check email validation here 
    ## password should be greater than 8 digits and must have numbers, reuse has_number function
    ## after validation insert into database
    ## create connection
    
    if len(name) < 4 or has_numbers(name):
        return "the name should have a minimum length of 4 characters and must not contain any digits."
    
    if len(username) < 6:
        return 'the username must have a minimum length of 5 characters.'
    
    if not check_email(email):
        return 'Invalid email.'
        
    if len(password) <= 8 or not has_numbers(password):
        return 'password should be greater than 8 digits and must have numbers.'
        
    # mydb = mysql_connection()
    # cursor = mydb.cursor()
    # query = 'SELECT * FROM my_users WHERE username = %s'
    # values = (username,)
    # cursor.execute(query, values)
    # if cursor.fetchone():
    #     return 'Username already exists'
    
    # query = 'INSERT INTO my_users (name, username, email, dob, password) VALUES (%s, %s, %s, %s, %s)'
    # values = (name, username, email, date, password)
    # cursor.execute(query, values)
    # mydb.commit()
    
    # mydb.close()
    
    return True
   
    
def capture_data(registration_form):
    
    ## if registration is valid
    data = register(registration_form)
    if data == True:
        
        name = registration_form['name']
        
        username = registration_form['username']
        email = registration_form['email']
        dob = registration_form['dob']
        password = registration_form['password']
        
        ## connect with database
        mydb = mysql_connection()
        ## returns cursor
        sql = mydb.cursor()
        
        ## check if username already in database, use 'where' clause
        ## if
        query = 'SELECT * FROM my_users where username = %s'
        values = (username,)
        sql.execute(query, values)
        if sql.fetchone():
            return 'username already taken, try another username.'

        #if username not taken create a new record, insert values into table
        query = "INSERT INTO my_users(name,username,email,date,password) VALUES (%s,%s,%s,%s,%s)"
        values = (name, username, email, dob, password)
        sql.execute(query,values)
        mydb.commit()
        mydb.close()
        return "registration data captured"
        
    else:
        return data
    

#do not delete following function
def task_runner():
    ## Test data
    name ='test username'
    user_name = 'testusername'
    email_value = 'test@testgmail.com'
    date_value = '15-12-1999'
    password_value = 'testdfs77ds'
    registration_form = {'name' : name,  'username' :user_name, 'email': email_value, 'dob' : date_value, 'password': password_value}
    print(capture_data(registration_form))