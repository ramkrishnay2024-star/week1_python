# Pandas
# import os
# os.system("cls")

## Pandas Class 1 Practice:

import pandas as pd


ice_cream = ['chocolate']
result = pd.Series(ice_cream)
print(result)

lottery_number = [4,8,15,16,23,42]
print(pd.Series(lottery_number))

booleans = ['True','False','True','False']
result = pd.Series(booleans)
print(result)

complexes = [1-2j,4+1j,9+2J]
result = pd.Series(complexes)
print(result)

Create a Series object from a dictionary:
fish = {"Salmon":"Orange","Tuna":"Red","Eel":"Brown"}
result = pd.Series(fish)
print(result['Tuna'])
print(result.iloc[0])

price = pd.Series([2.99, 4.55, 1.33])
print(price/2)

price = pd.Series([2.99, 4.55, 1.33])
print(price.mean())

price = pd.Series([2.99, 3.55, 1.33])
print(price.std())

pds = pd.Series([1,2,3,2000]).std()
print(pds)

# Into to Attribues

adjectives = pd.Series(["Smart", "Charming", "Brilliant", "Humble", "Smart"])
print(adjectives)

adjectives = pd.Series(["Smart", "Charming", "Brilliant", "Humble", "Smart"])
print(len(adjectives))

adjectives = pd.Series(["Smart", "Charming", "Brilliant", "Humble", "Smart"])
print(adjectives.size)

adjectives = pd.Series(["Smart", "Charming", "Brilliant", "Humble" , "Smart"])
print(adjectives.is_unique)

adjectives = pd.Series(["Smart", "Charming", "Brilliant", "Humble" , "Smart"])
print(adjectives.values)
print(adjectives.index)
print(list(adjectives.index))
print(list(adjectives.values))
print(adjectives)
print(dict(adjectives))
print(type(adjectives.index))

fruits = ['Apple', 'Orange', 'Plum', 'Grape', 'Blueberry', 'watermelon']
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'THursday', 'Friday', 'Monday']
print(pd.Series(weekdays))
print(pd.Series(fruits))
print(pd.Series(data=weekdays))
result = pd.Series(fruits,weekdays))
print(result.iloc['Monday'])



fruits = ['Apple', 'Orange', 'Plum', 'Grape', 'Blueberry', 'watermelon']
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'THursday', 'Friday', 'Monday']
result = pd.Series(fruits,weekdays)
# print(result.loc['Monday'])
print(result.loc[0])

pandu = pd.Series([1,2,3,4])
print(pandu)

df = pd.read_csv(r"C:\Users\hp\Desktop\employees.csv", usecols=["Team"]).squeeze("columns")
print(df)

df = pd.read_csv(r"C:\Users\hp\Desktop\google_stock_price.csv",usecols=["Price","Date"])
print(df)
print(type(df))

a = 2.49*1000
print(a)

b = 1000*138
print(b)

# Head and Tail method

employee = pd.read_csv(r"C:\Users\hp\Desktop\employees.csv",usecols=['First Name','Salary'])
print(employee)
print(employee.tail(10))
print(employee.sample(5))
print(len(employee))
print(type(employee))
print(list(employee.head(5)))
print(dict(zip(employee['First Name'],employee['Salary'])))

employee = pd.read_csv(r"C:\Users\hp\Desktop\employees.csv")
print(employee.head())
print(employee.columns)

employee = pd.read_csv(r"C:\Users\hp\Desktop\employees.csv",usecols=["First Name"])
# sorted_name = employee.sort_values(by="Salary")
# print(sorted_name.to_string(index=False))
# print(employee.sort_values(by='First Name'))
print(sorted(employee["First Name"].dropna(),reverse=True))  # Remove Nan value ese it will show an error
print(sorted())

google_stock = pd.read_csv(r"C:\Users\hp\Desktop\google_stock_price.csv",usecols=["Price"]).squeeze("columns")
maxs = max(google_stock)
print("Maximum Price:",maxs)
mins = min(google_stock)
print("Minimum Price:",mins)
print(sorted(google_stock))

# import os 
# os.system("cls")

nba = pd.read_csv(r"C:\Users\hp\Desktop\nba.csv")
check = (nba["Name"] == "Jeff Withey").any()
print(check)

lst = "arc" in "racecar"
print(lst)

nba = pd.read_csv(r"C:\Users\hp\Desktop\nba.csv")
print(nba.values)

nba = pd.read_csv(r"C:\Users\hp\Desktop\nba.csv")
checks = "Avery Bradley" in nba["Name"].values
print(checks)

googly = pd.read_csv(r"C:\Users\hp\Desktop\google_stock_price.csv",usecols=["Price"]).squeeze()
print(googly.head(10))
print(googly.sort_values(ascending=False).tail(3))
print(googly.head(15))
print(googly.sort_index())

nba = pd.read_csv(r"C:\Users\hp\Desktop\nba.csv",usecols=["Name"])
print(nba.sort_values(by="Name"))
print(nba.sort_index)















    
    