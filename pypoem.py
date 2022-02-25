#just run your code with this function its literally one more step 
def poem(filename):
    print('running file')
    
    with open(filename, 'r') as file:
        code = file.read()
    try:
        exec(code)
    except NameError as err:
        var = str(err).replace("name '", '').replace("' is not defined", '')
        #print(var)
        poem ='''
Roses are red
Violets are blue
unknown var {a}
good luck to u'''.format(a=var)
        print(poem)
    except TypeError as err:
        err = str(err).replace('unsupported operand type(s) for', '').replace(": '"," ").replace("' and '"," ").replace("'",'').split(' ')
        err.remove("")
      
        op = err[0]
        a = err[1]
        b = err[2]
        

        poem = '''
There once was a man
who thought you could {op} an
{a} and {b} but alas
that is a unsupported operand type'''.format(a=a, b=b, op=op)
        print(poem)


poem(str(input('what is the file name:')))
