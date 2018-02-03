from complexArray import *

def bode_plot(t, omega):
    orderNum = len(t.num)
    orderDenom = len(t.denom)
    s = complexArray(np.zeros(len(omega)),omega)
    #print s.getArg()
    sumNum = complexArray(np.zeros(len(omega)),np.zeros(len(omega)))
    sumDenom = complexArray(np.zeros(len(omega)),np.zeros(len(omega)))
    for j in range(orderNum):
        sumNum = sumNum.add(s.pow(j).scalarMultiply(t.num[j]) )
    for j in range(orderDenom):
        sumDenom = sumDenom.add(s.pow(j).scalarMultiply(t.denom[j]) )
            
    mag = 20*np.log(np.divide(sumNum.getAbs(),sumDenom.getAbs()))/(np.log(10))
    
    phase = np.subtract(sumNum.getArg(),sumDenom.getArg())*360/(2*np.pi)
    
    index = 0
    indexArray = np.zeros(len(phase))
    for j in range(1,len(phase)):
        #print phase[j], phase[j-1]
        if phase[j] - phase[j-1] > 180.0:
            index = index-1    
        if phase[j] - phase[j-1] < -180.0:
            index=index+1
        indexArray[j] = index
        
    for j in range(1,len(phase)):
        phase[j]=phase[j]+indexArray[j]*360.0
    
    #OR
    #phase = (sumNum.divide(sumDenom)).getArg()*360/(2*np.pi)
    
    return mag,phase

