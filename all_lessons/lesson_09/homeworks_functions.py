
# function 1
# create a function to the homework 5.1
# get cars that satisfy search criteria
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

def matching_cars(min_year, min_engine_volume, max_price):

    suitable_cars_list = [
        (car, *data)
        for car, data in car_data.items()
        if data[1] >= min_year and data[2] >= min_engine_volume and data[4] <= max_price
    ]

    # sorted 'suitable_cars_list' by price ascending
    sorted_by_price = sorted(suitable_cars_list, key=lambda x: x[5])

    if not sorted_by_price:  # if list is empty print 'No matching cars' text
        return 'No matching cars'
    else:  # if matches exist - print up to five first found elements
        return sorted_by_price[:5]


# Function 2
def find_primes(n: int) -> list:
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Function 3
def convert_to_24_hour(time_str):
    parts = time_str.split()
    if len(parts) != 2:
        raise ValueError('Time format is not a `hh:mm period`')
    time, period = parts
    hours, minutes = map(int, time.split(':'))

    # Validate the hours and minutes
    if not (1 <= hours <= 12):
        raise ValueError('Hours must be between 1 and 12')
    if not (0 <= minutes <= 59):
        raise ValueError('Minutes must be between 0 and 59')

    # Validate the period
    period = period.lower()
    if period not in ['am', 'pm']:
        raise ValueError('Period must be either "am" or "pm"')

    #Convert the time
    if period.lower() == 'pm' and hours != 12:
        hours += 12
    elif period.lower() == 'am' and hours == 12:
        hours = 0
    return f'{hours:02}:{minutes:02}'


