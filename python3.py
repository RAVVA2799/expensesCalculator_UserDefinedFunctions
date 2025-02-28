# Function to safely get integer input
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to calculate the on-road price
def calculate_on_road_price(vehicle_type, base_price, weight):
    on_road_details = {
        "baseprice": base_price,
        "weight": weight,
        "type": vehicle_type
    }
    
    if vehicle_type == "P":  # Private vehicle
        on_road_details["vehicleTax"] = (5 / 100) * base_price
        on_road_details["insurance"] = (1 / 100) * base_price
        on_road_details["weightTax"] = (1 / 100) * weight
    elif vehicle_type == "B":  # Business vehicle
        on_road_details["vehicleTax"] = (10 / 100) * base_price
        on_road_details["insurance"] = (2 / 100) * base_price
        on_road_details["weightTax"] = (3 / 100) * weight

    on_road_details["onRoadPrice"] = base_price + on_road_details["vehicleTax"] + on_road_details["weightTax"] + on_road_details["insurance"]
    
    return on_road_details

# Function to get vehicle details from user input
def get_vehicle_details():
    
    print("----------------------------------------------------------------------------------------------")
    base_price = get_integer_input("Enter Basic Price: ")
    weight = get_integer_input("Enter Vehicle Weight: ")
    
    while True:
        vehicle_type = input("Press P for PRIVATE vehicle and B for BUSINESS vehicle: ").strip().upper()
        if vehicle_type in ['P', 'B']:
            return calculate_on_road_price(vehicle_type, base_price, weight)
        else:
            print("Invalid vehicle type! Please enter 'P' or 'B'.")

# 3b: Get details of N vehicles
def get_n_vehicle_details(n):
    vehicles = []
    for _ in range(n):
        vehicle_details = get_vehicle_details()
        vehicles.append(vehicle_details)
    return vehicles

# 3c: Find vehicle with highest on-road price and least weight
def find_highest_and_least(vehicles):
    highest_on_road_price = max(vehicles, key=lambda x: x['onRoadPrice'])
    least_weight = min(vehicles, key=lambda x: x['weight'])
    
    return highest_on_road_price, least_weight

# 3d: Perform various calculations
def perform_calculations(vehicles, given_weight, given_budget):
    total_on_road_price = sum(v['onRoadPrice'] for v in vehicles)
    average_on_road_price = total_on_road_price / len(vehicles)
    
    # Vehicles with on-road price higher than average
    count_higher_than_avg = sum(1 for v in vehicles if v['onRoadPrice'] > average_on_road_price)
    
    # Vehicles with weight above a given value
    count_above_weight = sum(1 for v in vehicles if v['weight'] > given_weight)
    
    # Vehicles with on-road price less than or equal to a given budget
    count_within_budget = sum(1 for v in vehicles if v['onRoadPrice'] <= given_budget)
    
    return average_on_road_price, count_higher_than_avg, count_above_weight, count_within_budget

# Main program flow
def main():
    # Get the number of vehicles with input validation
    n = get_integer_input("Enter the number of vehicles: ")
    
    vehicles = get_n_vehicle_details(n)

    # 3c: Find vehicle with highest on-road price and least weight
    highest_on_road_price, least_weight = find_highest_and_least(vehicles)
    print("\nVehicle with highest on-road price:", highest_on_road_price)
    print("Vehicle with least weight:", least_weight)
    
    # 3d: Perform other calculations
    given_weight = get_integer_input("Enter the given weight: ")
    given_budget = get_integer_input("Enter the given budget: ")
    
    average_on_road_price, count_higher_than_avg, count_above_weight, count_within_budget = perform_calculations(vehicles, given_weight, given_budget)
    
    print(f"\nAverage on-road price: {average_on_road_price}")
    print(f"Number of vehicles with on-road price higher than the average: {count_higher_than_avg}")
    print(f"Number of vehicles with weight above {given_weight}: {count_above_weight}")
    print(f"Number of vehicles with on-road price less than or equal to {given_budget}: {count_within_budget}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
