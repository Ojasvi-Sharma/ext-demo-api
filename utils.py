from datetime import date, datetime as dt

optimization_applied = False

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

rooms = {
    "0": {
        "ac": [
            {
                "id": 1,
                "temp": 22
            },
            {
                "id": 2,
                "temp": 22
            },
            {
                "id": 3,
                "temp": 22
            }
        ],
        "light": [
            {
                "id": 1,
                "state": True
            },
            {
                "id": 2,
                "state": False
            },
            {
                "id": 3,
                "state": True
            },
            {
                "id": 4,
                "state": True
            }
        ]
    },
    "1": {
        "ac": [
            {
                "id": 1,
                "temp": 22
            },
            {
                "id": 2,
                "temp": 22
            }
        ],
        "light": [
            {
                "id": 1,
                "state": True
            },
            {
                "id": 2,
                "state": False
            },
            {
                "id": 3,
                "state": True
            }
        ]
    },
    "2": {
        "ac": [
            {
                "id": 1,
                "temp": 23
            },
            {
                "id": 2,
                "temp": 23
            }
        ],
        "light": [
            {
                "id": 1,
                "state": True
            },
            {
                "id": 2,
                "state": False
            },
            {
                "id": 3,
                "state": False
            },
            {
                "id": 4,
                "state": True
            }
        ]
    },
    "3": {
        "ac": [
            {
                "id": 1,
                "temp": 29
            },
            {
                "id": 2,
                "temp": 29
            },
            {
                "id": 3,
                "temp": 29
            }
        ],
        "light": [
            {
                "id": 1,
                "state": True
            },
            {
                "id": 2,
                "state": False
            }
        ]
    },
    "4": {
        "ac": [
            {
                "id": 1,
                "temp": 23
            }
        ],
        "light": [
            {
                "id": 1,
                "state": True
            },
            {
                "id": 2,
                "state": False
            },
            {
                "id": 3,
                "state": False
            },
            {
                "id": 4,
                "state": True
            },
            {
                "id": 5,
                "state": True
            }
        ]
    },
    "5": {
        "ac": [
            {
                "id": 1,
                "temp": 23
            },
            {
                "id": 2,
                "temp": 23
            }
        ],
        "light": [
            {
                "id": 1,
                "state": True
            },
            {
                "id": 2,
                "state": False
            },
            {
                "id": 3,
                "state": False
            },
            {
                "id": 4,
                "state": True
            }
        ]
    },
    "6": {
        "ac": [
            {
                "id": 1,
                "temp": 19
            },
            {
                "id": 2,
                "temp": 19
            },
            {
                "id": 3,
                "temp": 19
            }
        ],
        "light": [
            {
                "id": 1,
                "state": True
            },
            {
                "id": 2,
                "state": False
            },
            {
                "id": 3,
                "state": False
            },
            {
                "id": 4,
                "state": False
            }
        ]
    },
    "7": {
        "ac": [
            {
                "id": 1,
                "temp": 18
            }
        ],
        "light": [
            {
                "id": 1,
                "state": False
            },
            {
                "id": 2,
                "state": True
            }
        ]
    },
    "8": {
        "ac": [
            {
                "id": 1,
                "temp": 23
            },
            {
                "id": 2,
                "temp": 23
            }
        ],
        "light": [
            {
                "id": 1,
                "state": True
            },
            {
                "id": 2,
                "state": True
            },
            {
                "id": 3,
                "state": True
            },
            {
                "id": 4,
                "state": True
            }
        ]
    }
}

def get_optimization():
    return optimization_applied

def toggle_optimization():
    global optimization_applied
    optimization_applied = not optimization_applied
    return optimization_applied


def get_energy_values():
    hours = dt.now().hour
    energy_values = []

    for i in range(0,hours):
        energy_values.append(ref_energy_values[i])
    
    return energy_values


def get_energy_values_week():
    weeks = int(dt.today().strftime("%U"))

    energy_values = []

    for i in range(0, weeks):
        energy_values.append(ref_energy_values_week[i])

    return energy_values

def get_energy_values_month():
    months = dt.now().month

    energy_values = []

    for i in range(0, months):
        energy_values.append(ref_energy_values_month[i])

    return energy_values


