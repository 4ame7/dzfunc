def function(a):
    if type(a) == tuple:
        print('words', len(a))
    elif type(a) == list:
        print('letters', len(list(filter(lambda x: type(x) == str, a))), 'numbers', len(list(filter(lambda x: type(x) in (int, float), a))))
    elif type(a) == str:
        print('letters', len(a))
    else:
        print('Unknown type')

function(('qwe', 2, 'asdsad', 'qwqsasdzxzc'))
function([1, 2, 3, 'a', 'b', 'c'])
function('abcd')
function({1: 2})