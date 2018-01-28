#!/usr/bin/env python
#6位随机验证码

def r_code():
    code = ''
    for i in range(6):
        add = str(random.choice([random.randrange(10),chr(random.randint(65,90))]))
        code += add
    print(code)

if __name__ == '__main__':
    r_code()
