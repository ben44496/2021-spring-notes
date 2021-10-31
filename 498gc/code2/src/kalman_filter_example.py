#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:29:03 2020

@author: andres
"""
import numpy as np
from scipy.linalg import expm
import math
import matplotlib.pyplot as plt

# Kalman filter
# Author: Girish Chowdhary
#this file is intended to be a simple demonstration of a Kalman Filter for a linear system


#clear all
#close all

# parameters of the linear system: x_dot=Ax+Bu; y= Cx
# Students: Try different linear systems, try higher dimensional linear systems

A=np.array([[-1, -5], [6,-1]]) #np.array([[0, 1], [0, 0]]) # the system dynamics
B=np.array([[1, 0]]).T

x=np.array([[1,0]]).T #initial value of the state vector
u=0 #initial input
C=np.array([[0, 1]])

y=[] #declaring an empty array, its dimension is flexible
y.append((C@x)[0,0]) #filling out the array, this will be done during code

#integration parameters
dt=0.01
tf=10/dt
t=0

#This is a discrete implementation, so the following line makes the system discrete
# by taking the matrix exponential: Ad=expm(A*dt)
# so now our system becomes: x(k+1)=Ad*x_k+ Bd*u_k
Ad=expm(A*dt)


#noise parameters (Trey: you can change these and see how it affects the filter)
w=0.01 #process noise covariance
v=0.1 #measurement noise covariance
x_tilde=np.array([[0,0]]).T #This is where we initialize the state estimate, note how it is different from
               #the actual initial state (x=[1,0]), you can see how changing this affects the filter
x_hat=x_tilde #just setting the inital values

Q=np.eye(2,2)*w #Q matrix captures the process noise covariance
R= v #R matrix captuers the measurement noise covariance

P=np.eye(2,2)*1 #initial state error covariance matrix (P)



#storage variables
X_HAT_STORE= np.zeros((2,int(tf)))
X_STORE= np.zeros((2,int(tf)))
T_REC = np.zeros(int(tf))
Y = np.zeros(int(tf))


# main loop
U=[]
for k in range (1,int(tf)):
    
    #system intergration
    u=math.sin(0.01*k)*0.1 #Students: the input to the system can be changed here
                      #try changing the frequency to see how it affects
                      #the performance
    U.append(u)
    
    x=Ad@x+B*u+np.random.randn(2,1)*w #note the discrete propagation, and the addition of process noise
    y.append((C@x+np.random.randn(1)*v)[0,0]) #The measurement is simulated, and the measurement noise adds here

    t=t+dt
    
    #filter
    #prediction stage: This is where we make an a-priori prediction on what the system will do
    #we predict assuming that we know the A and B matrices
    x_tilde=Ad@x_hat+B*u
    y_tilde=C@x_tilde
    
    #we predict the error covariance here,
    P_tilde=Ad@P@Ad.transpose()+dt*Q
    
    #correction step, i.e. we use measurements to correct for any errors
    #K=P_tilde*C'*inv([C*P_tilde*C'+R]);
    K=P_tilde@C.T@np.linalg.inv(C@P_tilde@C.T+R) #this does the same thing as the line above better

    
    x_hat=x_tilde+K*(y[k-1]-y_tilde) #this is the "money" step, the actual correction to the estimate is applied here


    P=(np.eye(2,2)-K@C)@P_tilde #error covariance correction

    #store
    
    
    X_HAT_STORE[0,k-1] = x_hat[0,0]
    X_HAT_STORE[1,k-1] = x_hat[1,0]
    X_STORE[0,k-1] = x[0,0]
    X_STORE[1,k-1] = x[1,0]
    T_REC[k-1] = t
    Y[k-1]=y[k-1]
#end for    
plt.close('all')
plt.figure(1)
plt.plot(T_REC,Y,'*', T_REC, X_HAT_STORE[1,:],'.')
plt.legend(['real', 'estimated'])
plt.title('Output')
plt.xlabel('Time in unit time')
plt.ylabel('y')

fig, axs = plt.subplots(2)
axs[0].plot(T_REC,X_STORE[0,:],'*', T_REC, X_HAT_STORE[0,:],'.')
axs[0].set(ylabel = "x(1)")
axs[1].plot(T_REC,X_STORE[1,:],'*', T_REC, X_HAT_STORE[1,:],'.')
plt.xlabel('Time in unit time')
axs[1].set(ylabel = "x(2)")
axs[1].legend(['real', 'estimated'])