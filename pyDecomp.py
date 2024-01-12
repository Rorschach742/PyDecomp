import json

# Read JSON data from the file
with open('dive_data.json', 'r') as file:
    database = json.load(file)

# Get user input for depth and time
user_depth = input("Enter the depth of the dive: ")
user_time = input("Enter the duration of the dive: ")

# Check if the entered depth exists in the database
depths = sorted(map(int, database["depth"].keys()))
selected_depth = next((str(d) for d in depths if d >= int(user_depth)), None)

if selected_depth:
    # Check if the entered time exists in the database for the selected depth
    times = sorted(map(int, database["depth"][selected_depth]["time"].keys()))
    selected_time = next((str(t) for t in times if t >= int(user_time)), None)

    if selected_time:
        # Retrieve the data for the selected depth and time
        result = database["depth"][selected_depth]["time"][selected_time]
        print(f"Data for depth {selected_depth} and time {selected_time}:\n{result}")
    else:
        print(f"No data found for time {user_time} or any greater time for depth {selected_depth}.")
else:
    print(f"No data found for depth {user_depth} or any greater depth.")
