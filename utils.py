from datetime import date, datetime as dt


ref_energy_values = [18,19,20.3,21,20.4,19.8,19.2,19.6,19.9,20.2,
                    19.9,19.3,20.2,20.9,21.3,22,23.3,24,23.9,23.8,
                    22.9,24,24.2,25.1]

ref_energy_values_week = [
                137.26,144.19,164.98,151.11,158.04,123.39,178.84,158.04,158.04,144.19,
                123.39,151.11,178.84,164.98,123.39,178.84,185.76,171.91,123.39,164.98,
                178.84,178.84,130.32,137.26,164.98,164.98,137.26,144.19,151.11,171.91,
                185.76,137.26,178.84,130.32,151.11,137.26,171.91,171.91,151.11,185.76,
                85.76,185.76,178.84,144.19,178.84,151.11,144.19,123.39,171.91,171.91,
                137.26,130.32]

ref_energy_values_month = [
                544.26,445.56,618.66,643.46,494.66,445.91,
                494.66,494.66,519.46,544.26,469.86,544.26]


def get_energy_values():
    hours = dt.now().hour
    energy_values = []

    for i in range(0,hours):
        energy_values.append(ref_energy_values[i])
    
    return energy_values


def get_energy_values_week():
    weeks = dt.today().strftime("%U")

    energy_values = []

    for i in range(0, weeks):
        energy_values.append(ref_energy_values_week)

    return energy_values

def get_energy_values_month():
    months = dt.now().month

    energy_values = []

    for i in range(0, months):
        energy_values.append(ref_energy_values_month)

    return energy_values


################
# Home functions
################

def get_date():
    return date.today()

def get_location():
    return "Helsinki"

def get_room_info(room_no):
    room_values = [
        {
            "temperature": 23,
            "cost": 43
        },
        {
            "temperature": 21,
            "cost": 46
        },
        {
            "temperature": 22.3,
            "cost": 44.7
        },
        {
            "temperature": 25,
            "cost": 36
        },
        {
            "temperature": 18,
            "cost": 61
        },
        {
            "temperature": 19,
            "cost": 56.3
        },
        {
            "temperature": 20,
            "cost": 41.7
        },
        {
            "temperature": 23,
            "cost": 43
        }
    ]

    return room_values[room_no]


###################
# History functions
###################