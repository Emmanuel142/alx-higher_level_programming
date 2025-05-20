This is the test for basegeometry
_________________________________
_________________________________
>>> base_geometry = __import__('7-base_geometry').BaseGeometry

>>> my_base = base_geometry()
>>> my_base.area()
Traceback (most recent call last):
	...
Exception: area() is not implemented
>>> my_base.integer_validator("Triangle", 76)
>>> my_base.integer_validator("Rectangle", 0)
Traceback (most recent call last):
	...
ValueError: Rectangle must be greater than 0
>>> my_base.integer_validator("Square", "a")
Traceback (most recent call last):
	...
TypeError: Square must be an integer
