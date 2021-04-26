class Student:
    def __init__(self, name, gender, Data_sheet, img_url):
        self.name = name
        self.Data_sheet = Data_sheet

    def __str__(self):
        return 'stud_name: {name}, image_url: {image_url} '.format(
        name= self.name, image_url = self.image_url)

    def get_avg_grade(self):
        gradelist = Data_sheet.get_grades_as_list(self.data_sheet)
        print(str(sum(gradelist/len())))
        return sum(gradelist/len()) 


class Data_sheet:
    def __init__(self, courseList = []):
        self.courseList = courseList

    def get_grades_list(self):
        grades_list = []
        for c in self.courseList:
            print(int(c.grade))
            grades.append(c.grade)
        return grades_list

    def __str__(self):
        return 'datasheet {Data_Sheet}'.format(Data_sheet = self.courseList)


class Course:
    def __init__(self, name, classroom, teacher, ects, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = grade

c1 = Course("Hacking", "classroom 2", "HackerMan", 30, 12)
c2 = Course("Programming", "classroom 44", "Programmerman", 25, 10)

d1 = Data_sheet([c1, c2])
s1 = Student("Hackerstudent", "male", d1, "www.google.dk")


print(s1.get_avg_grade)

#print(s1.Data_sheet.get_grades_list)
#print(s1.Data_sheet.courseList)
#print(s1.Data_sheet.get_grades_list)
