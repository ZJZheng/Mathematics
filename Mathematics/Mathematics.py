# Author: Zongjun Zheng
# Date: 3/12/2018
###############################################################################################################################
from __future__ import division
import random
import operator
import numpy as np
import time
from sympy import *
from fractions import Fraction

# Arithmetic Questions
def ArithmrandomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    if type(answer) != int:
        answer = round(answer,3)
    print('What is {} {} {}?\n'.format(num1, op, num2))
    return answer

def ArithmaskQuestion():
    answer = ArithmrandomCalc()
    check = 1
    while (check):
        guess = input()
        if guess.isspace() or guess == '':
            print("Answer cannot be blank")
            continue
        if not guess.lstrip('-').isdigit():
            print('Answer has to be numbers')
            continue
        guess = float(guess)
        check = 0
    return answer, guess == answer

def Arithmetic(n):
    print('Welcome. This is a %d-question Arithimetic quiz\n' %n)
    print('For non-integer answers, please round answer to 3 decimal places\n')
    score = 0
    for i in range(n):
        answer, correct = ArithmaskQuestion()
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!')
            print("The correct answer is: ", answer)
            print('\n')
    percent = score/n
    print('Your score is: %d/%d'%(score,n))
    print ("Your accuracy of Arithmetic is:", "{0:.0f}%".format(percent * 100))
    return percent


# Fraction Questions
def FractionrandomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    numera1 = random.randint(1,10)
    numera2 = random.randint(1,10)
    denom1 = random.randint(1,10)
    denom2 = random.randint(1,10)
    num1 = Fraction(numera1, denom1)
    num2 = Fraction(numera2, denom2)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print('What is {}{}{} {} {}{}{}?\n'.format('(',num1,')', op, '(',num2,')'))
    return answer

def FractionQuestion():
    answer = FractionrandomCalc()
    check = 1
    while (check):
        guess = input()
        if guess.isspace() or guess == '':
            print("Answer cannot be blank")
            continue
        check = 0
    return answer, guess == str(answer)

def Fractionmain(n):
    print('Welcome. This is a %d-question Fraction quiz\n' %n)
    print('Please keep the answers in fraction form')
    score = 0
    for i in range(n):
        answer, correct = FractionQuestion()
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!')
            print("The correct answer is: ", answer)
            print('\n')
    percent = score/n
    print('Your score is: %d/%d'%(score,n))
    print ("Your accuracy of Fraction is:", "{0:.0f}%".format(percent * 100))
    return percent


# Derivative Questions
def DerivativerandomCalc():
    x, y, z = symbols('x y z')
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    coeff1 = random.randint(1,10)
    coeff2 = random.randint(1,10)
    coeff3 = random.randint(1,10)
    power1 = random.randint(1,10)
    power2 = random.randint(1,10)
    power3 = random.randint(1,10)
    isexp = random.randint(1,5)
    if isexp > 2:
        op1 = random.choice(list(ops.keys()))
        op2 = random.choice(list(ops.keys()))
        eq = ops.get(op1)(coeff1*(symbols('x y z')[random.randint(0,2)]**power1),coeff2*(symbols('x y z')[random.randint(0,2)]**power2))
        eq = ops.get(op2)(eq,coeff3*(symbols('x y z')[random.randint(0,2)]**power3))
        v = symbols('x y z')[random.randint(0,2)]
        answer = diff(eq,v)
    else:
        op1 = random.choice(list(ops.keys()))
        op2 = random.choice(list(ops.keys()))
        eq = ops.get(op1)((coeff1*(exp(symbols('x y z')[random.randint(0,2)]**power1))),(coeff2*(symbols('x y z')[random.randint(0,2)]**power2)))
        eq = ops.get(op2)((eq),(coeff3*(symbols('x y z')[random.randint(0,2)]**power3)))
        v = symbols('x y z')[random.randint(0,2)]
        answer = diff(eq,v)
    print('What is the derivative of:\n',eq,'with respect to:',v) 
    return answer

def DerivativeQuestion():
    answer = DerivativerandomCalc()
    answer = str(answer)
    check = 1
    while (check):
        guess = input()
        if guess.isspace() or guess == '':
            print("Answer cannot be blank")
            continue
        guess = str(guess)
        check = 0
    def compare(s1, s2):
        return [c for c in s1 if c.isalpha()] == [c for c in s2 if c.isalpha()]
    correct = compare(answer,guess)
    return answer, correct

def Derivative(n):
    print('Welcome. This is a %d-question Derivative quiz\n' %n)
    print('For non-integer answers, please round answer to 3 decimal places\n')
    score = 0
    for i in range(n):
        answer, correct = DerivativeQuestion()
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!')
            print("The correct answer is: ", answer)
            print('\n')
    percent = score/n
    print('Your score is: %d/%d'%(score,n))
    print ("Your accuracy of Derivative is:", "{0:.0f}%".format(percent * 100))
    return percent


