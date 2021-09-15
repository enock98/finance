#it allows us to use the math library
import math

#the variable below will display everthing that will be displayed before the program starts running
type_of_investments = "choose either 'investment' or 'bond' from the menu below :\n"
A_investment = "investment            - to calculate the amount of interest you'll earn on interest"
B_bond = "bond                  - to calculate the amount you'll have to pay back on a home loarn\n"
print(type_of_investments)
print(A_investment)
print(B_bond)


user = None


#the while loop is going to excute this body until the user pick what type of investment that they want to use
#its going to run till the user insect the choice of investment then it terminates
while user not in ("investment", "bond"):
    user = input("Do you want bond or investment? ").lower()
    if user not in ("investment", "bond"):
        print("Please enter 'investment' or 'bond'. ")
        
if user == "investment":


#the while loop is going to run and ask the user a series of question and only until the all the questions are answered
#will the loop terminate      
    interest_type = None
    while interest_type not in ("simple", "compound"):
        interest_type = input("do you want simple or compound interest? ").lower()
        if interest_type not in ("simple", "compund"):
            print("Please enter 'simple' or 'compound'. ")



#the if statement is going to work only when the user selects simple interest
#it will the calculate the interest rate and how long you want to invest your money for
#it will then print your display to show how much you will have at the end of your investment
    if interest_type.lower() == "simple":
        principal_amount = float(input("Enter the amount you would like to invest ? \n "))
        duration_time = float(input("Enter amount of time you would like to invest for ?\n"))
        interest_rate = float(input("Enter the interest rate  ?\n"))
        simple_interest = ( principal_amount  * duration_time * interest_rate)/100
        print("Simple interest is: %f" % (simple_interest))


#the compound interest is going to work if the user selects compound interest
#it will then calculater the interest rate and how long you want to invest your money for
#and it will then display the output to show much you will have at the end of your investment    
    elif interest_type.lower() == "compound":
        principal_amount = float(input("Enter the amount you would like to invest ? \n"))
        duration_time = float(input("Enter amount of time you would like to invest for ?\n"))
        interest_rate = float(input("Enter the interest rate  ?\n"))
        compound_interest = principal_amount * ( (1+interest_rate/100)**duration_time - 1)
        print("Compound interest is: %f\n" %(compound_interest))


#the elif statement is goin to work if the user select bond
#it will then work out how long the user is going to take to pay back the bank and the interst rate that their will be paying 
#and it will then print the results to show how much you will be paying per month 
elif user.lower() == "bond":
    p = float(input("Enter the value of the house ? \n"))
    i = int(input("Enter the interest rate ? \n"))
    i = (float(i)/100)/12
    n = int(input("Enter the number of months ? \n"))
    bond = (i * p)/(math.pow(1+ i,(-n))) 
    print("You monthly payment will be R%2f" % (bond))



# Displaying result

