class Student:
    def __init__(self, studentId, name, dateOfBirth, course, branch):
        self.id = studentId
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.course = course
        self.branch = branch

    def getAverage(self, subjectList, transcriptList):
        totalScore = 0
        totalCredit = 0

        for transcript in transcriptList:
            if transcript.studentId.lower() == self.id.lower():
                # Tìm môn học tương ứng để lấy số tín chỉ
                for subject in subjectList:
                    if subject.id.lower() == transcript.subjectId.lower():
                        totalScore += transcript.score * subject.credit
                        totalCredit += subject.credit
                        break

        if totalCredit == 0:
            return 0

        return totalScore / totalCredit

    # Lấy gpa tích luỹ
    def getGPA4(self, subjectList, transcriptList):
        totalScore = 0
        totalCredit = 0
        for transcript in transcriptList:
            if transcript.studentId.lower() == self.id.lower():
                for subject in subjectList:
                    if subject.id.lower() == transcript.subjectId.lower():
                        # Điểm bằng hệ 4 * tính chỉ
                        totalScore += transcript.getScore4() * subject.credit
                        totalCredit += subject.credit
                        break
        if totalCredit == 0:
            return 0
        # Tính gpa
        return totalScore / totalCredit

    def __str__(self):
        return (f"{self.id:<12} {self.name:<20} {str(self.dateOfBirth.strftime('%d/%m/%Y')):<12} {self.course:<10} {self.branch:<20}")