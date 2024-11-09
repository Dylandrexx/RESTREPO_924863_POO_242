from models.student import Student
from models.professor import Professor

person_1 = Student(
    name="Luis",
    lastname="Diaz",
    age=25,
    code=957511
)

print(person_1.sayHello())

professor_1=Professor(
    name="Felipe",
    lastname="Diaz",
    age=28

)

print(professor_1.sayHello())