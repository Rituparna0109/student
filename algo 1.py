a = float(input("Enter 1-1 semester percentage: "))
b = float(input("Enter 1-2 semester percentage: "))
c = float(input("Enter 2-1 semester percentage: "))
d = float(input("Enter 2-2 semester percentage: "))
e = float(input("Enter 3-1 semester percentage: "))
f = float(input("Enter 3-2 semester percentage: "))
g = float(input("Enter attendance percentage: "))
h = input("Do you have extracurricular activities? (yes or no): ")
i = input("Do you have any academic awards and achievements? (yes or no): ")
j = input("Do you have coding skills? (yes or no): ")

semester_grades=[a,b,c,d,e,f]

# Calculate dropout
dropout = 1 if min(semester_grades) < 35 and g < 30 else 0

# Calculate good performance
good_performance = 1 if all(grade > 60 for grade in semester_grades) else 0

# Calculate poor performance
poor_performance = 1 if max(semester_grades) < 40 else 0

# Calculate support required
support_required = 1 if any(40 <= grade < 60 for grade in semester_grades) else 0

# Calculate eligibility for placement
eligible_for_placement = 1 if all( grade > 65 for grade in semester_grades) and (j == "yes" or i == "yes" or h == "yes") else 0

print("\nResults:")
print(f"Dropout status: {'Yes' if dropout == 1 else 'No'}")
print(f"Good performance status: {'Yes' if good_performance == 1 else 'No'}")
print(f"Poor performance status: {'Yes' if poor_performance == 1 else 'No'}")
print(f"Support required status: {'Yes' if support_required == 1 else 'No'}")
print(f"Eligible for placement status: {'Yes' if eligible_for_placement == 1 else 'No'}")
