
"""

>>> from week4hw import *


>>> vowelIndex('hello')
1
>>> vowelIndex('string')
3
>>> vowelIndex('strIng')
3
>>> vowelIndex('BUY')
1
>>> vowelIndex('APPLE')
0
>>> vowelIndex('nymphly')
-1
>>> vowelIndex('string')==3
True
>>> vowelIndex('nymphly')==-1
True


>>> flipCase('ostrich')
'OSTRICH'
>>> flipCase('LyNx')
'lYnX'
>>> flipCase('Orangutan')
'oRANGUTAN'
>>> flipCase('AardVark')
'aARDvARK'
>>> flipCase('CamelCase')
'cAMELcASE'
>>> flipCase('ostrich')=='OSTRICH'
True


>>> palindromes("Hey Anna, would you prefer to ride in a kayak or a racecar?")
['Anna', 'a', 'kayak', 'a', 'racecar']
>>> palindromes("Able was I ere I saw Elba.")
['I', 'ere', 'I']
>>> palindromes("Otto, go see Tacocat at the Civic Center, their guitar solos are wow!")
['Otto', 'Tacocat', 'Civic', 'solos', 'wow']
>>> palindromes("Otto, go see Tacocat at the Civic Center, their guitar solos are wow!") == ['Otto', 'Tacocat', 'Civic', 'solos', 'wow']
True


>>> squares( [[1,2,3],[4,5],[6,7,8,9]]) # 1,4,9 are perfect squares
3
>>> squares( [[1,2,3],[4,5,6],[7,8],[9,10,11,12],[13,14,15,16]] )
4
>>> squares( [ range(1,1000,7), range(1,500,13)])
12
>>> squares( [range(2,1000,3), range(7,100,8), range(8,1000,5)])
0
>>> squares( [ range(1,1000,7), range(1,500,13)])==12
True


>>> rps('R','P') # player 2 wins, return 1
1
>>> rps('R','S') # player 1 wins, return -1
-1
>>> rps('S','S') # tie, return 0
0
>>> [ (p1,p2,rps(p1,p2)) for p1 in 'RPS' for p2 in 'RPS']
[('R', 'R', 0), ('R', 'P', 1), ('R', 'S', -1), ('P', 'R', -1), ('P', 'P', 0), ('P', 'S', 1), ('S', 'R', 1), ('S', 'P', -1), ('S', 'S', 0)]


"""