import numpy as np
import attr

SING = 1
MFJ = 2
MFA = 3
HOH = 4

@attr.s
class taxdata:
    tclass = attr.ib(default = SING)
    brackets  = attr.ib(default = [ (0.0, 0.25)])
    deduction = attr.ib(default = 0)

def calctax(tdata, incomes):
    nn = np.vstack((np.copy(incomes)-tdata.deduction, np.zeros(np.size(incomes))))
    for lim, mrate  in tdata.brackets:
        d = np.max( np.vstack( (nn[0,:] -lim, np.zeros_like(nn[0:]))), axis=0)
        nn[1,:] += d*mrate
        nn[0,:] -=d
    return nn[1,:]


crapola = taxdata(  tclass=SING,
                    brackets = [ (0.,0.1), (30000., 0.25), (100000., 0.33)],
                    deduction = 10000 )



