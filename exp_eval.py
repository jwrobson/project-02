from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '+', '-', '/', '*', '^']
    for a in input_str:
        if (valid.count(a) == 0):
            raise PostfixFormatException("Invalid Token")
    
    stack = Stack(30)
    counter = 0
    for x in input_str:            
            
        if((x == '+')or (x == '/') or (x == '-') or (x == '*') or (x == '^')): #Gets the two values to perform the operation
            
            if ((x == '-') and (counter == len(input_str) - 1)):
                stack.pop()
                s = stack.pop()
                val_1 = ''
                val_2 = ''
                while (s != ' '):
                    val_1 = s + val_1
                    s = stack.pop()
                s = stack.pop()
                while (s != ' '):
                    val_2 = s + val_2
                    if (stack.is_empty() == True):
                        break
                    else:
                        s = stack.pop()
                
                val_sum = float(val_2) - float(val_1)
                st_sum = str(val_sum)
                stack.push(' ')
                for t in st_sum:
                    stack.push(t)                 
                           
            elif (((x == '-') and (stack.is_empty == True)) or ((x == '-') and (input_str[counter+1] != ' '))):
                stack.push(x)
            else:    
                stack.pop()
                s = stack.pop()
                val_1 = ''
                val_2 = ''
                while (s != ' '):
                    val_1 = s + val_1
                    s = stack.pop()
                s = stack.pop()
                while (s != ' '):
                    val_2 = s + val_2
                    if (stack.is_empty() == True):
                        break
                    else:
                        s = stack.pop()            
            
                if (x == '+'):
                
                    val_sum = float(val_2) + float(val_1)
                    st_sum = str(val_sum)
                    stack.push(' ')
                    for t in st_sum:
                        stack.push(t)
                
                elif(x == '-'):
                
                    val_sum = float(val_2) - float(val_1)
                    st_sum = str(val_sum)
                    stack.push(' ')
                    for t in st_sum:
                        stack.push(t)                
                  
               
                elif(x == '*'):
                
                    val_sum = float(val_2) * float(val_1)
                    st_sum = str(val_sum)
                    stack.push(' ')
                    for t in st_sum:
                        stack.push(t) 
                    
                elif(x == '/'):
            
                    val_sum = float(val_2) / float(val_1)
                    st_sum = str(val_sum)
                    stack.push(' ')
                    for t in st_sum:
                        stack.push(t) 
                
                elif(x == '^'):
                
                    val_sum = float(val_2) ** float(val_1)
                    st_sum = str(val_sum)
                    stack.push(' ')
                    for t in st_sum:
                        stack.push(t)
                    
        else:    
            stack.push(x)
        
        counter = counter + 1
        
    result = ''
    r = stack.pop()
    while (stack.is_empty() == False):
        result = r + result
        r = stack.pop()
    result = r + result
    return float(result)
    

def infix_to_postfix(input_str):
    
    '''Converts an infix expression to an equivalent postfix expression
    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    
    result = '' #Creating an empty result string
    
    stack_vals = Stack(30)
    counter = 0
    masko = True
    for x in input_str:
        
        #------------reveals current entire value-------------
        if (x == ' '):
            val = ''
            r = counter - 1 
            while ( (r >= 0) and (input_str[r] != ' ') ):
                val = input_str[r] + val
                r = r - 1
            #Now that the value has been found as val it will be processed
            
            if (val == '('):
                masko = False
                stack_vals.push(val)
                
            elif (val == ')'):
                while (stack_vals.peek() != '('):
                    op = stack_vals.pop()
                    result = result + ' ' + op
                stack_vals.pop()
                
            elif (val == '+'):
                while (stack_vals.is_empty() == False):
                    peek = stack_vals.peek()
                    if ((peek == '+') or (peek == '-') or (peek == '*') or (peek == '/') or (peek == '^')):
                        higher = stack_vals.pop()
                        result = result + ' ' + higher
                    else:
                        break
                stack_vals.push(val)
                        
            elif (val == '-'):
                while (stack_vals.is_empty() == False):
                    peek = stack_vals.peek()
                    if ((peek == '+') or (peek == '-') or (peek == '*') or (peek == '/') or (peek == '^')):
                        higher = stack_vals.pop()
                        result = result + ' ' + higher
                    else:
                        break
                stack_vals.push(val)
                
            elif (val == '*'):
                while (stack_vals.is_empty() == False):
                    peek = stack_vals.peek()
                    if ((peek == '*') or (peek == '/') or (peek == '^')):
                        higher = stack_vals.pop()
                        result = result + ' ' + higher
                    else:
                        break
                stack_vals.push(val)
                
            elif (val == '/'):
                while (stack_vals.is_empty() == False):
                    peek = stack_vals.peek()
                    if ((peek == '*') or (peek == '/') or (peek == '^')):
                        higher = stack_vals.pop()
                        result = result + ' ' + higher
                    else:
                        break
                stack_vals.push(val)
                
            elif (val == '^'):
                stack_vals.push(val)
                
            else:
                result = result + ' ' + val
            
        #This next entire section is dedicated entirely to the last value in the string. Couldn't make it work with above    
        elif (counter == len(input_str) - 1):
            val = ''
            r = counter
            while ( (r >= 0) and (input_str[r] != ' ') ):
                val = input_str[r] + val
                r = r - 1
            result = result + ' ' + val
            while (stack_vals.is_empty() == False):
                result = result + ' ' + stack_vals.pop()
            
                
                
                
        counter = counter + 1
    return result[1:]


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    stack_vals = Stack(30)
    rev = len(input_str) - 1
    for x in input_str:
        c = input_str[rev]
        
        #Seperates values through spaces
        if (c == ' '):
            val = ''
            r = rev + 1 
            while ( (r <= len(input_str) - 1) and (input_str[r] != ' ') ):
                val = val + input_str[r]
                r = r + 1
                
            if ( (val == '+') or (val == '-') or (val == '*') or (val == '/') or (val == '^') ):

                st1 = stack_vals.pop()
                st2 = stack_vals.pop()
                op = st1 + ' ' + st2 + ' ' + val
                stack_vals.push(op)
                
            else:
                stack_vals.push(val)
                
                
        #Specifically Addresses the final value in the string
        if (rev == 0):
            val = ''
            r = rev
            while (input_str[r] != ' '):
                val = val + input_str[r]
                r = r + 1
            
            if ( (val == '+') or (val == '-') or (val == '*') or (val == '/') or (val == '^') ):
    
                st1 = stack_vals.pop()
                st2 = stack_vals.pop()
                op = st1 + ' ' + st2 + ' ' + val
                stack_vals.push(op)
                    
            else:
                stack_vals.push(val)
                    
        rev = rev - 1
        
        
    result = stack_vals.pop()
    
    return result


