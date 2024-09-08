# List
# 3. Manipulating the Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Get the number of members in the Justice League
print(len(justice_league))  # Outputs: 6, as there are 6 members initially

# Adding two new members: 'Batgirl' and 'Nightwing'
justice_league.extend(["Batgirl", "Nightwing"])
print(justice_league)  # Outputs: Updated list with new members added

# Removing 'Aquaman' from the list (element at index 2)
justice_league.pop(2)

# Move 'Wonder Woman' to the beginning of the list
justice_league.insert(0, "Wonder Woman")

# Print the updated list
print(justice_league)  # Outputs: List with 'Wonder Woman' moved to the beginning

# Remove the second element (now 'Batman'), and reinsert 'Superman' at index 3
justice_league.pop(1)
justice_league.insert(3, "Superman")
print(justice_league)  # Outputs: List with 'Superman' moved to index 3

# Clear all elements from the list
justice_league.clear()

# Add new members to the Justice League
justice_league.extend(["Cyborg", "Shazam", "Hawkgirl", "Martian", "Manhunter", "Green Arrow"])
print(justice_league)  # Outputs: New list with added members

# Sort the list alphabetically
justice_league.sort()
print(justice_league)  # Outputs: List sorted in alphabetical order