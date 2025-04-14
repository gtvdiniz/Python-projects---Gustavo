class Employee: 
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id 
        self.emp_name = emp_name 
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        self.horas_trabalhadas = int(input("Informe o número de horas trabalhadas:"))
        
        
    def print_employee_details(self): 
        print(f'\nId : {self.emp_id}\nNome : {self.emp_name}\n Salário: {self.emp_salary}\nDepartamento : {self.emp_department}')
        
    
    def calcule_emp_salary(self): 
             if self.horas_trabalhadas > 50: 
                horas_extras = self.horas_trabalhadas - 50
                valor_horasextras =1.5 *  (horas_extras * (self.emp_salary / 50))
                print(f'O valor das horas extras é {valor_horasextras}\nO valor do total do salário ficou {valor_horasextras + self.emp_salary}\n')
             else: pass 
             
    
    def assign_department(self): 
        novo_dep = input("Insira aqui o novo departamento: ")
        self.emp_department = novo_dep 
        
 
    
emp1 = Employee("UZZI", "E7876", 50000, "CONTABILIDADE")
emp2 = Employee("JOÃO", "E7499", 45000, "PESQUISA")
emp3 = Employee("SALVADOR", "E7900", 50000, "VENDAS")
emp4 = Employee("DENIS", "E7698", 55000, "OPERAÇÕES")

emp1.print_employee_details()
emp1.calcule_emp_salary()

emp2.print_employee_details()
emp2.calcule_emp_salary()

emp3.print_employee_details()
emp3.calcule_emp_salary()

emp4.print_employee_details()
emp4.calcule_emp_salary()



emp1.assign_department()
emp1.print_employee_details()