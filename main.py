import os
#
#
def Retirement():
    while(True):
        try:
            userAge=int(input("Enter your age: "))

            if(userAge>100):
            
                print("Retirement calculator is not valid for age over 100 years")
                print(" ")
                continue
            annualSalaryOfUser=int(input("Enter your annual salary: "))
            savedPercentage=int(input("Enter percentage Saved of your monthly salary: "))
            savingsGoal=int(input("Enter savings goal: "))
            break

        except:
            print("Enter valid values.")
            print("")
            closingApp=input("Do you want to exit out of BMI calculator, type \"yes\" to exit, or type \"no\" to continue: ")
            closingApp=closingApp.lower()
            if(closingApp=="yes"):
                print("")
                main()
            continue

    monthlySalary=annualSalaryOfUser/12
    savingInMonth=monthlySalary*(savedPercentage/100)
    savingInMonth=savingInMonth+(savingInMonth*(35/100))
    savingInYear=savingInMonth*12
    yearsWhenITheyGonnaAchieve=savingsGoal/savingInYear

    if(yearsWhenITheyGonnaAchieve+userAge>100):
        print("Can't achieve this with your age less than 100 years. ")

    else:
        print("Numbers of years to achieve your goal: "+str(yearsWhenITheyGonnaAchieve))
        print("Age where the goal will be met: "+str(yearsWhenITheyGonnaAchieve+userAge))
    return 0,0


    
def BMIFunction():

    print("Welcome to Body mass index calculator. ")
    while(True):
        try:
            weightInPounds=int(input("Enter weight in pounds: "))
            heightInFeetAndInches=input("Enter height in format feet\'inches\" ")

            heightInFeet=int(heightInFeetAndInches[:heightInFeetAndInches.find("\'")])
            heightInInches=int(heightInFeetAndInches[(int(heightInFeetAndInches.find("\'"))+1):heightInFeetAndInches.index("\"")])
            break
        
        except:
            print("Enter valid values")
            closingApp=input("Do you want to exit out of BMI calculator, type \"yes\" to exit, or type \"no\" to continue: ")
            closingApp=closingApp.lower()
            if(closingApp=="yes"):
                main()
 
            continue

    weightInKilograms=weightInPounds*0.45
    heightInMeters=((heightInFeet*12)+(heightInInches))*0.025
    BMICategory=""
    BMI=(weightInKilograms)/(heightInMeters**2)

    if(BMI<=18.5):
        BMICategory="underweight"
    elif(BMI>18.5 and BMI<24.9):
        BMICategory="normal weight"
    elif(BMI>25 and BMI<29.9):
        BMICategory="over weight"
    elif(BMI>=30):
        BMICategory="obese"
    return BMI, BMICategory

    


def main():
    print(" ")
    print("Welcome to the command-line interface")
    while(True):
        print(" ")
        print("""
        1) Body Mass Index
        2) Retirement
        3) exit()
    """)

        


        while(True):
            try:
                user_choice=int(input("Enter opition number: "))

                if(user_choice==1):
                    print(" ")
                    BMI, BMICategory = BMIFunction()
                elif(user_choice==2):
                    print(" ")
                    BMI, BMICategory = Retirement()
                elif(user_choice==3):
                    os._exit(0)
                break

            except:
                print("Number should be within the range of the options given.")
                print(" ")
                continue


        if(BMI and BMICategory):
            print("Your BMI: "+str(round(BMI,2)))
            print("Your BMI category: "+str(BMICategory))   
    
        
main()
