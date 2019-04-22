import mysql.connector

cnx = mysql.connector.connect(user='user', database='microshop')
cursor = cnx.cursor()

def myQuery(query):
  result = query.split(".")
  if(len(result) == 1):
    query = f"select * from {result[0]}"
    return cursor.execute(query)

  elif(len(result) == 2):
    query = f"select name from {result[0]}"
    return cursor.execute(query)


customers = myQuery("Customer")
for customer in customer:
  print(customer)


names = myQuery("Customer.name")
for name in names:
  print(name)
