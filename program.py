"""User interactivity"""
from studentworkloadcalculator import  StudentWorkloadCalculator
class Program:
    #TODO: define user name as a field variable in this class

    def run(self):
        #TODO: ask the user for their name and initialize field variable with the name provided

        #create a workload calculator object
        calc = StudentWorkloadCalculator()

        #ask the user for the number of class hours per week
        classHours = int(input("Please enter the number of class  hours per week: "))

        #set the class hours in the calculator
        calc.setClassHours(classHours)

        #ask the user for the number of work hours per week
        workHours  = int(input("Please enter the number of hours per week: "))

        #set the work hours in the calculator
        calc.setWorkHours(workHours)

        #TODO: use the name the user in the output messages
        
        #inform the user how many hours of independent study are required
        print(f"You will need to study independently for {calc.getIndepStudyHours()}")

        #let the user know what the total workload is
        totalWorkload = calc.calculateWorkload()
        print (f"Your total workload per week is {totalWorkload}")