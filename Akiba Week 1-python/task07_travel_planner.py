destination= input("Enter Destination: ")
distance= float(input("Enter Distance: "))
speed = float(input("Enter Average Speed in km/h: "))
print()

time = distance / speed

#bonus

hours = int(time)
minutes = int((time - hours) * 60)


print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {speed} km/h\n")

print(f"Estimated Travel Time: {hours} hours and {minutes} minutes")