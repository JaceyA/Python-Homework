# Program to calculate time saved by speeding

# Gather user inputs
avg_speed = float(input("Enter your average speed (mph): "))
speed_limit = float(input("Enter the speed limit (mph): "))
distance = float(input("Enter the distance traveled (miles): "))

# Calculate travel times
time_at_avg_speed = distance / avg_speed
time_at_limit_speed = distance / speed_limit

#If statement
if avg_speed > speed_limit:
    savedtime = avg_speed - speed_limit
else:
    print("Safe driver but no time saved")

# Calculate time saved (in minutes)
time_saved = (time_at_limit_speed - time_at_avg_speed) * 60

# Output result
print(f"You saved {time_saved:.2f} minutes by traveling at {avg_speed} mph instead of {speed_limit} mph.")
