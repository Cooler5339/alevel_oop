
std = {'Alex': 51, 'Bob': 66, 'Jango': 87, 'James': 87}
n = std.keys()
n = len(n)
point = sum(std.values())
avrg_grades = point / n
print("Средний балл студентов: " + str(int(avrg_grades)))
print('Студенты с баллом выше среднего: ')
for i in std:
    if std[i] > avrg_grades:
        print(i)
print("Студенты с баллом ниже среднего:")
for i in std:
    if std[i] < avrg_grades:
        print(i)
