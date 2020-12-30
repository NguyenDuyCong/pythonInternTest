#-*-coding:utf-8-*-
'''
2. Đọc file customer.csv sau đó lưu hết vào database. Yêu cầu:
	- Database dùng mysql
	- Database được tạo trước
	- Table sẽ được tự động tạo khi chạy
'''
import pymysql
import csv

# connect to database
connection = pymysql.connect(host="localhost", user="root", passwd="", database="test")
# print("sussess")
cursor = connection.cursor()

# read data from csv
data = csv.reader(open('customer.csv'))
row_0 = next(data)
fieldname = ",".join(row_0)

create_query = "CREATE TABLE IF NOT EXISTS customers("
for i in range(len(row_0)):
	if i == len(row_0) - 1:
		create_query += row_0[i] + " varchar(50)"
	else:
		create_query += row_0[i] + " varchar(50),"

create_query += ")"
# print(string_query)

cursor.execute(create_query)

insert_query = "INSERT INTO customers(" + fieldname + ") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"   
# print (insert_query)

for row in data:
	cursor.execute(insert_query,row)

connection.commit()
cursor.close()