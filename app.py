from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

from utils import (
    get_date, 
    get_location, 
    get_energy_values,
    get_energy_values_week, 
    get_energy_values_month,
    get_compare_day,
    get_compare_week,
    get_compare_month,
    get_day_cost,
    get_day_savings,
    get_week_cost,
    get_week_savings,
    get_month_cost,
    get_month_savings,
    get_room_info,
    get_room_actuator_info,
    change_ac,
    change_light,
    get_optimization
)

app = Flask(__name__)
mongo = PyMongo(app)

################
# Home endpoints
################


@app.route('/home', methods=['GET'])
def home():
    _response = {
        "date": get_date(),
        "location": get_location(),
        "energy_values": get_energy_values(),
        "initial_room_info": get_room_info(0),
        "optimization": get_optimization()
    }

    return jsonify(_response)

@app.route('/home/room/<string:room_no_str>', methods=['GET'])
def home_room_info(room_no_str):
    room_no = int(room_no_str)
    
    if room_no not in range(0,8):
        _response =  {
            "temperature": 0,
            "cost": 0
        }
    else:
        _response =  get_room_info(room_no)
    
    return jsonify(_response)


###################
# History endpoints
###################

@app.route('/history/day', methods=['GET'])
def history_day():
    _response = {
        "values": get_energy_values(),
        "cost": get_day_cost(),
        "savings": get_day_savings(),
        "compare": get_compare_day()
    }
    return jsonify(_response)

@app.route('/history/week', methods=['GET'])
def history_week():
    _response = {
        "values": get_energy_values_week(),
        "cost": get_week_cost(),
        "savings": get_week_savings(),
        "compare": get_compare_week()
    }
    return jsonify(_response)

@app.route('/history/month', methods=['GET'])
def history_month():
    _response = {
        "values": get_energy_values_month(),
        "cost": get_month_cost(),
        "savings": get_month_savings(),
        "compare": get_compare_month()
    }
    return jsonify(_response)

###################
# Admin endpoints
###################

@app.route('/admin/initialise', methods=['GET'])
def admin_initialise():
    _response = {
        "date": get_date(),
        "location": get_location()
    }
    return jsonify(_response)

@app.route('/admin/room/<string:room_no>', methods=['GET'])
def admin_room_info(room_no):
    _response = get_room_actuator_info(room_no)
    return jsonify(_response)

@app.route('/admin/room/change/ac/', methods=['POST'])
def admin_change_ac():
    request_data = request.get_json()
    
    room_no = request_data['room_no']
    ac_id = request_data['ac_id']
    increase = request_data['increase']
   
    new_temp = change_ac(room_no, ac_id, increase)

    if new_temp is not None:
        _response = {
            "status": True,
            "temp":new_temp
            }
    else:
        _response = {
            "status": False
        }

    return jsonify(_response)


@app.route('/admin/room/change/light/', methods=['POST'])
def admin_change_light():
    request_data = request.get_json()
    
    room_no = request_data['room_no']
    light_id = request_data['light_id']
   
    new_state = change_light(room_no, light_id)

    if new_state is not None:
        _response = {
            "status": True,
            "state":new_state
            }
    else:
        _response = {
            "status": False
        }

    return jsonify(_response)

app.run(port=3000, debug=True)