# -*- coding: utf-8 -*-
"""Question_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K-SmX-4ox0krTCrogZs9AxhnVJffED79
"""

import numpy as np
class X:
  z={}
  def __init__(self,arr,target):
    self.arr=arr
    self.target=target

  def f1(self):
    k=1
    a = self.arr
    t = self.target
    for i in range(len(a)):
      for j in range(len(a)):
        if i!=j and (a[i]+a[j]) == t:
          self.z[k]=[i,j]
          k=k+1
    print(self.z)


x2=input()
y=int(input())
x1=x2.split()
for i in range(len(x1)):
  x1[i]=int(x1[i])
x=np.array(x1)
c=X(x,y)
z = c.f1()