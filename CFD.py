import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import researchpy as rp

PD = pd.read_excel(r'/Users/macbookpro/Desktop/Data CFD.xlsx', sheet_name='PD')
V = pd.read_excel(r'/Users/macbookpro/Desktop/Data CFD.xlsx', sheet_name='V')
fonttype = {'fontname': 'Times New Roman'}
fig = plt.figure(figsize=(10,6))
ax1 = plt.axes()
ax1.plot(V['I 1 medium'], V[' V 1 medium'], marker='+', color = 'blue',linewidth=0.5)
ax1.plot(V['I 2 medium'], V[' V 2 medium'], marker='+', color = 'red',linewidth=0.5)
ax1.plot(V['I 1 fine'], V['V 1 fine'], marker='.', color = 'blue',linewidth=0.5)
ax1.plot(V['I 2 fine'], V['V 2 fine'], marker='.', color = 'red',linewidth=0.5)
ax1.plot(V['I 1 coarse'], V['V 1 coarse'], marker='x', color = 'blue',linewidth=0.5)
ax1.plot(V['I 2 coarse'], V['V 2 coarse'], marker='x', color = 'red',linewidth=0.5)
plt.rcParams['figure.dpi'] = 1000
ax1.set_xlim([-0.0105, 0.0105])
ax1.set_ylim([-0.2, 0.025])
ax1.set_title('Velocity', fontsize=12, **fonttype, weight="bold")
ax1.set_ylabel('Velocity [j] (m/s)', fontsize=12, **fonttype)
ax1.set_xlabel('Position [X] (m)', fontsize=12, **fonttype)
ax1.legend(['1st order Medium','2nd order Medium','1st order Fine','2nd order Fine', '1st order Coarse','2nd order Coarse'],
    loc='upper left',bbox_to_anchor=(1.05, 1), borderaxespad=0., prop={"size": 12, "family": 'Times New Roman'})
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.tight_layout(pad=0.2)
#plt.savefig('V.png')

fig = plt.figure(figsize=(10,6))
ax1 = plt.axes()
ax1.plot(V['I 2 medium'], V[' V 2 medium'], marker='+', color = 'blue',linewidth=0.5)
ax1.plot(V['I 2 initial'], V['V 2 initial'], marker='.', color = 'orange',linewidth=0.5)
plt.rcParams['figure.dpi'] = 1000
ax1.set_xlim([-0.0105, 0.0105])
ax1.set_ylim([-0.2, 0.025])
ax1.set_title('Velocity', fontsize=12, **fonttype, weight="bold")
ax1.set_ylabel('Velocity [j] (m/s)', fontsize=12, **fonttype)
ax1.set_xlabel('Position [X] (m)', fontsize=12, **fonttype)
ax1.legend(['2nd order Medium','2nd order Initial'],
    loc='upper left',bbox_to_anchor=(1.05, 1), borderaxespad=0., prop={"size": 12, "family": 'Times New Roman'})
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.tight_layout(pad=0.2)
plt.savefig('V2.png')

fig = plt.figure(figsize=(10,6))
ax1 = plt.axes()
ax1.plot(PD['I 2 medium'], PD[' PD 2 medium'], marker='+', color = 'blue',linewidth=0.5)
ax1.plot(PD['I 2 initial'], PD['PD 2 initial'], marker='.', color = 'orange',linewidth=0.5)
plt.rcParams['figure.dpi'] = 1000
ax1.set_xlim([2, 40])
ax1.set_ylim([-10, 60])
ax1.set_title('Pressure Drop', fontsize=12, **fonttype, weight="bold")
ax1.set_ylabel('Pressure (Pa)', fontsize=12, **fonttype)
ax1.set_xlabel('Iteration', fontsize=12, **fonttype)
ax1.legend(['2nd order Medium','2nd order Initial'],
    loc='upper left',bbox_to_anchor=(1.05, 1), borderaxespad=0., prop={"size": 12, "family": 'Times New Roman'})
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.tight_layout(pad=0.2)
plt.savefig('PD2.png')

WSS = pd.read_excel(r'/Users/macbookpro/Desktop/Data CFD.xlsx', sheet_name='WSS')
fonttype = {'fontname': 'Times New Roman'}
fig = plt.figure(figsize=(10,6))
ax1 = plt.axes()
ax1.plot(WSS['I 1 medium'], WSS['WSS 1 medium'], marker='+', color = 'blue',linewidth=0.5)
ax1.plot(WSS['I 2 medium'], WSS[' WSS 2 medium'], marker='+', color = 'red',linewidth=0.5)
ax1.plot(WSS['I 1 fine'], WSS['WSS 1 fine'], marker='.', color = 'blue',linewidth=0.5)
ax1.plot(WSS['I 2 fine'], WSS['WSS 2 fine'], marker='.', color = 'red',linewidth=0.5)
ax1.plot(WSS['I 1 coarse'], WSS['WSS 1 coarse'], marker='x', color = 'blue',linewidth=0.5)
ax1.plot(WSS['I 2 coarse'], WSS['WSS 2 coarse'], marker='x', color = 'red',linewidth=0.5)
plt.rcParams['figure.dpi'] = 1000
ax1.set_xlim([0,80])
ax1.set_ylim([-0.15,0.01])
ax1.set_title('Wall Shear Stress (y-component)', fontsize=12, **fonttype, weight="bold")
ax1.set_ylabel('WSS', fontsize=12, **fonttype)
ax1.set_xlabel('Iteration', fontsize=12, **fonttype)
ax1.legend(['1st order Medium','2nd order Medium','1st order Fine','2nd order Fine', '1st order Coarse','2nd order Coarse'],
    loc='upper left',bbox_to_anchor=(1.05, 1), borderaxespad=0., prop={"size": 12, "family": 'Times New Roman'})
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.tight_layout(pad=0.2)
#plt.savefig('WSS.png')


fonttype = {'fontname': 'Times New Roman'}
fig = plt.figure(figsize=(10,6))
ax1 = plt.axes()
ax1.plot(PD['I 1 medium'], PD[' PD 1 medium'], marker='+', color = 'blue',linewidth=0.5)
ax1.plot(PD['I 2 medium'], PD[' PD 2 medium'], marker='+', color = 'red',linewidth=0.5)
ax1.plot(PD['I 1 fine'], PD['PD 1 fine'], marker='.', color = 'blue',linewidth=0.5)
ax1.plot(PD['I 2 fine'], PD['PD 2 fine'], marker='.', color = 'red',linewidth=0.5)
ax1.plot(PD['I 1 coarse'], PD['PD 1 coarse'], marker='x', color = 'blue',linewidth=0.5)
ax1.plot(PD['I 2 coarse'], PD['PD 2 coarse'], marker='x', color = 'red',linewidth=0.5)
plt.rcParams['figure.dpi'] = 1000
ax1.set_xlim([0, 60])
ax1.set_ylim([-10, 60])
ax1.set_title('Pressure Drop', fontsize=12, **fonttype, weight="bold")
ax1.set_ylabel('Pressure (Pa)', fontsize=12, **fonttype)
ax1.set_xlabel('Iteration', fontsize=12, **fonttype)
ax1.legend(['1st order Medium','2nd order Medium','1st order Fine','2nd order Fine', '1st order Coarse','2nd order Coarse'],
    loc='upper left',bbox_to_anchor=(1.05, 1), borderaxespad=0., prop={"size": 12, "family": 'Times New Roman'})
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.tight_layout(pad=0.2)
#plt.savefig('PD.png')