def temperature_tracker():
    # Initialise variables to store calculations 
    total_temperature = 0.0
    day_count = 0

    # Initialise highest_temperature to a very low integer value and lowest_temperature to a very high integer value.
    highest_temperature = -1_000_000  # A sufficiently low integer
    lowest_temperature = 1_000_000   # A sufficiently high integer

    increased_days_count = 0
    previous_day_temperature = None  # To keep track of the temperature from the preceding day 

    file_name = "hk-temperatures-2024.txt" # Opening the text file

    try:
        # Open the temperature file read only. The 'with' statement ensures the file is closed automatically.
        with open(file_name, 'r') as file:
            # Loop through each line in the file, as each line contains a daily temperature reading.
            for line in file:
                try:
                    # Remove any leading/trailing whitespace (like newline characters) and convert the string
                    # to a float.
                    current_temperature = float(line.strip())

                    total_temperature += current_temperature
                    # running total of total temperatue to be used to calculate average
                    day_count += 1

                    # Use selection structures (if statements) to identify the highest and lowest temperatures
                    if current_temperature > highest_temperature:
                        highest_temperature = current_temperature

                    if current_temperature < lowest_temperature:
                        lowest_temperature = current_temperature

                    # Compare with the previous day's temperature to count increases.
                    # This comparison is skipped for the very first day's reading 
                    if previous_day_temperature is not None:
                        if current_temperature > previous_day_temperature:
                            increased_days_count += 1

                    # Update the previous day's temperature for the next iteration of the loop
                    previous_day_temperature = current_temperature

                except ValueError:
                    # Implement exception handling for non-numeric data in the file to prevent crashes
                    print(f"Warning: Skipping non-numeric data found in file: '{line.strip()}'")
                    continue  # Move to the next line in the file

    except FileNotFoundError:
        # Implement exception handling for cases where the input file does not exist 
        print(f"Error: The temperature file '{file_name}' was not found. Please ensure it is in the correct directory.")
        # Return default values (0 for all statistics) if the file cannot be processed
        return 0, 0, 0, 0

    # Calculate the average temperature, ensuring to handle cases where no valid data was read
    if day_count > 0:
        average_temperature = total_temperature / day_count
    else:
        average_temperature = 0.0
        # If no valid temperatures were read, reset highest/lowest to 0 for a meaningful return
        highest_temperature = 0.0
        lowest_temperature = 0.0

    # Round all calculated temperature values to the nearest integer
    rounded_average_temperature = round(average_temperature)
    rounded_highest_temperature = round(highest_temperature)
    rounded_lowest_temperature = round(lowest_temperature)

    # The function must return 4 integers: average, highest, lowest, and count of increased days
    return rounded_average_temperature, rounded_highest_temperature, rounded_lowest_temperature, increased_days_count

avg_temp, high_temp, low_temp, days_increased = temperature_tracker()
print(f"Average Temperature (rounded): {avg_temp}°C")
print(f"Highest Temperature (rounded): {high_temp}°C")
print(f"Lowest Temperature (rounded): {low_temp}°C")
print(f"Number of Days with Temperature Increase: {days_increased}")