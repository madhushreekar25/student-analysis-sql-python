import pyodbc
connection = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=MADHUSHREE_PROJECT;"
    "TRUSTED_CONNECTION=yes;"
    "TRUSTSERVERCERTIFICATE=yes;"
)
cursor = connection.cursor()
print("Pass student list")
cursor.execute("SELECT * FROM PASS_STUDENT")
for row in cursor.fetchall():
    print(row)

print("Subject wise average marks")
cursor.execute("SELECT * FROM SUBJECT_AVERAGE")
for row in cursor.fetchall():
    print(row)
connection.close()
