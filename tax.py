import numpy as np
import attr

SING = 1
MFJ = 2
MFA = 3
HOH = 4

@attr.s
class taxdata:
    brackets  = attr.ib(default = [ (0.0, 0.25)])
    deduction = attr.ib(default = 0)

def calctax(tdata, incomes):
    nn = np.vstack((np.copy(incomes)-tdata.deduction, np.zeros(np.size(incomes))))
    d = np.empty(nn[0,:].shape)
    for lim, mrate  in tdata.brackets:
        d = [ max(i - lim, 0.0) for i in nn[0,:]]
        nn[1,:] += d*mrate
        nn[0,:] -=d
    return nn[1,:]


crapola = taxdata(  brackets = [ (0.,0.1), (30000., 0.25), (100000., 0.33)],
                    deduction = 10000 )



