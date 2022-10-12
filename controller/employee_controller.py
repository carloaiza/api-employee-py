from flask import Response, Blueprint, request
from util.util_encoder import UtilEncoder
import json

from model.employee import Employee
from service.employee_service import EmployeeService

app_employee_controller = Blueprint("app_employee",__name__)

employee_service = EmployeeService()

@app_employee_controller.route("/employee")
def get_list_employees():
    return Response(status=200,
                    response=json.dumps(employee_service.list,cls=UtilEncoder),
                    mimetype="application/json")

@app_employee_controller.route("/employee",methods=["POST"])
def save_employee():
    body = request.json
    if "age" in body:
        new_employee = Employee(body['identification'],body['name'],body['age'])
        return Response(status=200,response= employee_service.
                        save_employee(new_employee), mimetype="application/json")
    else:
        return "El campo age es obligatorio"

@app_employee_controller.route("/employee/<id>")
def get_employee_by_id(id:str):
    employee_find = employee_service.find_employee_by_id(id)
    if employee_find != None:
        return Response(status=200,
                    response=json.dumps(employee_find,cls=UtilEncoder),
                    mimetype="application/json")
    else:
        return Response(status=404,
                        response=json.dumps({"message":"Empleado no existe"}),
                        mimetype="application/json")