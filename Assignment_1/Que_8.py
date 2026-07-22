#WAP TO CONVERT DAYS INTO YEARS, WEES AND DAYS.

days = int(input("Enter the days: ")) 

years = days // 365
days = days % 365
weeks = days // 7
days = days % 7

print("Year =", years)
print("Weeks =",weeks)
print("Days =",days)

