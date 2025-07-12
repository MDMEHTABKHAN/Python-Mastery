# variable length keyword arguments

def collect_student_data(*data):
    print(data)
collect_student_data('Mehtab', 23, 60.3, 'M') 


def collect_student_data(**data):
    print(data)
    print(type(data))
collect_student_data(Name = 'Mehtab', age = 23, weight = 60.3, Gender = 'M')   