################
# Home functions
################

def get_date():
    return date.today().strftime('%d.%m.%y')

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

## Savings and cost helpers

def get_day_cost():
    current_hour = dt.now().hour
    total_cost = 0

    for i in range(0,current_hour):
        total_cost = total_cost + ref_energy_values[i]
    
    return total_cost

def get_day_savings():
    today_cost = get_day_cost()
    yesterday_cost = get_day_cost() * 1.56

    savings = yesterday_cost - today_cost

    return savings

def get_week_cost():
    current_week = int(dt.today().strftime("%U"))

    return ref_energy_values_week[current_week]

def get_week_savings():
    current_week = int(dt.today().strftime("%U"))

    if current_week > 1:

        current_week_cost = ref_energy_values_week[current_week]
        past_week_cost = ref_energy_values_week[current_week-1]

    else:
        current_week_cost = ref_energy_values_week[current_week]
        past_week_cost = current_week_cost

    savings = past_week_cost - current_week_cost
    savings = savings if savings > 0 else -savings

    return savings

def get_month_cost():
    current_month = dt.now().month

    return ref_energy_values_month[current_month-1]

def get_month_savings():
    current_month = dt.now().month - 1

    print("current_month val")
    print(ref_energy_values_month[current_month])
    print("past_month val")
    print(ref_energy_values_month[current_month-1])


    if current_month > 1:

        print("month is greater than 1")
        current_month_cost = ref_energy_values_month[current_month]
        past_month_cost = ref_energy_values_month[current_month-1]
    
    else:
        current_month_cost = ref_energy_values_month[current_month]
        past_month_cost = current_month_cost

    savings = past_month_cost - current_month_cost
    savings = savings if savings > 0 else -savings        
    
    return savings


## Comparision helpers


def get_compare_day():
    current_hour = dt.now().hour
    
    if current_hour == 1:
        return {
            "0": ref_energy_values[current_hour-1],
            "-1": 0,
            "-2": 0,
        }
    
    elif current_hour == 2:
        return {
            "0": ref_energy_values[current_hour-1],
            "-1": ref_energy_values[current_hour-2],
            "-2": 0,
        }
    
    else:
        return {
            "0": ref_energy_values[current_hour-1],
            "-1": ref_energy_values[current_hour-2],
            "-2": ref_energy_values[current_hour-3],
        }

def get_compare_week():
    current_week = int(dt.today().strftime("%U"))

    if current_week == 1:
        return {
            "0": ref_energy_values_week[current_week-1],
            "-1": 0,
            "-2": 0,
        }
    
    elif current_week == 2:
        return {
            "0": ref_energy_values_week[current_week-1],
            "-1": ref_energy_values_week[current_week-2],
            "-2": 0,
        }
    
    else:
        return {
            "0": ref_energy_values_week[current_week-1],
            "-1": ref_energy_values_week[current_week-2],
            "-2": ref_energy_values_week[current_week-3],
        }

def get_compare_month():
    current_month = dt.now().month

    if current_month == 1:
        return {
            "0": ref_energy_values_month[current_month-1],
            "-1": 0,
            "-2": 0,
        }
    
    elif current_month == 2:
        return {
            "0": ref_energy_values_month[current_month-1],
            "-1": ref_energy_values_month[current_month-2],
            "-2": 0,
        }
    
    else:
        return {
            "0": ref_energy_values_month[current_month-1],
            "-1": ref_energy_values_month[current_month-2],
            "-2": ref_energy_values_month[current_month-3],
        }
    

###################
# Admin functions
###################

def get_room_actuator_info(room_no):
    return rooms.get(room_no)

def change_ac(room_no, ac_id, increase):
    room = rooms.get(str(room_no))
    acs = room.get("ac")
    for ac in acs:
        if(ac['id'] == ac_id):
            if increase == "True":
                ac["temp"] = ac["temp"] + 1
            else:
                ac["temp"] = ac["temp"] - 1

            return ac["temp"]
    
    return None


def change_light(room_no, light_id):
    room = rooms.get(str(room_no))
    lights = room.get("light",[])
    for light in lights:
        if(light['id'] == light_id):
            light['state'] = not light['state']
        return light['state']

    return None