#!/usr/bin/env python

# This python script has been developed for students in the 4P03
# composite laboratory at McMaster University. Given a plant transfer
# function, this algorithm gives the parameters for a PD controller 
# 
# 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from numpy import *
from complexArray import *
from tf import *
import math
import bodeplot
import getIndex
                
# assumes that the input array is initially positive and monotonically decreasing 
def getCF(seq):
    i = 0
    while (seq[i] > 0):
        i = i+1
    return seq[i]

# get the desired crossover frequency
def getDCF(PO,ts):
    PM = 2920.0/(PO + 40.0)
    wc = (840.0/(ts*PM)) - (8.7/ts)
    return PM,wc


# constructs arrays for magnitude and phase from a transfer function object



omega = pow(10,np.linspace(-3,3,601))

# declare a transfer function
t = tf(np.zeros(5),np.zeros(5))

# part 1 of controller design procedure in lab
t.num[0] = 4900000
t.denom[1] = 4900
t.denom[2] = 140
t.denom[3] = 1
# the parameters for the dynamic accuracy of the controller
PO = 3
ts = 0.11

#get the magnitude and phase numpy arrays from the bode_plot function
mag, phase = bodeplot.bode_plot(t,omega)

#get the crossover frequency
#cf = getCF(mag)

# PD controller design procedure

# get the desired values of the phase margin and crossover frequency
PMd, wcd = getDCF(PO,ts)

print "the desired phase margin and crossover frequency are", PMd, wcd

dBshift = -mag[getIndex.getIndex(omega,wcd)]

Kp = np.power(10.0,dBshift/20.0)
print "Kp is", Kp
    
PMnew = phase[getIndex.getIndex(omega,wcd)]+180

PhiPD = PMd + 5.0 - PMnew
tau = np.power(10.0,(PhiPD-45.0)/45.0)/wcd

Kd = tau*Kp

print "Kd is", Kd

tauf = 1.0/(10*wcd)

print "tau_f is", tauf

print ""

# plot the magnitude
fig_bode = plt.figure(1)
ax_mag = fig_bode.add_subplot(211)
ax_mag.plot(omega,mag,color="blue",ls='-',lw=2.0)
ax_mag.grid(True,which="both",ls=":",lw=2,color="grey")
ax_mag.set_xscale('log')
ax_mag.set_xlim([0.1,1000])
#ax_mag.set_xlabel('frequency (rad/sec)', fontsize=12)
ax_mag.set_ylabel('magnitude (dB)', fontsize=12)
ax_mag.grid(color='grey',ls=':',lw=2.0)
ax_mag.set_axisbelow(True)

# plot the phase 
ax_phase = fig_bode.add_subplot(212)
#ax_phase.set_position([0.17,0.155,0.8,0.79])
ax_phase.plot(omega,phase,color="blue",ls='-',lw=2.0)
extraticks=[-180]
#ax_phase.set_yticks(list(ax_phase.get_yticks()[0]) + extraticks)
ax_phase.set_yticks([0,-30,-60,-90,-120,-150,-180])
ax_phase.set_xlim([0.1,1000])
ax_phase.set_xscale('log')
#s = (ax_phase.get_gridlines)[0].ls
ax_phase.grid(True,which="both",ls=":",lw=2,color="grey")
ax_phase.tick_params(axis='y',which='minor',bottom='on')
ax_phase.set_xlabel('frequency (rad/sec)', fontsize=12)
ax_phase.set_ylabel('phase (degrees)', fontsize=12)
ax_phase.set_ylim([-200,0])
ax_phase.grid(color='grey',ls=':',lw=2.0)
ax_phase.set_axisbelow(True)

pp = PdfPages("bodeplot" +".pdf")
fig_bode.savefig(pp, format='pdf')
pp.close()





