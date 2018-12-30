import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

plt.close()
rho = 1000
g = 9.87
kv = 1
ku = 0.01
T = np.arange(0,10000,1)
x0 = np.array([1,0])
u = np.arange(0,10000,1)

a = np.array([[-kv/(2*np.sqrt(rho*g)),0],[0,1]])
b = np.array([[ku],[0]])
c = np.array([[1,0]])
d = np.array([[0]])

sys = ctrl.StateSpace(a, b, c, d)

T, yout, xout = ctrl.forced_response(sys,T,u,x0)

ctrl.bode_plot(sys)
plt.plot(T,yout,T,u)
plt.show()
