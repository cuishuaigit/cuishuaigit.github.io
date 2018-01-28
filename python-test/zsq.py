#!/usr/bin/env python

#装饰器

import time
import random

def logger(flag):
    def show_time(f):
        def change(*args,**kwargs):
            start = time.time()
            f(*args,**kwargs)
            end = time.time()
            print("execute time:{}".format(start-end))
            if flag == 'true':
                with open('/data/logs/out.log','ab+') as f:
                    f.write('rslog')
        return change
    return shoe_time

@logger('false')
def r_code():
    code = ''
    for i in range(6):
        add = str(random.choice([random.randrange(10),random.randint(65,90)]))
        code += add
    print(code)

if __name__ == '__main__':
    r_code()
