def calculate(a, b):
    J  = a + b
    Z = a * b
    return J, Z
re = calculate(3, 5)
print(re)


def send_sms(number, sms):
    print(f"{sms} was sent to {number}")
    
send_sms('0902', 'Fuckkkkkk Youuuuu!')