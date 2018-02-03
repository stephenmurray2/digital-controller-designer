#!/usr/bin/env python
import numpy as np

# define a complex array class, whose attrubutes are arrays 
class complexArray:
    def __init__(self, realArray, imagArray):
        # it would be good practice to ensure these lengths are the same length. YOLO
        self.real = realArray
        self.imag = imagArray
        
    def add(self, other):
        return complexArray(np.add(self.real, other.real),np.add(self.imag, other.imag) )
    
    def subtract(self, other):
        return complexArray(np.subtract(self.real, other.real),np.subtract(self.imag, other.imag) )
    
    def multiply(self, other):
        return complexArray(np.subtract(np.multiply(self.real, other.real),np.multiply(self.imag,other.imag)),\
                            np.add(np.multiply(self.real, other.imag), np.multiply(self.imag,other.real)))
    
    def divide(self, other):
        c = np.divide(1.0, np.subtract( np.power(other.real,2.0), np.power(other.imag,2.0) ) )
        print c
        return self.multiply( other.conjugate() ).scalarArrayMultiply(c)
    
    def scalarMultiply(self,c):
        return complexArray(c*(self.real),c*(self.imag) )
    
    def scalarArrayMultiply(self,c):
        return complexArray(np.multiply(c,self.real),np.multiply(c,self.imag) )
    
    def conjugate(self):
        return complexArray(self.real,np.subtract(0,self.imag))
    
    def pow(self,p):
        if p == 0:
            return complexArray(np.ones(len(self.real)),np.zeros( len(self.imag) ) ) 
        if p == 1:
            return self
        if p >= 2:
            temp = self
            for i in range(1,p):
                temp = self.multiply(temp)
            return temp
        
    def getAbs(self):
        return np.sqrt(np.add(np.multiply(self.real,self.real),np.multiply(self.imag,self.imag)))

    def getArg(self):
        return np.arctan2( self.imag, self.real )