challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]

# Extract strings "eyes", "goggles", and "nothing"
eyes = challenge[2][1]
goggles = challenge[2][0]
nothing = challenge[3]

# Print function
print(f"My {eyes}! The {goggles} do {nothing}!")

trial = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

# Extract strings "eyes", "goggles", and "nothing"
eyes = trial[2]["eyes"]
goggles = trial[2]["goggles"]
nothing = trial[3]

# Print function
print(f"My {eyes}! The {goggles} do {nothing}!")

