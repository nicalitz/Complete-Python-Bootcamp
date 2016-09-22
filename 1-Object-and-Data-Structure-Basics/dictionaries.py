# DIctionaries are very flexable in what they can hold
dict = {'key1': 1, 'key2': 4, 'key3': 'bacon', 'key4': ['item0', 'item1', 'item2']}
print dict['key3']
print dict['key4'][0].upper()

dict['key2'] -= 4
print dict['key2']

dict2 = {}
dict2['one'] = 'one'   # creating a new key through assignment
dict2['two'] = 2
print dict2

dict3 = {'key1': {'nestkey': {'subnestkey': 'value'}}}
# NB: Keys are defined as strings, and should be called as such
print dict3['key1']['nestkey']['subnestkey']

# Dictionary methods
print dict.keys()   # return a list of all keys
print dict.values()   # return all values
print dict.items()   # return tuples of all key-value pairs
