import time

Employer = {'baoyu': lambda x,y:8*(x+y),\
            'jiamu': lambda x,y:10*max(x,y),\
            'wangfuren': lambda x,y:5*min(x,y),\
            'jiazheng': lambda x,y:4*x+2*y}

Employee = {'qingwen': ([900,800,900,800,900,800,900,800,900,800,900,800],\
                        [500,500,500,500,500,500,500,500,500,500,500,500]),\
            'sheyue': ([600,600,600,600,600,600,600,600,600,600,600,600],\
                       [400,400,400,400,400,400,700,700,700,700,700,700]),\
            'xiren': ([1000,1000,1000,1500,1500,1500,1000,1000,1000,1500,1500,1500],\
                      [2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000])}


def calc_cur_mon_salary(master, slave):
    cur_mon = time.localtime().tm_mon
    factors = acquire_factors(slave, cur_mon)
    return Employer[master](factors[0], factors[1])


def acquire_factors(slave, mon):
    base = Employee[slave][0][mon-1]
    bonus = Employee[slave][1][mon-1]
    return base, bonus

