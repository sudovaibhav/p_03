import emp 
def test_get_employee_details():
    name = "Alice Smith"
    emp_id = "E202"
    department = "HR"
    salary = 60000
    
    expected_output = "Employee Name: Alice Smith, Employee ID: E202, Department: HR, Salary: 60000"
    assert emp.get_employee_details(name, emp_id, department, salary) == expected_output