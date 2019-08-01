my_dict = {'key1' : 'value1' , 'key2':'value2'}
print(my_dict)
print(my_dict['key1'])

price_lookup = {'apple': 10, 'orange' : 20 , 'mango' : 30}
print(price_lookup['apple'])

# can define a list or dictionary within dictionary
dict = { 'k1' : 123 , 'k2' : ['a','b','c'] , 'k3' : {'insideKey' : 100}}
print(dict)
print(dict['k3']['insideKey'])
print(dict['k2'][2])
# to upper an element of list
print(dict['k2'][0].upper())
# set to a new value
dict['k1'] = 'NEW VALUE'
print(dict)

# Methods 
d = {'k1' : 'v1' , 'k2':'v2' , 'k3' : 'v3'}
    # return all the keys
print(d.keys())
    # return values
print(d.values())
    # return as items
print(d.items())