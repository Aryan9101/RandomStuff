Python 3.6.1rc1 (v3.6.1rc1^0:e0fbe5feee4f9c00f09eb9659c2182183036261a, Mar  4 2017, 20:00:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.sin(60)
-0.3048106211022167
>>> math.sin(math.pi / 6)
0.49999999999999994
>>> def getRange(time, x):
	v = 0.019/time
	dx = 2 * (v**2) * math.sin(x) * math.cos(x) / 9.80609
	return dx

>>> getRange(0.234, 15)
-0.0006642788995856579
>>> def getRange(time, x):
	v = 0.019/time
	dx = 2 * (v**2) * math.sin(math.pi * x / 180) * math.cos(math.pi * x / 180) / 9.80609
	return dx

>>> getRange(0.234, 15)
0.00033616277221670414
>>> math.sin(math.pi * 15 / 180)
0.25881904510252074
>>> math.sin(math.pi * 30 / 180)
0.49999999999999994
>>> 0.019/0.234
0.08119658119658119
>>> def getRange(time, x):
	v = 0.019/time
	dx = (2 * (v**2) * math.sin(math.pi * x / 180) * math.cos(math.pi * x / 180)) / 9.80609
	return dx

>>> getRange(0.196, 45)
0.0009582949164669858
>>> getRange(0.0092, 15)
0.21747316582582535
>>> getRange(0.0094, 15)
0.20831743725099428
>>> getRange(0.0091, 15)
0.22227905754737173
>>> getRange(0.0092, 45)
0.4349463316516507
>>> getRange(0.0025, 45)
5.890217201759316
>>> getRange(0.0048, 30)
1.3837558947839783
>>> while True:
	x = input("Enter time: ")
	a = input("Enter angle: ")
	print(getRange(x, a))

	
Enter time: 0.0042
Enter angle: 15
Traceback (most recent call last):
  File "<pyshell#41>", line 4, in <module>
    print(getRange(x, a))
  File "<pyshell#18>", line 2, in getRange
    v = 0.019/time
TypeError: unsupported operand type(s) for /: 'float' and 'str'
>>> while True:
	x = float(input("Enter time: "))
	a = float(input("Enter angle: "))
	print(getRange(x, a))

	
Enter time: 0.0042
Enter angle: 15
1.0434766868196066
Enter time: 
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    x = float(input("Enter time: "))
ValueError: could not convert string to float: 
>>> while True:
	x = float(input("Enter time: "))
	a = float(input("Enter angle: "))
	print(100 * getRange(x, a))

	
Enter time: 0.0042
Enter angle: 30
180.7354638085196
Enter time: 0.0047
Enter angle: 45
166.65394980079546
Enter time: 0.0044
Enter angle: 45
190.15422268076296
Enter time: 0.0045
Enter angle: 45
181.7968272147937
Enter time: 0.0042
Enter angle: 45
208.69533736392137
Enter time: 0.0042
Enter angle: 60
180.73546380851963
Enter time: 0.0044
Enter angle: 30
164.67838747842382
Enter time: 0.0048
Enter angle: 30
138.37558947839784
Enter time: 0.0045
Enter angle: 45
181.7968272147937
Enter time: 0.0047
Enter angle: 45
166.65394980079546
Enter time: 0.0049
Enter angle: 60
132.7852387164634
Enter time: 0.0048
Enter angle: 60
138.37558947839787
Enter time: 0.0045
Enter angle: 75
90.89841360739683
Enter time: 0.0048
Enter angle: 75
79.89118383462613
Enter time: 0.0038
Enter angle: 0.0033
0.02936739576550813
Enter time: 0.0033
Enter angle: 45
338.0519514324677
Enter time: 0.0042
Enter angle: 15
104.34766868196066
Enter time: 0.0046
Enter angle: 30
150.66982899727245
Enter time: 0.0045
Enter angle: 45
181.7968272147937
Enter time: 0.0042
Enter angle: 60
180.73546380851963
Enter time: 0.0046
Enter angle: 60
150.6698289972725
Enter time: 0.0042
Enter angle: 60
180.73546380851963
Enter time: 0.0044
Enter angle: 75
95.07711134038148
Enter time: 0.0039
Enter angle: 15
121.01859799801356
Enter time: 0.0038
Enter angle: 30
220.7876441538979
Enter time: 0.0039
Enter angle: 45
242.0371959960272
Enter time: 0.0038
Enter angle: 60
220.78764415389793
Enter time: 0.0034
Enter angle: 15
159.22948750430677
Enter time: 0.0033
Enter angle: 30
292.7615777394202
Enter time: 0.0034
Enter angle: 45
318.45897500861355
Enter time: 0.0035
Enter angle: 60
260.25906788426823
Enter time: 0.003
Enter angle: 
Traceback (most recent call last):
  File "<pyshell#45>", line 3, in <module>
    a = float(input("Enter angle: "))
ValueError: could not convert string to float: 
>> while True:
	x = float(input("Enter time: "))
	a = float(input("Enter angle: "))
	print(100 * getRange(x, a))

	
Enter time: 0.0033
Enter angle: 75
169.02597571623383
Enter tim
