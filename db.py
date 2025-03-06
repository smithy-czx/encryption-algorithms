import sqlite3

def execute_query(command, parameters=None):
    con = sqlite3.connect("cryptology.db")
    cur = con.cursor()
    
    if parameters:
        cur.execute(command, parameters)
    else:
        cur.execute(command)
    
    con.commit()
    result = cur.fetchall()
    con.close()   
    return result

def initialise():
   ## TODO: move these commands into separate text files
   
   command = """CREATE TABLE IF NOT EXISTS Student(
       Username TEXT PRIMARY KEY,
       Password TEXT,
       Year INTEGER
    )"""
   execute_query(command)

   



def register(username, password, year):
    command = f"""INSERT INTO Student VALUES
        ("{username}", "{password}", "{year}")
        """
    
    execute_query(command)
    
def login(username, password):    
   # command = "SELECT Username FROM Student WHERE Year=8" # select usernames for all students in year 8
   command = f'SELECT Username FROM Student WHERE Password = "{password}" AND Username = "{username}"' 
   result = execute_query(command)
   if result: # if there are any rows returned by the query
       return True
   else:
       return False

def get_year(username):
    command = f'SELECT Year FROM Student WHERE Username = "{username}"'
    result = execute_query(command)
    year = result[0][0]
    return year

def get_username():
    names = []
    command = f'SELECT Username FROM Student'
    result = execute_query(command)
    for username in result:
        names.append(username[0].upper())
    
    return names

def print_all_records():
    command = 'SELECT * FROM Student'
    result = execute_query(command)
    if result:
        print("All Records in Student Table:")
        for row in result:
            print(row)
    else:
        print("No records found.")

def delete_record(username):
    command = "DELETE FROM Student WHERE Username = ?"
    execute_query(command, (username,))
    print(f"Record for {username} deleted.")


#delete_record()
# login('user2', '12345')


# PK = primary key
# every table has to have a column designated as the primary key
# the values of the primary key must be unique for each row

# Student
# ----------------------------------------
# username (PK) | password   |    year
# ----------------------------------------
# user1         | 12345      |    8
# user2         | mypass123  |    12 
