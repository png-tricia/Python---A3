"""
    Name: Patricia J. Gariando 
    Student Number: 000 000 000
    Task: Assignment 3
    Date: Nov. 19 2023 
"""
# user's choices
choice = """
|- - - - - - - - -    - - - - - - - - -|
|         HR - EMPLOYEE SERVER         |
|- - - - - - - - -    - - - - - - - - -|
|  1. Add Worker                       |
|  2. Process Worker                   |
|  3. Display All Workers ID and Name  |
|  4. Display Processed Workers        |
|  5. End Program                      |
|- - - - - - - - -    - - - - - - - - -|
"""
# table headers 
tableOne = """
|------------------------------------------------------------------|
|                       EMPLOYEE - WEEKLY PAY                      |
|------------------------------------------------------------------|"""
tableTwo = """
|----------------------------------------|
|         EMPLOYEE - OVERTIME PAY        |
|----------------------------------------|"""
# dictionary 
listOfWorkers = {101:'Fred Budd', 103:'Barney Stone', 106:'Wilma Flint', 109:'Betty Rubble', 112:'Dino Dawg'}
# lists 
processedID = ['ID']
processedName = ['Name']
processedWP = ['Weekly Pay']
processedTaxes = ['Income Taxes']
processedNP = ['Net Pay']
overtimeID = ['ID']
overtimeName = ['Name']
overtimeHrs = ['Hours']
overtimeRate = ['Rate']
overtimePay = ['Pay']
# constant variable(s)
constNum = 1.5
    
def checkID(id):
    if id in listOfWorkers.keys():
        return True
    else:
        return False

def findName(name):
    if name in listOfWorkers.values():
        return True
    else:
        return False

def calculatePay(hourlyWage, hoursWorked):
    regularPay = hourlyWage * hoursWorked
    otPay = calculateOT(hourlyWage, hoursWorked)
    weeklyPay = regularPay + otPay 
    if hoursWorked > 40:
        return weeklyPay # regular pay + ot pay 
    else: 
        return regularPay # regular pay + did not work overtime 
    
def calculateTax(wage):
    if wage < 0:
        return 0
    elif wage < 300.01:
        incomeTax = wage * .10
        return incomeTax
    elif wage < 600.01:
        incomeTax = wage * .12
        return incomeTax
    elif wage < 900.01:
        incomeTax = wage * .15
        return incomeTax
    else: 
        incomeTax = wage * .20
        return incomeTax

def calculateOTHours(hoursWorked):
    return hoursWorked - 40

def calculateOT(hourlyWage, hoursWorked):
    otHours = calculateOTHours(hoursWorked)
    otPay = otHours * (hourlyWage * constNum)
    return otPay

def main():
    print(choice) # display option board 
    userChoice = int(input("Enter choice: ")) # prompt the user for a choice 
    while userChoice < 1 or userChoice > 5:
        userChoice = int(input("Invalid input - Enter choice: "))
    while userChoice != 5:
        # 1. Add Worker 
        if userChoice == 1:
            idNum = int(input("\nEnter ID number: "))
            while checkID(idNum):
                idNum = int(input("ID number already exists - Enter ID number: "))
            else:
                workerName = str(input("\nEnter name: "))
                while findName(workerName):
                    workerName = str(input("Name already exists - Enter name: "))
            listOfWorkers[idNum] = workerName
        # 2. Process Worker 
        elif userChoice == 2:
            idNum = int(input("\nEnter ID number: "))
            print()
            while idNum not in listOfWorkers:
                idNum = int(input("ID number does not exist - Enter ID number: "))
            else:
                idName = listOfWorkers.get(idNum)
                # add to the process list 
                processedID.append(idNum)
                processedName.append(idName)
                # WAGES 
                hourlyWage = int(input("Enter hourly wage: "))
                while hourlyWage < 0:
                    hourlyWage = int(input("Invalid wage - Enter hourly wage: "))
                else: 
                    hoursWorked = int(input("Enter the amount of hours worked: "))
                    while hoursWorked < 0:
                        hoursWorked = int(input("Invalid number - Enter the amount of hours worked: "))
                    if hoursWorked > 40: 
                        # add to the overtime list 
                        overtimeID.append(idNum) # ID of overtime worker 
                        overtimeHrs.append(calculateOTHours(hoursWorked)) # number of overtime hours 
                        overtimeRate.append(hourlyWage) # wage 
                        overtimePay.append(calculateOT(hourlyWage, hoursWorked)) 
                # calculate and process 
                wage = calculatePay(hourlyWage, hoursWorked)
                tax = calculateTax(wage)
                netPay = wage - tax 
                # add to the process list 
                processedWP.append(int(wage))
                processedTaxes.append(int(tax))
                processedNP.append(int(netPay))
        # 3. Display All Workers ID and Name
        elif userChoice == 3:
            print("\n|" + " -"*15 + "|")
            print("| {:<10} {:<5}".format('ID', 'Name'))
            print("|" + " -"*15 + "|")
            for idNum, workerName in listOfWorkers.items():
                print("| {:<10} {:<5}".format(idNum, workerName))
            print("|" + " -"*15 + "|")
        # 4. Display Processed Workers 
        elif userChoice == 4:
            if len(processedID) > 1:
                print(tableOne)
                for row in range(0, len(processedID)):
                    print("| {} \t {:<12} \t {:<10} \t {:<10} \t {:<10}|".format(processedID[row], processedName[row], processedWP[row], processedTaxes[row], processedNP[row]))
                print("|------------------------------------------------------------------|")
            else:
                print("\nNo workers have been processed!")
            
            if len(overtimeID) > 1:
                print(tableTwo)
                for row in range(0, len(overtimeID)):
                    print("| {} \t {:<10} {:<10} {:<10}|".format(overtimeID[row], overtimeHrs[row], overtimeRate[row], overtimePay[row]))
                print("|----------------------------------------|")

        userChoice = int(input("\nEnter choice: ")) 

if __name__ == "__main__": main() # call the main function 

print("\nPatricia J. Gariando: 000 000 000\n") # display name and student ID
