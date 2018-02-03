import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from numpy import *
from complexArray import *
from tf import *
import math
import bodeplot
import getIndex

# evaluation of coefficients for PDD^2 controller
# def getPDD2coeffs(omega,mag):

t = tf(np.zeros(5),np.zeros(5))
omega = pow(10,np.linspace(-3,3,601))

# construct the relationship between peak/K and damping ratio
zeta = np.arange(0.1,0.3,0.01)
ratio = np.zeros(len(zeta))

# print ratio
ratio = np.array([ 5., 4.55264152 , 4.18731832,  3.8754111   ,3.60616055 , 3.37147825 , 3.16517658 , 2.98244732 , 2.81950111 , 2.67800775 , 2.55102185 , 2.43525488 ,2.32931715 , 2.23203395 , 2.14511088 , 2.06551933 , 1.99141973,  1.92228309, 1.85969831,  1.80155687])
#redefine omega
#omega = pow(10,np.linspace(0,3,301))

xi_in = 0.26
K_in = 1000
w_d_in = 20
    
w_n_in = w_d_in/np.sqrt(1-np.power(xi_in,2.0))
t.num[0] = K_in*np.power(w_n_in,2.0)
t.denom[0] = np.power(w_n_in,2.0)
t.denom[1] = 2*xi_in*w_n_in
t.denom[2] = 1

mag2, phase2 = bodeplot.bode_plot(t,omega)

mag2 = np.power(10,np.divide(mag2,20))    
K = mag2[0]
peak_mag = max(mag2)
omega_d = omega[np.argmax(mag2)]
xi = zeta[getIndex.getIndex(ratio,peak_mag/K)]
omega_n = omega_d/np.sqrt(1-np.power(xi,2.0))
print "xi is", xi
print "K is", K
print "omega_n is", omega_n
tau_f = 1/(10*omega_n)
#    return {'K':K, 'omega_n':omega_n,'xi':xi,'tau_f':tau_f}
print "assuming PDD2 controller"

print "numerator", 1, 2*xi*omega_n, np.power(omega_n,2.0)
print "denominator", K/100, (K/5)*omega_n, K*np.power(omega_n,2.0)

fig_pdd2 = plt.figure()
ax_pdd2 = fig_pdd2.add_subplot(111)
ax_pdd2.plot(omega,mag2,color="blue",ls='-',lw=2.0)
ax_pdd2.grid(True,which="both",ls=":",lw=2,color="grey")
ax_pdd2.set_xscale('log')
#ax_mag.set_xlabel('frequency (rad/sec)', fontsize=12)
ax_pdd2.set_ylabel('magnitude', fontsize=12)
ax_pdd2.set_yticks([0,200,400,600,800,1000,1200,1400,1600,1800,2000])
ax_pdd2.grid(color='grey',ls=':',lw=2.0)
ax_pdd2.set_axisbelow(True)

pp = PdfPages("pdd2.pdf")
fig_pdd2.savefig(pp, format='pdf')
pp.close()
