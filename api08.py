import tbapy

eventList = []
eventKey = []
teamKeyList = []
eventTeam = []
uniqueTeamSet = set()
uniqueCountrySet = set()
uniqueStateSet = set()
uniqueCitySet = set()

API_KEY = "FSabJgFcjafTOy9LLgV9eIVrDXckixWZYg99ZgebyiR8RsDtOdXgCvX1y4vASrm6"

tba = tbapy.TBA("FSabJgFcjafTOy9LLgV9eIVrDXckixWZYg99ZgebyiR8RsDtOdXgCvX1y4vASrm6")

team = input("Enter team number: ")

eventData = tba.team_events(int(team), 2023, simple=True)

# Fetches all events that a user-provided team has participated in in the 2023 season
for i in eventData:
    event_num = i['name']
    event_key = i['key']
    eventList.append(event_num)
    eventKey.append(event_key)

print(f"Events that the team {team} participated in are: ")

for i in eventList:
    print(f"- {i}")


print("--------------------------------------------")
print("--------------------------------------------")

# Fetches all teams that participated in each of those events
for j in eventKey:
    event_teamKey = tba.event_teams(j, keys=True)
    teamKeyList.append(event_teamKey)

l = 0
while l < len(teamKeyList):
    eventTeam = []  # Clear the list for each event
    for k in teamKeyList[l]:
        event_team = tba.team(k, simple=True)
        eventTeam.append(event_team["name"])
        uniqueTeamSet.add(event_team['name'])
        uniqueCountrySet.add(event_team['country'])
        uniqueStateSet.add(event_team['state_prov'])
        uniqueCitySet.add(event_team['city'])
    print(f"The teams that participated in the event, {eventList[l]} are:")
    for team_name in eventTeam:
        print(f"  - {team_name}")

    l += 1

print("--------------------------------------------")
print("--------------------------------------------")

# Compiles a list of unique teams out of all of those teams
print("There are a total of", len(uniqueTeamSet), "unique teams: ")
for uts in uniqueTeamSet:
    print(f"- {uts}")

print("--------------------------------------------")
print("--------------------------------------------")

# Displays the following information:
# i. All unique countries that these teams are from
print("There are a total of", len(uniqueCountrySet), "unique countries: ")
for ucs1 in uniqueCountrySet:
    print(f"- {ucs1}")

print("--------------------------------------------")
print("--------------------------------------------")

# ii. All unique states or provinces that these teams are from
print("There are a total of", len(uniqueStateSet), "unique states: ")
for uss in uniqueStateSet:
    print(f"- {uss}")

print("--------------------------------------------")
print("--------------------------------------------")

# iii. All unique cities that these teams are from
print("There are a total of", len(uniqueCitySet), "unique cities: ")
for ucs2 in uniqueCitySet:
    print(f"- {ucs2}")
