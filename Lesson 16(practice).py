class Employee:

    def __init__(self, name, salary, working_days):
        self.name = name
        self.salary = salary
        self.working_days = working_days

    def work(self):
        return 'I come to the office.'

    def check_salary(self):
        salary = self.salary
        working_days = self.working_days
        return salary * working_days


class Candidate:
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
        return


class Programmer(Employee):

    def __init__(self, name, salary, working_days, tech_stack):
        self.tech_stack = tech_stack
        super().__init__(name, salary, working_days)

    def work(self):
        emp_work = super().work()[:-1]
        emp_check_salary = super().check_salary()
        return f"{emp_work}  and start coding. I have earned : {emp_check_salary} $"

    def __str__(self):
        name = self.name
        return f"Programmer: {name}"


tech_stack = ['JavaScript', 'Python', 'C++', 'PHP', 'SQL', 'Java']


class Programmer2(Employee):

    def __init__(self, name, salary, working_days, tech_stack):
        self.tech_stack = tech_stack
        super().__init__(name, salary, working_days)

    def work(self):
        emp_work = super().work()[:-1]
        emp_check_salary = super().check_salary()
        return f"{emp_work}  and start coding. I have earned : {emp_check_salary} $"

    def __str__(self):
        name = self.name
        return f"Programmer_2 : {name}"


class SuperProgrammer(Programmer, Programmer2):
    pass


class Recruiter(Employee):

    def work(self):
        return f"{super().work()[:-1]} and start hiring. I have earned : {self.check_salary()} $"

    def __str__(self):
        return f"Recruiter : {self.name}"


if __name__ == '__main__':
    emp = Employee('Own', 300, 14)
    prog = Programmer('John', 1500, 9, 'Python')
    recr = Recruiter('Jack', 500, 14)

    emp.work()
    emp.__str__()
    prog.work()
    prog.__str__()
    recr.work()
    recr.__str__()

    print(prog.work())
