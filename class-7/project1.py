import time

print("Welcome To My Calculator")
time.sleep(0.5)

num_1 = int(input('Enter a number: '))
time.sleep(2)
operator = input('Enter an operator: ')
time.sleep(2)
num_2 = int(input('Enter another number: '))

def add(num_1:int, opreator:str, num_2:int):
    if(opreator == '+'):
        cal = num_1 + num_2
    elif(opreator == '-'):
        cal = num_1 - num_2
    elif(opreator == '*'):
        cal = num_1 * num_2
    elif(opreator == '/'):
        cal = num_1 / num_2
    else:
        print('Invalid Operator')   
    return cal

result = add(num_1, operator, num_2)
time.sleep(2)
print(f"Your result is {result}")