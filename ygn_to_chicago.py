from datetime import datetime, timedelta

def convert_yg_to_chicago(yg_time_str):
    # Define the time difference between YGn and Chicago
    time_difference = timedelta(hours=11, minutes=30)
    
    # Parse the YGn time string to a datetime object
    yg_time = datetime.strptime(yg_time_str, "%Y-%m-%d %H:%M:%S")
    
    # Convert YGn time to Chicago time by subtracting the time difference
    chicago_time = yg_time - time_difference
    
    # Return the Chicago time as a string in the same format
    return chicago_time.strftime("%Y-%m-%d %H:%M:%S")

# Example usage:
yg_time_str = "2024-09-11 20:49:00"  # Replace with the actual YGn time
chicago_time_str = convert_yg_to_chicago(yg_time_str)

print("yangon time:", yg_time_str)
print("Chicago time:", chicago_time_str)

