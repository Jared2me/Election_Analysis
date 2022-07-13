counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)


counties_tuples = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuples)):

      print(counties_tuples[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):

      print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

candidate_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

