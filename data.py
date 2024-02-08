def calculate(a, b):
    J  = a + b
    Z = a * b
    return J, Z
re = calculate(3, 5)
print(re)


def send_sms(number, sms):
    print(f"{sms} was sent to {number}")
    
send_sms('0902', 'Fuckkkkkk Youuuuu!')



def save_ph_number(*number):
    phone_numbers = []
    phone_numbers.append(number)
    print(f'The list of phone numbers is {phone_numbers}')
    
save_ph_number('0912', '0991')



def get_remainder(a, b):
    print(f'The remainder of these two nums is : ({a % b})')
    
get_remainder(10, 2)



def get_division(a, b):
    print(f'The division of these two nums is : ({a / b})')
    
get_division(120, 20)