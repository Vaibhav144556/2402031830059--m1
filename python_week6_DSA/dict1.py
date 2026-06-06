mydict = {
	'id':101,
	'name':"Ayush",
	'contact':9857458630
}

print(type(mydict))
print(mydict)

print(mydict['contact'])

mydict['address'] = "Ahmedabad"
print(mydict)

del mydict['contact']
print(mydict)