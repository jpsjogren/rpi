from flask import Flask, request, jsonify, Response
from water import *

app = Flask(__name__)


@app.route('/', methods=['PUT'])
def query_records():

    # Starta vattning
    time = request.args.get('time')
    pin = request.args.get('pin')
    print(type(pin))
    print(pin)
    print("--------")
    try:
        time = int(time)
        pin = int(pin)
    except:
       time = 5
       pin = 21
    print(type(pin))
    print(time)
    response = watering(time, pin)
    return Response(status=response)

@app.route('/', methods=['GET'])
def update_record():
    # Är det färdigt?
    # dict = getStatus()

    return Response(status=200)

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

'''
@app.route('/', methods=['GET'])
def index():
    # Är det färdigt?
    dict = watering()
   #  dict = {"test": "GET"}
    return jsonify(dict)

'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
