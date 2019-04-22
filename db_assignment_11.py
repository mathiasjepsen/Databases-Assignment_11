import json


json_string = """
{ "schemaName": "MicroShop",
  "entities": [
  	{"Customer": {
  		"name": "String",
  		"orders" :"*Order"}
		},
  	{"Order" :{
  		"date": "String",
  		"total": "Number",
  		"customer": "Customer",
  		"lines": "*OrderLine" }
		},
  	{"OrderLine" : {
  		"order": "Order",
  		"product": "Product",
  		"count": "Number",
  		"total": "Number" }
		},
  	{"Product" : {
  		"name": "String",
  		"price" :"Number"}
		}
  ]
}"""

def valueOf(sql_type):
	if sql_type == "String":
		sql_type = "VARCHAR(30)"
	elif sql_type == "Number" or not sql_type.startswith("*"):
		sql_type = "INT"
	if sql_type.startswith("*"):
		sql_type = None
	return sql_type

data = json.loads(json_string)
with open(data["schemaName"] + ".sql", 'w') as outfile:
	outfile.write("create database " + data["schemaName"] + ";\n")
	for e in data["entities"]:
		keys = e.keys()
		table_name = list(e.keys())[0]
		outfile.write("drop table if exists " + table_name + ";\n")
		outfile.write("create table " + table_name + "(\n")
		for columns in e.values():
			for column in columns:
				if valueOf(columns[column]) is not None:
					outfile.write("\t" + column + " " + valueOf(columns[column]) + "\n")
		outfile.write(");\n")

def createTable(table_name, columns):
	str =	"create table " + table_name + "(\n"
	for column in columns:
		str += "\t" + column + " " + columns[column] + "\n"
	return str

def jsonToPython():
	str = ""
	with open("class_definitions.py", "w") as f:
		for element in data["entities"]:
			str += "class ".lstrip() + list(element.keys())[0] + ":\n\t"
			str += "def __init__(self, "
			for attribute in element.values():
				for index, value in enumerate(attribute):
					str += value
					if not(len(attribute) -1 == index):
						str += ", "
					if (len(attribute) -1 == index):
						str += "):\n\t"
				for v in attribute.keys():
					str += "\tself." + v + " = " + v + "\n\t"
				str += "\n"
		f.write(str)
