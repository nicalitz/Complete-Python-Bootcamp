dict = {'key1': 1, 'key2': 4, 'key3': 'bacon', 'key4': ['item0', 'item1', 'item2']}
print dict['key3']
print dict['key4'][0].upper()

dict['key2'] -= 4
print dict['key2']

dict2 = {}
dict2['one'] = 'one'
dict2['two'] = 2
print dict2

dict3 = {'key1':{'nestkey':{'subnestkey':'value'}}}
print dict3['key1']['nestkey']['subnestkey'] #NB: Keys are defined as strings, and should be called as such

print dict.keys()
print dict.values()
print dict.items()