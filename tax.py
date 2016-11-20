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
    dr = np.zeros(nn[0,:].shape)
    for lim, mrate  in tdata.brackets:
        dr = np.array([ max(i - lim, 0.0) for i in nn[0,:]])
        nn[1,:] += dr*mrate
        nn[0,:] -= dr
    return nn[1,:]


simple_sample = taxdata(  brackets = [ (0.,0.1), (30000., 0.25), (100000., 0.33)],
                    deduction = 10000 )



us2016 = taxdata(deduction=12600., 
                 brackets = [ 
                     (466950., 0.396), (413350., 0.35),
                     (231450., 0.33), (151900., 0.28),
                     (75300., 0.25), (18550., 0.15), (0, 0.1)])

trump = taxdata(deduction=30000.,
            brackets = [
                (225000., 0.33), (75000., 0.25), (0., 0.12) ])


