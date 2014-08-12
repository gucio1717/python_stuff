from unittest.mock import patch, MagicMock, mock_open
import os.path
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
    openmock().__enter__.return_value.__iter__.return_value = ( i for i in content)
    with open('c:/mylog.log', 'r') as f:
        for i in f:
            print(i)
        print(openmock.mock_calls)
    print('koniec')
        
file1 = 'aaa'
file2 = 'bbb'

with patch('os.path.isfile') as p:
    p.side_effect = lambda x: {'aaa': 'pierwszy', 'bbb': 'drugi'}[x]
    result1 = os.path.isfile(file1)
    result2 = os.path.isfile(file2)
    print(result1, result2)
    print(p.mock_calls)
    
@patch('os.path.isdir')
@patch('os.path.isfile')
def test_isdir(dirr, p_isfile, p_isdir):
    p_isdir.return_value = 'isfile'
    p_isfile.return_value = 'isdir'
    print(os.path.isdir(dirr))
    print(os.path.isfile(dirr))
    print(p.mock_calls)
    
test_isdir('aaa')