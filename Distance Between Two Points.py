spent_time_hours = int(input())
average_speed_kmh = int (input())

distance_traveled_km = spent_time_hours * average_speed_kmh

fuel_liters = distance_traveled_km / 12

print(f"{fuel_liters:.3f}")
