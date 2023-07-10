employee =[
    {"name":"John","salary":3000,"designation":"developer"},
      {"name":"Emma","salary":4000,"designation":"manager"},
  {"name":"Kelly","salary":3500,"designation":"tester"},
]

def max_slary_employee(employee):
    max=0
    str={}
    for i in range(len(employee)):
      if employee.salary > max:
           str=employee.salary
       
      return str

result=max_slary_employee(employee)
print(result)
    


