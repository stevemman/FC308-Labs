# Option 1 : Take the bus to the college.
# Distance from the college is 5 miles.
college_dist = 5

# Bus speed is 25 mph.
bus_speed = 25

# Each stop delays the bus by 2 mins.
stop_delay = 2

# Number of stops is 10.
stops = 10

# Calculate the commute time in minutes when taking the bus.
# We convert mph to mile per minute so that total_time is measured in minutes instead of hours.
total_time_bus = college_dist / (bus_speed / 60) + stop_delay * stops

# Print the bus commute time.
print("The total commute time by bus is:", int(total_time_bus), "minutes")

# Option 2 : Jog to the college.
light_jog_speed = 6
heavy_jog_speed = 10
medium_jog_speed = 7

# Calculate the commute time in minutes when jogging.
# We convert mph to mile per minute so that total_time is measured in minutes instead of hours.
total_time_jog = 1 / (light_jog_speed / 60) + 2 / (heavy_jog_speed / 60) + 1 / (medium_jog_speed / 60)

# Print the jog commute time.
print("The total commute time by jogging is:", int(total_time_jog), "minutes")
