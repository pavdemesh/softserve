class Testpaper:

    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self, tests_taken="No tests taken"):
        self.tests_taken = tests_taken

    def take_test(self, paper, answers):
        # initialize variable to hold correct answers
        correct_answers = 0

        # compare answers with markscheme in paper and update correct answers
        for i, ans in enumerate(answers):
            if ans == paper.markscheme[i]:
                correct_answers += 1

        # calculate percentage of correct answers
        correct_percentage = round(correct_answers / len(answers)) * 100

        # calculate verdict Passed or Failed
        pass_threshold = int(paper.pass_mark[:-1])
        verdict = "Passed!" if correct_percentage >= pass_threshold else "Failed!"

        # create dict of tests_taken if no tests were taken so far
        if self.tests_taken == "No tests taken":
            self.tests_taken = {}

        # update dictionary of tests taken
        self.tests_taken[paper.subject] = f"{verdict} ({correct_percentage}%)"


paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
student1 = Student()
student1.take_test(paper1, ['1A', '2C', '3D', '4A', '5A'])
print(student1.tests_taken)
