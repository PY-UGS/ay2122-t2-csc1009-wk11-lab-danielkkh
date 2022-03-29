class Calculator: #constructor
    def __init__(self,input1,input2):
        self.input1=input1
        self.input2=input2

    def adder(self): #function for addition
        return input1+input2

    def subtractor(self): #function for subtraction
        return input1-input2

    def multiplier(self): #function for multiplication
        return input1*input2

    def dividor(self): #function for division
        return input1/input2 

    def clear(self): #function to set values of Calculator class to 0
        self.input1=0 #set input1 to 0
        self.input2=0 #set input2 to 0

#user input 2 numbers
input1=float(input("Enter first number:"))
input2=float(input("Enter second number:"))

#initialize calculator object with user inputs
calculator=Calculator(input1,input2)
#perform all operations and output result
print("Addition:",calculator.adder())
print("Subtraction:",calculator.subtractor())
print("Multiplication",calculator.multiplier())
print("Division:",calculator.dividor())
calculator.clear() #reset values
print("After reset, value of input1 is:",calculator.input1," and input2 is:",calculator.input2)