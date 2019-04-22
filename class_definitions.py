class Customer:
	def __init__(self, name, orders):
		self.name = name
		self.orders = orders
	
class Order:
	def __init__(self, date, total, customer, lines):
		self.date = date
		self.total = total
		self.customer = customer
		self.lines = lines
	
class OrderLine:
	def __init__(self, order, product, count, total):
		self.order = order
		self.product = product
		self.count = count
		self.total = total
	
class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price
	
