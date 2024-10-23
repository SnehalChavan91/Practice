# Rupal has a huge collection of country stamps. 
# She decided to count the total number of distinct country stamps in her collection. She asked for your help. 
# You pick the stamps one by one from a stack of  country stamps.

# Find the total number of distinct country stamps.

distinct_countries=set()    #initialize an empty set
n=int(input("Enter the number of countries"))

for _ in range(n):
    stamp=input("Enter the country name : ").strip()
    distinct_countries.add(stamp)

print("Total number of distinct country stamps: ",len(distinct_countries))