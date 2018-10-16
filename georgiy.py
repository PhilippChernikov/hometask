
#!/usr/bin/env python3
        #тут имя
    # -*- coding: utf-8 -*-
   
import math
        #Из библиотеки math ,numpy,matplotlib.pyplot беру готовый код
import numpy
import matplotlib.pyplot as mpp
   
   
if __name__=='__main__':
          #ввожу параметры и задаю вид функции,в которую эты параметры будут подставлены.Затем запрашиваю график введенной функции.
        arguments = numpy.r_[0:200:0.1]
        mpp.plot(
            arguments,
            [math.sin(a) * math.sin(a/20.0) for a in arguments]
        )
        mpp.show()
   
