import ast
#Lexical Analysis Assignment COMP 3050
#Brenden Henry

#Gets token number for each 'Operator'
def getoptoken(var):
  if var == '+':
    return('7')
  elif var == '-':
    return('47')
  elif var == '*':
    return('37')
  elif var == '/':
    return('27')
  elif var == '(':
    return('17')
  elif var == ')':
    return('67')

#Classifies Identities, 'Operators', and Literal Ints. and returns the token number.
def gettoken(var, ID, OP, IL):
  token = var
  tokenlist = []
  i = ID
  o = OP
  il = IL
  if token in i:
    return '11'
  elif token in o:
    return(getoptoken(token))
  elif token.isdigit():
    return '13'
  else:
    return('Error')

#Used to find and test the type of the lexemes
def identifier(equation):
  equ = equation
  for i in equ:
    print(type(i))

#Used to break up the Identities
def anlexid(equation):
  list1 = equation
  variables = [
    node.id for node in ast.walk(ast.parse(list1)) 
    if isinstance(node, ast.Name)]
  return variables


# Used to identify and convert numbers into actual floats
def numconverter(equation):
  list1 = equation
  numlist = []
  for value in list1:
    try:
      numlist.append(float(value))
    except ValueError:
      continue
  return numlist

#Creates a INT list of INT_LIT
def numconverter2(equation):
  list1 = equation
  numlist = []
  for value in list1:
    try:
      numlist.append(int(value))
    except ValueError:
      continue
  return numlist

#Used to identify and make a list of 'Operators'
def operatorid(equation):
  list1 = equation
  tokenlist = []
  oplist = []

  for i in list1:
    if i == '+':
      oplist.append(i)
      tokenlist.append('7')
    elif i == '-':
      oplist.append(i)
      tokenlist.append('47')
    elif i == '*':
      oplist.append(i)
      tokenlist.append('37')
    elif i == '/':
      oplist.append(i)
      tokenlist.append('27')
    elif i == '(':
      oplist.append(i)
      tokenlist.append('17')
    elif i == ')':
      oplist.append(i)
      tokenlist.append('67')
  return oplist

#Main method. Used to read the file., create lists of tokens, and print out the token number and lexemes. 
def main():
  INT_LIT = []
  INT_LIT2 = []

  infile = open('equations.txt', 'r')

  equation = infile.read()

  unsplitequation = equation

  if ' ' in equation:
    equation = equation.split()
  else:
    equation = list(equation)
    equation.pop()       

  length = (len(equation))
  #Creates a float list of INT_LIT
  INT_LIT = numconverter(equation)

  #Creates an int list of INT_LIT
  INT_LIT2 = numconverter2(equation)

  OPERATORS = operatorid(equation)

  IDENTITIES = anlexid(unsplitequation)

  print()
  print('In, ', unsplitequation)
  print(INT_LIT2, 'are INT_LIT tokens')
  print()
  print(OPERATORS, 'are OPERATOR tokens')
  print()
  print(IDENTITIES, 'are IDENT tokens')
  print()
  tokenlist = []
  
  token = ''
  for x in equation:
    token = gettoken(x, IDENTITIES, OPERATORS, INT_LIT2)
    tokenlist.append(gettoken(x, IDENTITIES, OPERATORS, INT_LIT2))

  for x in range(length):
    print('Next token is: ',tokenlist[x], ';' ,'Next lexeme is: ',equation[x], ';')
      
 
main()