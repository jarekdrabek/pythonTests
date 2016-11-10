
class MyError(Exception):
	pass

def division_by_zero():
	raise MyError("Ble")

try:
	division_by_zero();
except Exception as ex: 
	print("An error occurred")
	print(ex.args)
	print(type(ex))