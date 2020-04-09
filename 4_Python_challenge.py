grade_one= {
    'Sami': [19, 18, 19.5, 30, 10],
    'Ahmad': [15, 14, 16, 21, 7],
    'Faris': [18, 19, 17, 26, 9],
    'Salem': [20, 20, 19, 30, 10],
    'Mahmoud': [12, 13, 11, 18, 7]
}

grade_two= {
    'Lana': [17, 19, 20, 28, 9],
    'Dina': [18.5, 19.5, 20, 29,10],
    'Maha': [20, 20, 18, 26, 9],
    'Abeer': [16, 18, 19.5, 25, 8]
}

grade_three= {
    'Rima': [18, 19, 18, 26, 9],
    'Tala': [20, 20, 19, 29, 10],
    'Lamar': [19, 20, 18, 26, 9],
    'Rola': [15, 14, 16, 19, 7],
    'Naya': [9, 6, 11, 14, 7],
    'Dalal': [1, 5, 2, 6, 7],
    'Ola': [19.5, 20, 20, 29.5, 10]
}
def students_names(class_name):
    list = []
    for i in class_name:
        list.append(i)
    return list

def student_score(class_name , student_name ):
    name = class_name[student_name]
    scour = sum(name)
    return student_name , scour
def student_count(class_name):
    count = len(class_name.keys())
    return  count


question = "more"
condition = {"more" : 0 , "done" :1}
condition1 = condition["more"]
choices = {"students_names": students_names , "student_score" : student_score , "students_count" : student_count}
grads = {"grade_one": grade_one, "grade_two": grade_two , "grade_three":grade_three}

while condition1 == 0 :
    choice = (input("Choose one: students_names, student_score, students_count: ")).lower()
    grade = input("grade_number (grade_one , grade_two or grade_three) :").lower()
    logic1 = choice in choices
    logic2 = grade in grads
    if logic1 == True and logic2 == True :
        x = choices[choice]
        y = grads[grade]
        if choice == "students_names":
            print("The names of the students in "+ grade + " are: " , str(x(y)))
            condition1 = condition[input("if you want to stop, write -done-, and if you want to continue, write -more-: ")]
        elif choice == "students_count":
            print("The number of students in " + grade + " are: ", x(y))
            condition1 = condition[
            input("if you want to stop, write -done-, and if you want to continue, write -more-: ")]
        elif choice == "student_score":
            student_name = input("Enter Student Name : ")
            logic3 = student_name in y
            if logic3 == True:
                print(student_name ," Score is: " ,sum(y[student_name]))
                condition1 = condition[input("if you want to stop, write -done-, and if you want to continue, write -more-: ")]
            else:
                print("The name of the student is wrong")
                condition1 = condition[
                    input("if you want to stop, write -done-, and if you want to continue, write -more-: ")]
    else:
        print("Wrong input")
        condition1 = condition[input("if you want to stop, write -done-, and if you want to continue, write -more-: ")]