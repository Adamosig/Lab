groupmates = [
    {
        "name": "Артем",
        "surname": "Кузнецов",
        "exams": ["Программирование", "Математика", "Физика"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Дарья",
        "surname": "Новикова",
        "exams": ["Английский", "История", "Литература"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Никита",
        "surname": "Морозов",
        "exams": ["Химия", "Биология", "Экология"],
        "marks": [4, 3, 4]
    },
    {
        "name": "София",
        "surname": "Лебедева",
        "exams": ["Экономика", "Право", "Обществознание"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Владислав",
        "surname": "Егоров",
        "exams": ["Информатика", "Алгоритмы", "Web"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Алиса",
        "surname": "Павлова",
        "exams": ["Дизайн", "Графика", "Мультимедиа"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Роман",
        "surname": "Степанов",
        "exams": ["Сети", "Безопасность", "Базы данных"],
        "marks": [4, 4, 3]
    }
]

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(12), "Экзамены".ljust(35), "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(12), str(student["exams"]).ljust(35), str(student["marks"]).ljust(20))


def filter(students, min_average):
    return [student for student in students if sum(student["marks"]) / len(student["marks"]) > min_average]

print_students(groupmates)
print()
print_students(filter(groupmates, float(input("Введи ср балл для фильтра: "))))
