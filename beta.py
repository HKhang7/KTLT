
# Thống kê học lực theo abcd
# def learningStat(studentList, subjectList, transcriptList):
#     amountOfAPlus = 0
#     amountOfA = 0
#     amountOfBPlus = 0
#     amountOfB = 0
#     amountOfCPlus = 0
#     amountOfC = 0
#     amountOfDPlus = 0
#     amountOfD = 0
#     amountOfF = 0
#
#     # Đếm số điểm từng sinh viên
#     for student in studentList:
#         score = student.getAverage(subjectList, transcriptList)
#         if score >= Rank.A_PLUS.value:
#             amountOfAPlus += 1
#         elif score >= Rank.A.value:
#             amountOfA += 1
#         elif score >= Rank.B_PLUS.value:
#             amountOfBPlus += 1
#         elif score >= Rank.B.value:
#             amountOfB += 1
#         elif score >= Rank.C_PLUS.value:
#             amountOfCPlus += 1
#         elif score >= Rank.C.value:
#             amountOfC += 1
#         elif score >= Rank.D_PLUS.value:
#             amountOfDPlus += 1
#         elif score >= Rank.D.value:
#             amountOfD += 1
#         else:
#             amountOfF += 1
#     print(f"""
# Số lượng A+ là {amountOfAPlus}
# Số lượng A là {amountOfA}
# Số lượng B+ là {amountOfBPlus}
# Số lượng B là {amountOfB}
# Số lượng C+ là {amountOfCPlus}
# Số lượng C là {amountOfC}
# Số lượng D+ là {amountOfDPlus}
# Số lượng D là {amountOfD}
# Số lượng F là {amountOfF}
# """)
#     pressEnterToContinue()

# Thống kê học lực theo hệ 10
# def learningStat(studentList, subjectList, transcriptList):
#     amountOfExcellent = 0
#     amountOfGood = 0
#     amountOfAverage = 0
#     amountOfWeak = 0
#     amountOfPoor = 0
#
#     # Đếm số điểm từng sinh viên
#     for student in studentList:
#         score = student.getAverage(subjectList, transcriptList)
#         if score >= Rank.A.value:
#             amountOfExcellent += 1
#         elif score >= Rank.B.value:
#             amountOfGood += 1
#         elif score >= Rank.C.value:
#             amountOfAverage += 1
#         elif score >= Rank.D.value:
#             amountOfWeak += 1
#         else:
#             amountOfPoor += 1
#     print(f"""
# Số lượng sinh viên học lực Giỏi là {amountOfExcellent}
# Số lượng sinh viên học lực Khá là {amountOfGood}
# Số lượng sinh viên học lực Trung Bình là {amountOfAverage}
# Số lượng sinh viên học lực Trung Bình Yếu là {amountOfWeak}
# Số lượng sinh viên học lực Kém là {amountOfPoor}
# """)
#     pressEnterToContinue()

# # Xem xếp loại
# def getRank(self):
#     if self.score >= Rank.A_PLUS.value:
#         return "A+"
#     elif self.score >= Rank.A.value:
#         return "A"
#     elif self.score >= Rank.B_PLUS.value:
#         return "B+"
#     elif self.score >= Rank.B.value:
#         return "B"
#     elif self.score >= Rank.C_PLUS.value:
#         return "C+"
#     elif self.score >= Rank.C.value:
#         return "C"
#     elif self.score >= Rank.D_PLUS.value:
#         return "D+"
#     elif self.score >= Rank.D.value:
#         return "D"
#     else:
#         return "F"
#
#
# # Chuyển hệ 4
# def getScore4(self):
#     rank = self.getRank()
#     if rank == "A+":
#         return 4.0
#     elif rank == "A":
#         return 3.8
#     elif rank == "B+":
#         return 3.5
#     elif rank == "B":
#         return 3.0
#     elif rank == "C+":
#         return 2.5
#     elif rank == "C":
#         return 2.0
#     elif rank == "D+":
#         return 1.5
#     elif rank == "D":
#         return 1.0
#     else:
#         return 0.0