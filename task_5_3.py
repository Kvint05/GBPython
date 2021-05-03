tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Светлана', 'Георгий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def my_gen():
    tutors_1 = (el for el in tutors)
    klasses_1 = (el for el in klasses)
    for _school in zip(klasses_1,
                       tutors_1):
        yield _school[::-1]
    for rest in tutors_1:
        yield rest, None


my_gener = my_gen()
for item in my_gener:
    print(item)
