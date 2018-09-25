Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print In [1]: #!/usr/bin/env python3
   ...: #тут имя
   ...: # -*- coding: utf-8 -*-
   ...:
   ...: import math
   ...: #Из библиотеки math ,numpy,matplotlib.pyplot беру готовый код
   ...: import numpy
   ...: import matplotlib.pyplot as mpp
   ...:
   ...:
   ...: if __name__=='__main__':
   ...:     #ввожу параметры и задаю вид функции,в которую эты параметры будут подставлены.Затем запрашиваю график введенной функции.
   ...:     arguments = numpy.r_[0:200:0.1]
   ...:     mpp.plot(
   ...:         arguments,
   ...:         [math.sin(a) * math.sin(a/20.0) for a in arguments]
   ...:     )
   ...:     mpp.show()
