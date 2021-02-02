import os
import pymysql
# Get username from Cloud9 workspace
# Modify this variable if running on another environment)

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
