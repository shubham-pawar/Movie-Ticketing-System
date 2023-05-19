import re
from settings import mysql_connection


mydb = mysql_connection()
## create cursor
sql = mydb.cursor()
#select ticket and ids
def select_movie(movie_id, no_of_tickets):
    
    ##take movie id and no of tickets as inputs
    
    ## only 5 tickets for a person condition validation
    if no_of_tickets <= 0 or no_of_tickets > 5:
        return False
    
    ##select movie_id and avaibility from the database
    sql.execute("SELECT availability FROM movies WHERE movie_id=%s",(movie_id,))
    result = sql.fetchone()

    ##validate if a particular movie id is available
    if not result:
        return False

    ## Display how many tickets available
    availability = int(result[0])
    
    if availability >= no_of_tickets:
        updated_availability = availability - no_of_tickets
    ## assume that payment gateway has processed (at the counter)

    #update the tickets dynamically into database (Change the type to int) (tickets available - ticket booked)
        sql.execute('UPDATE movies SET availability = %s WHERE movie_id = %s', (str(updated_availability), movie_id))
    ## this is to maintain realistic records
        mydb.commit()
    ## write update query, change from int to string record where movie_id = 'value'
        return True
    #return True when success
    #default return should be False
    return False

    ##challenge since the ticket count is in varchar format in table, you have to dynamically convert type and validate


#do not delete following function
def task_runner():
    print(select_movie(1001, 2))