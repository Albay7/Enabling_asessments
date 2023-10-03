#Salary Bonus
def calculate_bonus(years_of_service,runtime):

    if years_of_service <= 5:
        runtime = 0+1
        bonus_percentage = 0                                # 0(1)

    elif years_of_service >= 5 and years_of_service <= 10:
        runtime = 1+1
        bonus_percentage = 0.5                              # 0(1)


    elif years_of_service >= 10 and years_of_service <= 15:
        runtime = 1+2
        bonus_percentage = 1.0                              # 0(1)

    elif years_of_service >= 15 and years_of_service <= 20:
        runtime = 1+3
        bonus_percentage = 1.5                              # 0(1)

    elif years_of_service >= 20 and years_of_service >= 20:
        runtime = 1+4
        bonus_percentage = 2.0                              # 0(1)

    else:
        runtime = 1+5
        print("Invalid option")                             # 0(1)


    salary = float(input("Enter the employee's basic salary: $"))
    bonus = salary * bonus_percentage
    total_salary = salary + bonus

    print("\n")

    print(f"Employee's Bonus: ${bonus:.2f}")
    print(f"Hello {name} your Total Salary with Bonus: ${total_salary:.2f}")
    print(f"The running time of the code is 0 ({runtime})")
    # Input the years of service

name = input("Enter your name: ")
years_of_service = int(input("Enter the number of years of service: "))
runtime = 0

# Call the function to calculate the bonus
calculate_bonus(years_of_service,runtime)


