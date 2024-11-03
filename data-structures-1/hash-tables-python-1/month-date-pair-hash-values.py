# Computing list of all month, date pairs having same hash value
from collections import defaultdict

# Initialize a dictionary to track collisions
collisions = defaultdict(list)

# Number of days in each month for a non-leap year
days_in_month = {
    1: 31,  # January
    2: 28,  # February
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Calculate hash values for each (month, date) pair
for month in range(1, 13):
    for date in range(1, days_in_month[month] + 1):
        hash_value = month * 31 + date
        collisions[hash_value].append((month, date))

# Filter out hash values that have more than one pair (indicating a collision)
collision_list = {k: v for k, v in collisions.items() if len(v) > 1}

# Print the collisions
for hash_value, dates in collision_list.items():
    print(f"Hash Value {hash_value}: {dates}")
