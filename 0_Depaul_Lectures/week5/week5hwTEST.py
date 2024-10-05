"""

>>> from week5hw import *

>>> doubleVowel('apple')
False
>>> doubleVowel('pear')
True
>>> doubleVowel('peAr')
True
>>> doubleVowel('DURIAN')
True
>>> doubleVowel('baNaNa')
False
>>> doubleVowel('baNaNa')==False
True


>>> numPairs( 3, [0,1,2,3] )
2
>>> numPairs( 4, [0,1,2,3] )
1
>>> numPairs( 6, [0,1,2,3] )
0
>>> numPairs( 4, [0,1,2,3,4,2] )
3
>>> numPairs( 4, [0,1,2,3,4,2,2] )
5
>>> numPairs( 4, [0,1,2,3,4,2,2] )==5
True


>>> hideShow('apple','11001')
'ap##e'
>>> hideShow('apple','00000')
'#####'
>>> hideShow('apple','11111')
'apple'
>>> hideShow('abcdefghijklmnopqrstuvwxyz',13*'01')
'#b#d#f#h#j#l#n#p#r#t#v#x#z'
>>> hideShow( 'df###re##', '101010101' )
'd#####e##'
>>> hideShow( 'df###re##', '101010101' )=='d#####e##'
True


>>> hideShow('apple','11001')
'ap##e'
>>> hideShow('apple','00000')
'#####'
>>> hideShow('apple','11111')
'apple'
>>> hideShow('abcdefghijklmnopqrstuvwxyz',13*'01')
'#b#d#f#h#j#l#n#p#r#t#v#x#z'
>>> hideShow( 'df###re##', '101010101' )
'd#####e##'
>>> hideShow( 'df###re##', '101010101' )=='d#####e##'
True


>>> clean(" hello ")
'hello'
>>> clean(" hello, how are you? ")
'hello, how are you?'
>>> clean("\n\n\t what's up,\n\n doc? \n \t")
"what's up,\n\n doc?"
>>> clean("\n\n\t what's up,\n\n doc? \n \t")=="what's up,\n\n doc?"
True


>>> sequence(3)
3
4
2
1
>>> sequence(4)
4
2
1
>>> sequence(17)
17
18
9
10
5
6
3
4
2
1


"""