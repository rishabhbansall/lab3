import pandas as pd
print("Rishabh bansal")
employee_data = [
    ["161E90", "Raman", 41, 56000],
    ["161F91", "Himadri", 38, 67500],
    ["161F99", "Jaya", 51, 82100],
    ["171E20", "Tejas", 30, 55000],
    ["171G30", "Ajay", 45, 44000],
]
# -----data
#----
df = pd.DataFrame(employee_data, columns=["Employee ID", "Name", "Age", "Salary (PM)"])

search_parameter = int(input("Enter the search parameter: 1 (Age), 2 (Name), 3 (Salary): "))

search_value = input("Enter the search value: ")

if search_parameter == 1:
  
    df_filtered = df[df["Age"] == search_value]
elif search_parameter == 2:
  
    df_filtered = df[df["Name"] == search_value]
elif search_parameter == 3:
   
    operator = input("Enter the operator (>, <, <=, >=): ")
    df_filtered = df[df["Salary (PM)"] ,operator, search_value]
else:
    print("Invalid search parameter.")

####
print(df_filtered)