# Matrix Questions
def MatrixrandomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':'matrix multiplication',
           'invert':'invert the matrix'}
    op = random.choice(list(ops.keys()))
    if op == '+' or op == '-' :
        matrix1 = np.random.randint(10, size=(2, 2))
        matrix2 = np.random.randint(10, size=(2, 2))
        answer = ops.get(op)(matrix1,matrix2)
        print('What is {} {} {}?\n'.format(matrix1, op, matrix2))
        return answer
    elif op == '*':
        matrix1 = np.random.randint(10, size=(2, 2))
        matrix2 = np.random.randint(10, size=(2, 2))
        answer =  np.matmul(matrix1, matrix2)
        print('What is {} {} {}?\n'.format(matrix1, op, matrix2))
        return answer
    else:
        while(1):
            matrix = np.random.randint(10, size=(2, 2))
            try:
                inverse = np.linalg.inv(matrix)
                print('What is the {} {} {}?\n'.format('inversion', 'of', matrix))
                break
            except np.linalg.LinAlgError:
                pass
        for i in range(inverse.shape[0]):
            for j in range(inverse.shape[1]):
                inverse[i][j] = round(inverse[i][j],3)
        return inverse
        

def MatrixQuestion():
    answer = MatrixrandomCalc()
    result = np.copy(answer)
    check = 1
    while (check):
        check2 = 1
        guess = input()
        if guess.isspace() or guess == '':
            print("Answer cannot be blank")
            continue
        guess=[x.strip() for x in guess.split(',')]
        for i in guess:
            if not i.lstrip('-').isdigit():
                print('Answer has to be numbers')
                check2 = 0
                break
        if check2 == 0:
            continue
        check = 0
        guess = list(map(float, guess))
    result = result.tolist()
    result2 = []
    for i in result:
        result2 = result2 + i 
    return answer, guess == result2

def Matrix(n):
    print('Welcome. This is a %d-question Matrix quiz\n' %n)
    print('Type answers in a list. e.g. 1,2,3,4 stands for 2 by 2 matrix [[1,2],[3,4]]\n')
    print('For non-integer answers, please round answer to 3 decimal places\n')
    score = 0
    for i in range(n):
        answer, correct = MatrixQuestion()
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!')
            print("The correct answer is: ", answer)
            print('\n')
    percent = score/n
    print('Your score is: %d/%d'%(score,n))
    print ("Your accuracy of Arithmetic is:", "{0:.0f}%".format(percent * 100))
    return percent


# The main Quiz Program
stop = 0
typestr = {1:'Arithmetic',2:'Fraction',3:'Derivative',4:'Matrix'}
print('Type of Questions: ', typestr)
while (1):
    if stop ==0:
        typeofquestions = {1:Arithmetic,2: Fractionmain, 3:Derivative, 4:Matrix}
        check = 1
        while (check):
            index = input("Pick index of question type: ")
            if index.isspace() or index == '':
                print("Choice cannot be blank")
                continue
            if not index.isdigit():
                print('Has to choose a number')
                continue 
            index = int(index)
            check = 0
        check = 1
        while (check):
            n = input("Enter the number of questions: ")
            if n.isspace() or n == '':
                print("Choice cannot be blank")
                continue
            if not n.isdigit():
                print('Has to choose a number')
                continue 
            n = int(n)
            check = 0        
        print('')
        typeofquestions[index](n)
        stop = 1
        print('')
    else:
        flag = 0
        while (flag == 0):        
            quit = input("want to end the quiz? y/n: ")
            if quit == 'y':
                flag = 1
                break
            elif quit=='n':
                print('')
                typeofquestions = {1:Arithmetic, 2:Fractionmain, 3:Derivative, 4:Matrix}
                check = 1
                while (check):
                    index = input("Pick index of question type: ")
                    if index.isspace() or index == '':
                        print("Choice cannot be blank")
                        continue
                    if not index.isdigit():
                        print('Has to choose a number')
                        continue
                    index = int(index)
                    check = 0
                check = 1
                while (check):
                    n = input("Enter the number of questions: ")
                    if n.isspace() or n == '':
                        print("Choice cannot be blank")
                        continue
                    if not n.isdigit():
                        print('Has to choose a number')
                        continue 
                    n = int(n)
                    check = 0                     
                print('')
                typeofquestions[index](n)
                print('')
            else:
                print('Have to choose between y or n')
                continue 
        if flag == 1:
            break

print('')
print('Quiz Over\n')
print('Program Closing...')
time.sleep(3) 