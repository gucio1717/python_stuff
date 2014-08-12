from unittest.mock import patch, MagicMock
# def dekorator(fu):
#     def aaa(*args, **kwds):
#         print ('Nazwa funkcji: ', fu.__name__)
#         print(fu.__doc__)
#         return fu(*args, **kwds)
#     return aaa
# 
# # @dekorator
# # def print2(*args, **kwds):
# #     print(*args, **kwds)
# 
# print2 = dekorator(print)
# print2('dupa')


content =  ['dupa', 'blada']
with patch('builtins.open', create=True) as openmock:
    fh = openmock().__enter__.return_value
    fh.__iter__.return_value = ( i for i in content)
    print(openmock)
    with open('c:/mylog.log', 'r') as f:
        for i in f:
            print(i)
        print(openmock.mock_calls)
    print('koniec')
        
