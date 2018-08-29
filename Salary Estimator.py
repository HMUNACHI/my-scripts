
salary = int(input("Enter your Start salary: "))
work_years = int(input("Enter Work Years: "))
print_mean = int(input("Enter 1 if you want me to display the mean or 0 if you dont: "))
total_salary = 0
counter = 1
mean_salary = 0
salary_increase_rate = salary * 0.05

while counter <= work_years:
    salary = salary + salary_increase_rate
    total_salary = total_salary + salary
    counter = counter + 1

mean_salary = total_salary / work_years

print("Current Salary is: ", salary)

if print_mean is 1:
    print("Mean Salary is: ", mean_salary)

input("Press ENTER to exit")
 
