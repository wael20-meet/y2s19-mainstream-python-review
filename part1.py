# Part 1 of the Python Review lab.

def hello_world():
	return ("hello world")
	pass

def greet_by_name(name):
	return ("hello "+name)
	pass

def encode(x):
	return (x*3953531)
	pass

def decode(y):
	return (y/3953531)
	pass

hello_world()
greet_by_name("wael")
encode(391241)
decode(encode(5))