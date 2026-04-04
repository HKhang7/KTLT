from rank import Rank
class Transcript:
    def __init__(self, studentId, subjectId, score):
        self.studentId = studentId
        self.subjectId = subjectId
        self.score = score

    # Lấy điểm hệ 4
    def getScore4(self):
        if self.score >= Rank.A_PLUS.value:
            return 4.0
        elif self.score >= Rank.A.value:
            return 3.8
        elif self.score >= Rank.B_PLUS.value:
            return 3.5
        elif self.score >= Rank.B.value:
            return 3.0
        elif self.score >= Rank.C_PLUS.value:
            return 2.5
        elif self.score >= Rank.C.value:
            return 2.0
        elif self.score >= Rank.D_PLUS.value:
            return 1.5
        elif self.score >= Rank.D.value:
            return 1.0
        else:
            return 0.0

    def __str__(self):
        return f"{self.studentId:<12} {self.subjectId:<12} {self.score}"