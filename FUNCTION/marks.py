# def grade(marks):
#     if marks >= 90:
#         return 'A+'
#     elif marks >= 80:
#         return 'A'
#     elif marks >= 70:
#         return 'B+'
#     elif  marks >= 60:
#         return 'B'
#     elif marks >= 60:
#         return 'C'
#     elif marks >= 50:
#         return 'D'
#     else:
#         return 'F'
# print(grade(90))  
# print(grade(65))
# print(grade(65)) 
# print(grade(55))
# print(grade(45)) 

def grade(marks):
    grade_mapping = {
        range(90, 100): 'A+',
        range(80, 90): 'A',
        range(70, 80): 'B+',
        range(60, 70): 'B',
        range(50, 60): 'C',
        range(40, 50): 'D',
    }

    for mark_range, grade_value in grade_mapping.items():
        if marks in mark_range:
            return grade_value
    return 'F'


print(grade(90))
print(grade(65))   
print(grade(55))   
print(grade(45))   
print(grade(35))   
