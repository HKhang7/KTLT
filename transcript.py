class Transcript:
    def __init__(self, studentId, subjectId, score):
        self.studentId = studentId
        self.subjectId = subjectId
        self.score = score

    def __str__(self):
        return f"{self.studentId:<12} {self.subjectId:<12} {self.score}"