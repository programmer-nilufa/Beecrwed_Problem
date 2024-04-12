# Read spent time and average speed from input
spent_time_hours, average_speed_kmh = map(int, input().split())

# Calculate distance traveled (distance = speed * time)
distance_traveled_km = spent_time_hours * average_speed_kmh
fuel_liters = distance_traveled_km / 12
print(f"{fuel_liters:.3f}")
