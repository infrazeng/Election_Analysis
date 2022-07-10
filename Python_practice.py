print("Hello World")
num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True

counties = ["Arapahoe","Denver","Jefferson"]
counties
['Arapahoe', 'Denver', 'Jefferson']
counties[0]
'Arapahoe'
counties.insert(2, "El Paso")
counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson']
counties[2] = "Denver"
counties.insert(1, "El Paso")
counties.remove("Arapahoe")
counties
['El Paso', 'Denver', 'Denver', 'Jefferson']
counties[1] = "Jefferson"
counties.append("Arapahoe")
counties
['El Paso', 'Jefferson', 'Denver', 'Jefferson', 'Arapahoe']
counties.pop(3)
'Jefferson'
counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
counties_tuple[1]
'Denver'
len(counties_tuple)
3
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
len(counties_dict)
3
counties_dict.items()
counties_dict["Arapahoe"]


[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Jefferson', 'registered_voters': 432438}]

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

input = 90
temp = int(input("What is the temperature outside?"))
if temp > 80:
    print("Turn on the AC")
else:
    print("Open the windows.")

counties = ["Arapahoe", "Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

counties = ["Arapahoe", "Denver","Jefferson"]
for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

    
