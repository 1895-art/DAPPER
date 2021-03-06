# Settings not taken from anywhere

import dapper as dpr

from dapper.mods.DoublePendulum import step, x0, LP_setup, dstep_dx

t = dpr.Chronology(0.01, dkObs=100, T=30, BurnIn=10)

Dyn = {
    'M': len(x0),
    'model': step,
    'noise': 0,
    'linear': dstep_dx,
}

X0 = dpr.GaussRV(mu=x0, C=0.01**2)

jj = [0, 2]
Obs = dpr.partial_Id_Obs(len(x0), jj)
Obs['noise'] = 0.1**2

HMM = dpr.HiddenMarkovModel(Dyn, Obs, t, X0, LP=LP_setup(jj))

####################
# Suggested tuning
####################
# from dapper.mods.DoublePendulum.settings101 import HMM # Expct rmse.a:

# HMM.t.dkObs = anything
# xps += Climatology()                                 # 5
# xps += OptInterp()                                   # 2.5

# HMM.t.dkObs = 7 # <-- max dkObs for tolerable performance with Var3D
# xps += Var3D(xB=0.1)                                 # 0.81

# HMM.t.dkObs = 10
# xps += ExtKF(infl=2)                                 # 0.12
# xps += EnKF('Sqrt', N=3  ,infl=1.03,rot=True)        # 0.12
# xps += EnKF('Sqrt', N=5  ,infl=1.01,rot=True)        # 0.10
# xps += PartFilt(    N=40  ,reg=1.0,NER=0.9)          # 0.12

# HMM.t.dkObs = 20 # <-- max dkObs for tolerable performance with ExtKF
# xps += ExtKF(infl=3)                                 # 0.18
# xps += EnKF('Sqrt', N=20 ,infl=1.02,rot=True)        # 0.15
# xps += PartFilt(    N=100  ,reg=1.0,NER=0.9)         # 0.13
# xps += PartFilt(    N=400  ,reg=1.0,NER=0.9)         # 0.12
# xps += PartFilt(    N=1000 ,reg=1.0,NER=0.9)         # 0.11

# HMM.t.dkObs = 30 # <-- for larger dkObs, EnKF deteriorates quickly
# xps += EnKF('Sqrt', N=20 ,infl=1.01,rot=True)        # 0.17
# xps += PartFilt(    N=100  ,reg=1.0,NER=0.9)         # 0.14
# xps += PartFilt(    N=400  ,reg=1.0,NER=0.9)         # 0.13
# xps += PartFilt(    N=1000 ,reg=1.0,NER=0.9)         # 0.12

# HMM.t.dkObs = 60
# xps += EnKF( 'Sqrt',N=20      ,infl=1.01,rot=True)   # 0.41
# xps += iEnKS('Sqrt',N=10,Lag=2,infl=1.01,rot=True)   # 0.14
# xps += PartFilt(    N=400  ,reg=1.0,NER=0.9)         # 0.15

# HMM.t.dkObs=100
# xps += EnKF('Sqrt', N=40,rot=True,infl=1.01)         # 1.9
# xps += iEnKS('Sqrt',N=10,Lag=1,infl=1.01,rot=True)   # 0.19
# xps += PartFilt(    N=400  ,reg=2.0,NER=0.9)         # 0.23
# xps += PartFilt(    N=1000 ,reg=1.0,NER=0.9)         # 0.19

# TODO 7: implement cartesian obs
