from flask import Flask, jsonify

from utils import (
    get_date, 
    get_location, 
    get_energy_values,
    get_energy_values_week, 
    get_energy_values_month
    get_room_info
)

app = Flask(__name__)


################
# Home endpoints
################


@app.route('/home', methods=['GET'])
def home():
    _response = {
        "date": get_date(),
        "location": get_location(),
        "energy_values": get_energy_values(),
        "initial_room_info": get_room_info(0)
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
    _response = get_energy_values()
    return jsonify(_response)

@app.route('/history/week', methods=['GET'])
def history_week():
    _response = get_energy_values_week()
    return jsonify(_response)

@app.route('/history/month', methods=['GET'])
def history_month():
    _response = get_energy_values_month()
    return jsonify(_response)
