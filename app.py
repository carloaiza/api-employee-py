from flask import Flask
from controller.employee_controller import app_employee_controller

app = Flask(__name__)
app.register_blueprint(app_employee_controller)

if __name__ == '__main__':
    app.run()
