#Day7 Assignment
import mysql.connector as sqlcon
from tabulate import tabulate

try:
	conn = sqlcon.connect(host = "localhost", user = "root", database = 'student')
	cur = conn.cursor()
	cur.execute("select * from stu")
	result = cur.fetchall()
	print(tabulate(result, headers=['Roll', 'FName', 'LName', 'Percentage'], tablefmt='psql'))
	cur.execute("UPDATE stu SET LName = 'Raj' WHERE Roll = 101")
	cur.execute("select * from stu")
	result = cur.fetchall()
	print(tabulate(result, headers=['Roll', 'FName', 'LName', 'Percentage'], tablefmt='psql'))
except sqlcon.Error as e:
	print("Error in MySQl Table", e)

finally:
	if conn.is_connected():
		conn.commit()
		conn.close()
		cur.close()
		print("Connection is Closed")
