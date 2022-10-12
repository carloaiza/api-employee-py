from model.employee import Employee


class EmployeeService:
    def __init__(self):
        self.list = []
        self.list.append(Employee("123456","Carlos Loaiza",44))
        self.list.append(Employee("654321", "Pedro Pérez", 24))

    def save_employee(self,employee:Employee):
        self.list.append(employee)
        return "Adicionado con éxito"

    def find_employee_by_id(self,id:str):
        for empl in self.list:
            if empl.identification == id:
                return empl
        return None