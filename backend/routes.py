from config import app, db, jsonify, request
from models import Car, Driver, Garage

@app.route('/', methods=['GET'])
def index():
  return 'Sistema de cadastro de Carros<br>' +\
    '<a href="/index-cars">Veja os carros cadastrados aqui</a>'


@app.route('/index_cars', methods=['GET'])
def index_cars():
  cars = db.session.query(Car).all()

  json_cars = [_.json() for _ in cars]
  response = jsonify(json_cars)
  response.headers.add("Access-Control-Allow-Origin", "*")

  return response


@app.route('/create_car', methods=['POST'])
def create_car():
  response = jsonify({"result": "success", "details": "ok"})

  data = request.get_json()

  try:
    new_car = Car(**data)
    db.session.add(new_car)
    db.session.commit()
  except Exception as e:
    response = jsonify({"result": "error", "details": str(e)})

  response.headers.add("Access-Control-Allow-Origin", "*")

  return response


@app.route('/delete_car/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
  response = jsonify({"result": "success", "details": "ok"})

  try:
    Car.query.filter(Car.id == car_id).delete()
    db.session.commit()

  except Exception as e:
    response = jsonify({"result": "error", "details": str(e)})

  response.headers.add("Access-Control-Allow-Origin", "*")

  return response


@app.route('/index_drivers', methods=['GET'])
def index_drivers():
  drivers = db.session.query(Driver).all()

  json_drivers = [_.json() for _ in drivers]
  response = jsonify(json_drivers)
  response.headers.add("Access-Control-Allow-Origin", "*")

  return response


@app.route('/index_garages', methods=['GET'])
def index_garages():
  garages = db.session.query(Garage).all()

  json_garages = [_.json() for _ in garages]
  response = jsonify(json_garages)
  response.headers.add("Access-Control-Allow-Origin", "*")

  return response