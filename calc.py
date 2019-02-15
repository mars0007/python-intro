# write a simple calc that handles + - * /, handle invalid input

while True:

    in_put = input('enter an equestion or "exit" to quit: ')
    if in_put=='exit': break
    in_put_clean = in_put.replace(" ","")
    operator_1 = ''
    parameter_1 = ''
    parameter_2 = ''
    operators = ['+','-','/','*']
    first_number = True
    for d in in_put_clean:
        if d.isdigit() and first_number:
            parameter_1=parameter_1+d
        elif d in operators:
                operator_1 = str(d)
                first_number = False
        elif d.isdigit() and not first_number:
            parameter_2 = parameter_2+d
        else:
            print('the fuck...')    

    val = 0

    if operator_1 == '+':
        try:
            val = int(parameter_1)+int(parameter_2)
        except TypeError:
            print('oops, cannot add these two things, try again...')
            continue
        except:
            print('oops, something went wrong, try again...')
            continue
    elif operator_1 == '-':
        try:
            val = int(parameter_1)-int(parameter_2)
        except:
            print('oops, something went wrong, try again...')            
            continue
    elif operator_1 == '/':
        try:
            val = int(parameter_1)/int(parameter_2)
        except:
            print('oops, something went wrong, try again...')            
            continue
    elif operator_1 == '*':
        try:
            val = int(parameter_1)*int(parameter_2)
        except:
            print('oops, something went wrong, try again...')
            continue            
    else:
        print('that not a supported operator, please try again with - + / and *')
        continue     
    
    print('the equasion is {0} {1} {2} = {3}'.format(parameter_1,operator_1,parameter_2,val))
    
 
    