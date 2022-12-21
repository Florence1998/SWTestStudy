# 人类
class Human:
    pass


# 学生类
class Student(Human):
    pass


# 老师类
class Teacher(Human):
    pass


# 检查实例与类的关系
stu = Student()
print(isinstance(stu, Human))  # 将会打印 True

# 检查类与类的关系
print(issubclass(Student, Human))  # 将会打印 True
print(issubclass(Student, Teacher))  # 将会打印 False
