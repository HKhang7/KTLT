import csv
import os
from datetime import date, datetime
from student import Student
from subject import Subject
from transcript import Transcript
from rank import Rank

# Chỗ lưu và lấy file
STUDENTS_FILE = "students.csv"
SUBJECTS_FILE = "subjects.csv"
TRANSCRIPTS_FILE = "transcripts.csv"
EXIT_CHOICE = 0
def loadData(studentList, subjectList, transcriptList):
    # Đọc sinh viên
    # Nếu có file sẽ đọc ko sẽ rỗng
    if os.path.exists(STUDENTS_FILE):
        # mở file, newline ngăn lỗi xuống dòng, utf 8 là kiểu mã, f là tên biến
        with open(STUDENTS_FILE, newline='', encoding='utf-8') as f:
            # lấy dòng đầu làm key và xem như dict
            reader = csv.DictReader(f)
            # lấy từng dòng
            for row in reader:
                #Chuyển kiểu date
                dateOfBirth = datetime.strptime(row['dateOfBirth'], '%d/%m/%Y').date()
                # them vao ds
                studentList.append(Student(
                    row['id'], row['name'], dateOfBirth,
                    row['course'], row['branch']
                ))

    # Đọc môn học
    if os.path.exists(SUBJECTS_FILE):
        with open(SUBJECTS_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                subjectList.append(Subject(
                    row['id'], row['name'], int(row['credit'])
                ))

    # Đọc bảng điểm
    if os.path.exists(TRANSCRIPTS_FILE):
        with open(TRANSCRIPTS_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                transcriptList.append(Transcript(
                    row['studentId'], row['subjectId'], float(row['score'])
                ))

def saveData(studentList, subjectList, transcriptList):
    # Ghi sinh viên
    with open(STUDENTS_FILE, 'w', newline='', encoding='utf-8') as f:
        # Các cột
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'dateOfBirth', 'course', 'branch'])
        # gắn header
        writer.writeheader()
        for s in studentList:
            # viết từng dòng
            writer.writerow({
                'id': s.id,
                'name': s.name,
                'dateOfBirth': s.dateOfBirth.strftime('%d/%m/%Y'),
                'course': s.course,
                'branch': s.branch
            })

    # Ghi môn học
    with open(SUBJECTS_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'credit'])
        writer.writeheader()
        for s in subjectList:
            writer.writerow({'id': s.id, 'name': s.name, 'credit': s.credit})

    # Ghi bảng điểm
    with open(TRANSCRIPTS_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['studentId', 'subjectId', 'score'])
        writer.writeheader()
        for transcript in transcriptList:
            writer.writerow({'studentId': transcript.studentId, 'subjectId': transcript.subjectId, 'score': transcript.score})

    print("Đã lưu dữ liệu!")
# Hàm nhập input số
def inputInteger():
    while True:
        try:
            num = int(input("Nhập số: "))
        except ValueError:
            print("Số phải là số nguyên dương")
            continue
        return num

# Hàm delay sau khi xuất dữ liệu
def pressEnterToContinue():
    input("\nNhấn enter để tiếp tục! ")

# Hàm in ds kết quả
def printList(result):
    if result:
        for student in result:
            print(student)
    else:
        print("Không tìm thấy sinh viên!")
    pressEnterToContinue()

# Hàm xem list có bị trống k
def isTheListEmpty(lst):
    # Nếu lst trống sẽ ra True
    return len(lst) == 0

# Hàm xem input có rỗng k
def isInputEmpty(inp):
    return inp == ""

# Hàm giới hạn kí tự
def isStringOutLength(string, amount):
    if len(string) > amount:
        print(f"Giới hạn là {amount} kí tự!")
        return True
    return False

# Hàm in heading student
def printStudentHeading():
    print(f"{"MSSV":<12} {"Họ và Tên":<20} {"Ngày sinh":<12} {"Lớp":<10} {"Ngành"}")
    return

def inputBirthDay():
    while True:
        try:
            day = int(input("Nhập ngày sinh: "))
            month = int(input("Nhập tháng sinh: "))
            year = int(input("Nhập năm sinh (Phải lớn hơn 1920): "))
            # Ngăn sinh viên quá già/ trẻ
            minYear = 1920
            # sinh viên ít nhất 16 tuổi
            maxYear = date.today().year - 16
            if year > minYear and year <= maxYear:
                return date(year, month, day)
            else:
                print("Năm sinh không hợp lệ! Vui lòng nhập lại!")
                continue
        except ValueError:
            print("Ngày sinh không hợp lệ, nhập lại!")

# Hàm lấy sinh viên/ môn học có Id đó
def findById(lst, id = None):
    if id is None:
        id = input("Nhập Id cần tìm: ").strip().lower()
    sorted_list = sortById(lst, False)

    # dùng binary search (chia đôi) để tìm nhanh hơn
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        currentId = sorted_list[mid].id.lower()

        if currentId == id.lower():
            return sorted_list[mid]
        elif currentId < id.lower():
            left = mid + 1
        else:
            right = mid - 1
    return None

def addTranscript(transcriptList, studentList, subjectList):
    # Bảng điểm phải có sinh viên và môn đã tồn tại
    studentId = input("Nhập mã sinh viên: ").strip()
    if not findById(studentList, studentId):
        print("Không tìm thấy sinh viên!")
        pressEnterToContinue()
        return

    subjectId = input("Nhập mã môn học: ").strip()
    if not findById(subjectList, subjectId):
        print("Không tìm thấy môn học!")
        pressEnterToContinue()
        return

    for t in transcriptList:
        if t.studentId.lower() == studentId.lower() and t.subjectId.lower() == subjectId.lower():
            print("Sinh viên đã có điểm môn này rồi!")
            return

    while True:
        try:
            studentScore = float(input("Nhập điểm sinh viên: "))
            if 0 <= studentScore <= 10:
                break
            else:
                print("Điểm phải từ 0-10")
        except ValueError:
            print("Điểm lỗi, hãy nhập lại!")

    transcriptList.append(Transcript(studentId, subjectId, studentScore))
    print("Thêm thành công!")
    pressEnterToContinue()

def updateTranscript(transcriptList):

    if isTheListEmpty(transcriptList):
        print("Chưa có dữ liệu")
        pressEnterToContinue()
        return
    # Dùng mssv và mã môn để ra bảng điểm
    studentId = input("Nhập MSSV muốn tìm: ").strip()
    subjectId = input("Nhập mã môn học muốn tìm: ").strip()

    for transcript in transcriptList:
        if transcript.studentId.lower() == studentId.lower() and transcript.subjectId.lower() == subjectId.lower():
            print("Đã tìm thấy bảng điểm!")

            while True:
                try:
                    studentScore = float(input("Nhập điểm sinh viên: "))
                    if 0 <= studentScore <= 10:
                        transcript.score = studentScore
                        print("Cập nhật thành công!")
                        return
                    else:
                        print("Điểm phải từ 0-10")
                except ValueError:
                    print("Điểm lỗi, hãy nhập lại!")

    print("Không tìm thấy bảng điểm!")
    pressEnterToContinue()

def transcriptManager(studentList, subjectList, transcriptList):
    while True:
        print("\n-- Quản lý bảng điểm --")
        print("1. Thêm bảng điểm")
        print("2. Sửa điểm")
        print("3. Xem bảng điểm")
        print("0. Quay lại")

        ADD_TRANSCRIPT_CHOICE = 1
        UPDATE_TRANSCRIPT_CHOICE = 2
        PRINT_TRANSCRIPT_CHOICE = 3
        
        choice = inputInteger()
        
        if choice == ADD_TRANSCRIPT_CHOICE:
            addTranscript(transcriptList, studentList, subjectList)
        elif choice == UPDATE_TRANSCRIPT_CHOICE:
            updateTranscript(transcriptList)
        elif choice == PRINT_TRANSCRIPT_CHOICE:
            if isTheListEmpty(transcriptList):
                print("Chưa có dữ liệu")
                pressEnterToContinue()
                continue
            print(f"{"MSSV":<12} {"Mã môn":<12} {"Điểm"}")
            # sort ds cho dễ nhìn
            printList(mergeSortList(transcriptList, sortBy=lambda s: s.studentId.lower(), inPlace=False))
        elif choice == EXIT_CHOICE:
            break
        else:
            print("Lựa chọn không hợp lệ!")

def updateTranscriptOfStudent(transcriptList, oldId, newId):
    for transcript in transcriptList:
        if transcript.studentId.lower() == oldId.lower():
            transcript.studentId = newId

def updateTranscriptOfSubject(transcriptList, oldId, newId):
    for transcript in transcriptList:
        if transcript.subjectId.lower() == oldId.lower():
            transcript.subjectId = newId

def deleteTranscriptOfStudent(lst, id):
    if isTheListEmpty(lst):
        return

# do duyệt xuôi sẽ nhảy ptu nên sẽ duyệt ngược
    for i in range(len(lst) - 1, -1, -1):
        if lst[i].studentId.lower() == id.lower():
            lst.pop(i)

def deleteTranscriptOfSubject(lst, id):
    if isTheListEmpty(lst):
        return

# do duyệt xuôi sẽ nhảy ptr nên sẽ duyệt ngược
    for i in range(len(lst) - 1, -1, -1):
        if lst[i].subjectId.lower() == id.lower():
            lst.pop(i)

def addStudent(studentList):
    # Nhập MSSV
    while True:
        studentId = input("Nhập mã số sinh viên: ").strip()
        if isInputEmpty(studentId):
            print("MSSV không được bỏ trống")
            continue
        if len(studentId) != 11:
            print("MSSV phải đúng 11 kí tự")
            continue
        if not studentId.isdigit():
            print("MSSV chỉ được chứa chữ số!")
            continue
        if findById(studentList, studentId):
            print("MSSV đã tồn tại!")
            continue
        break

    # Nhập tên
    while True:
        name = input("Nhập tên sinh viên: ").strip()
        if isInputEmpty(name):
            print("Tên không được để trống!")
            continue
        if isStringOutLength(name, 20):
            continue
        break

    # Nhập ngày sinh
    dateOfBirth = inputBirthDay()

    # Nhập lớp
    while True:
        course = input("Nhập lớp: ").strip()
        if isInputEmpty(course):
            print("Lớp không được để trống!")
            continue
        if isStringOutLength(course, 8):
            continue
        break

    # Nhập ngành
    while True:
        branch = input("Nhập ngành: ").strip()
        if isInputEmpty(branch):
            print("Ngành không được để trống!")
            continue
        if isStringOutLength(branch, 20):
            continue
        break

    studentList.append(Student(studentId, name, dateOfBirth, course, branch))
    print("Thêm thành công!")
    pressEnterToContinue()

def updateStudentList(studentList, transcriptList):
    if isTheListEmpty(studentList):
        print("Chưa có dữ liệu")
        pressEnterToContinue()
        return

    studentId = input("Nhập MSSV của sinh viên cần tìm: ")
    student = findById(studentList, studentId)
    if student is None:
        print("Không tìm thấy MSSV")
        pressEnterToContinue()
        return
    print("Đã tìm thấy sinh viên!")

    while True:
        print("Chọn thông tin muốn cập nhật: ")
        print("1. Sửa MSSV")
        print("2. Sửa tên")
        print("3. Sửa ngày sinh")
        print("4. Sửa lớp")
        print("5. Sửa ngành")
        print("0. Thoát")

        
        UPDATE_STUDENT_ID_CHOICE = 1
        UPDATE_STUDENT_NAME_CHOICE = 2
        UPDATE_STUDENT_BIRTHDAY_CHOICE = 3
        UPDATE_STUDENT_COURSE_CHOICE = 4
        UPDATE_STUDENT_BRANCH_CHOICE = 5

        choice = inputInteger()
        
        if choice == EXIT_CHOICE:
            return
        
        elif choice == UPDATE_STUDENT_BIRTHDAY_CHOICE:
            student.dateOfBirth = inputBirthDay()
            print("Cập nhật hoàn tất!")
            continue

        new = input("Nhập thông tin mới: ").strip()
        if isInputEmpty(new):
            print("Không được bỏ trống")
            continue

        if choice == UPDATE_STUDENT_ID_CHOICE:
            if len(new) != 11:
                print("MSSV phải đúng 11 kí tự")
                continue
            if findById(studentList, new):
                print("MSSV trùng!")
                continue
            updateTranscriptOfStudent(transcriptList, student.id, new)
            student.id = new
            print("Cập nhật hoàn tất!")
            
        elif choice ==  UPDATE_STUDENT_NAME_CHOICE:
            if isStringOutLength(new, 20):
                continue
            student.name = new
            print("Cập nhật hoàn tất!")
            
        elif choice == UPDATE_STUDENT_COURSE_CHOICE:
            if isStringOutLength(new, 8):
                continue
            student.course = new
            print("Cập nhật hoàn tất!")
            
        elif choice ==  UPDATE_STUDENT_BRANCH_CHOICE:
            if isStringOutLength(new, 20):
                continue
            student.branch = new
            print("Cập nhật hoàn tất!")

def deleteStudent(studentList, transciptList):
    if isTheListEmpty(studentList):
        print("Chưa có dữ liệu")
        pressEnterToContinue()
        return

    studentId = input("Nhập MSSV của sinh viên cần xoá: ")
    student = findById(studentList, studentId)

    if student is None:
        print("Không tìm thấy MSSV")
        pressEnterToContinue()
        return

    studentList.remove(student)
    deleteTranscriptOfStudent(transciptList, studentId)
    print("Đã xoá!")
    pressEnterToContinue()

def studentManager(studentList, transcriptList = None):
    while True:
        print("\n-- Quản lý sinh viên --")
        print("1. Thêm sinh viên")
        print("2. Cập nhật sinh viên")
        print("3. Xoá sinh viên")
        print("4. Hiển thị danh sách sinh viên")
        print("0. Quay lại")

        ADD_STUDENT_CHOICE = 1
        UPDATE_STUDENT_CHOICE = 2
        DELETE_STUDENT_CHOICE = 3
        PRINT_STUDENT_LIST_CHOICE = 4
        choice = inputInteger()

        if choice == ADD_STUDENT_CHOICE:
            addStudent(studentList)
        elif choice == UPDATE_STUDENT_CHOICE:
            updateStudentList(studentList, transcriptList)
        elif choice == DELETE_STUDENT_CHOICE:
            deleteStudent(studentList, transcriptList)
        elif choice == PRINT_STUDENT_LIST_CHOICE:
            if isTheListEmpty(studentList):
                print("Chưa có dữ liệu")
                pressEnterToContinue()
                continue
            print("Danh sách sinh viên: ")
            print(
                f"{"MSSV":<12} {"Họ và Tên":<20} {"Ngày sinh":<12} {"Lớp":<10} {"Ngành"}")
            printList(studentList)
        elif choice == EXIT_CHOICE:
            break
        else:
            print("Lựa chọn không hợp lệ!")


def addSubject(subjectList):
    # Thêm mã môn học
    while True:
        subjectId = input("Nhập mã môn học: ").strip()
        if isInputEmpty(subjectId):
            print("Mã môn không được bỏ trống")
            continue
        if isStringOutLength(subjectId, 12):
            continue
        if findById(subjectList, subjectId):
            print("Mã môn học đã tồn tại!")
            continue
        break

    # Thêm tên môn học
    while True:
        subjectName = input("Nhập tên môn học: ").strip()
        if isInputEmpty(subjectName):
            print("Tên không được để trống!")
            continue
        if isStringOutLength(subjectName, 20):
            continue
        break

    # Thêm số tín chỉ
    while True:
        credit = inputInteger()
        if credit <= 0:
            print("Số tín chỉ phải lớn hơn 0!")
            continue
        break

    subjectList.append(Subject(subjectId, subjectName, credit))
    print("Thêm thành công")
    pressEnterToContinue()


def updateSubject(subjectList, transcriptList):
    if isTheListEmpty(subjectList):
        print("Chưa có dữ liệu")
        pressEnterToContinue()
        return

    subjectId = input("Nhập mã môn học cần sửa: ")
    subject = findById(subjectList, subjectId)
    if subject is None:
        print("Không tìm thấy môn học!")
        pressEnterToContinue()
        return
    print(" Đã tìm thấy mã môn học cần sửa")

    while True:
        print("Chọn thông tin muốn cập nhật")
        print("1. Sửa mã môn học")
        print("2. Sửa tên môn học")
        print("3. Sửa số tín chỉ")
        print("0. Thoát ra")

       
        UPDATE_ID_CHOICE = 1
        UPDATE_NAME_CHOICE = 2
        UPDATE_CREDIT_CHOICE = 3
        choice = inputInteger()

        if choice == UPDATE_ID_CHOICE:
            newSubjectId = input("Nhập mã môn học mới: ").strip()
            if isInputEmpty(newSubjectId):
                print("Mã môn không được để trống!")
                continue
            # Kiểm tra xem mã mới đã tồn tại ở môn khác chưa
            if findById(subjectList, newSubjectId):
                print("Mã môn học đã tồn tại, không thể đổi!")
                continue
            elif isStringOutLength(newSubjectId, 12):
                continue
            updateTranscriptOfSubject(transcriptList, subjectId, newSubjectId)
            subject.id = newSubjectId
            print("Cập nhật mã môn thành công!")
        elif choice == UPDATE_NAME_CHOICE:
            new = input("Nhập tên môn học mới: ").strip()
            if isInputEmpty(new):
                print("Tên không được để trống!")
                continue
            if isStringOutLength(new, 20):
                continue
            subject.name = new
            print("Cập nhật tên thành công!")
        elif choice == UPDATE_CREDIT_CHOICE:
            while True:
                try:
                    newCredit = int(input("Nhập số tín chỉ mới: "))
                    if newCredit > 0:
                        subject.credit = newCredit
                        print("Cập nhật tín chỉ thành công!")
                        break
                    else:
                        print("Số tín chỉ phải lớn hơn 0!")
                except ValueError:
                    print("Lỗi! Số tín chỉ phải là số nguyên.")
        elif choice == EXIT_CHOICE:
            print("Cập nhật hoàn tất!")
            return
        else:
            print("Lựa chọn không hợp lệ!")


def deleteSubject(subjectList, transcriptList):
    if isTheListEmpty(subjectList):
        print("Chưa có dữ liệu")
        pressEnterToContinue()
        return

    subjectId = input("Nhập mã môn học cần xoá: ").strip()
    subject = findById(subjectList, subjectId)
    if subject is None:
        print("Không tìm thấy mã môn học này!")
        pressEnterToContinue()
        return
    subjectList.remove(subject)
    deleteTranscriptOfSubject(transcriptList, subjectId)
    print("Đã xoá môn học thành công!")
    pressEnterToContinue()
    return

def subjectManager(subjectList, transcriptList):
    while True:
        print("\n-- Quản lý môn học --")
        print("1. Thêm môn học")
        print("2. Cập nhật môn học")
        print("3. Xoá môn học")
        print("0. Quay lại")

        ADD_SUBJECT_CHOICE = 1
        UPDATE_SUBJECT_CHOICE = 2
        DELETE_SUBJECT_CHOICE = 3
        choice = inputInteger()

        if choice == ADD_SUBJECT_CHOICE:
            addSubject(subjectList)
        elif choice == UPDATE_SUBJECT_CHOICE:
            updateSubject(subjectList, transcriptList)
        elif choice == DELETE_SUBJECT_CHOICE:
            deleteSubject(subjectList, transcriptList)
        elif choice == EXIT_CHOICE:
            break
        else:
            print("Lựa chọn không hợp lệ!")

# Các mục sắp xếp, inplace là chọn có đổi list gốc hay ko
def mergeSortList(lst, sortBy=lambda x: x, inPlace=True, reverse=False):
    # List 1 ptu trở xuống k cần sort v cũng để nó trả ptu cho việc merge
    if len(lst) <= 1:
        return lst
    # Chia đôi
    mid = len(lst) // 2
    # Tách list
    left = mergeSortList(lst[:mid], sortBy, reverse=reverse)
    right = mergeSortList(lst[mid:], sortBy, reverse=reverse)
    # Gộp list
    sorted_result = mergeList(left, right, sortBy, reverse)

    # Nếu false sẽ ko đổi list gốc
    if inPlace:
        # Ghi đè để đổi list gốc
        lst[:] = sorted_result
    return sorted_result

# Gộp list
def mergeList(left, right, sortBy, reverse=False):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Lấy giá trị của key để so sánh
        leftValue = sortBy(left[i])
        rightValue = sortBy(right[j])
        # reverse = True thì xếp từ lớn -> bé (Lấy bên trái)
        # so sánh i vs j cái nào lớn hơn sẽ ghép vào và bỏ qua nó, khi còn 1 ptu sẽ extend
        if (leftValue > rightValue) if reverse else (leftValue < rightValue):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sortByName(studentList, inPlace=True):
    return mergeSortList(
        studentList,
        sortBy=lambda s: s.name.lower(),
        inPlace=inPlace)

def sortById(studentList, inPlace = True):
    return mergeSortList(
        studentList,
        sortBy=lambda s: s.id.lower(),
        inPlace=inPlace)

def sortByAverage(studentList, subjectList, transcriptList, inPlace=True, reverse=True):
    # reverse là true để xếp điểm từ cao -> thấp
    return mergeSortList(
        studentList,
        # sort theo điểm tb
        sortBy = lambda s: s.getAverage(subjectList, transcriptList),
        inPlace = inPlace,
        reverse = reverse
)

def sortStudentList(studentList, subjectList = None, transcriptList = None):
    if isTheListEmpty(studentList):
        print("Chưa có dữ liệu")
        pressEnterToContinue()
        return

    while True:
        print("Bạn muốn sắp xếp theo")
        print("1. Tên sinh viên")
        print("2. MSSV")
        print("3. Điểm trung bình")
        print("0. Quay lại")

        NAME_STUDENT_CHOICE = 1
        ID_STUDENT_CHOICE = 2
        AVERAGE_SCORE_CHOICE = 3
        choice = inputInteger()

        if choice == NAME_STUDENT_CHOICE:
            sortByName(studentList)
            print("Đã sắp xếp")
            return
        elif choice == ID_STUDENT_CHOICE:
            sortById(studentList)
            print("Đã sắp xếp")
            return
        elif choice == AVERAGE_SCORE_CHOICE:
            if transcriptList is None:
                print("Chưa có dữ liệu điểm!")
                return
            sortByAverage(studentList, subjectList, transcriptList)
            print("Đã sắp xếp")
            return
        elif choice == EXIT_CHOICE:
            break

def findByCourse(studentList):
    # Phải dùng linear search vì có thể có nhiều người trùng dữ liệu
    result = []
    course = input("Nhập lớp của sinh viên muốn tìm: ").strip()
    for student in studentList:
        if student.course.lower() == course.lower():
            result.append(student)
    return result


def findByName(studentList):
    # Phải dùng linear search vì có thể có nhiều người trùng dữ liệu
    result = []
    name = input("Nhập tên của sinh viên muốn tìm: ").strip()

    for student in studentList:
        if student.name.lower() == name.lower():
            result.append(student)
    return result


def findByBranch(studentList):
    # Phải dùng linear search vì có thể có nhiều người trùng dữ liệu
    result = []
    branch = input("Nhập ngành của sinh viên muốn tìm: ").strip()
    for student in studentList:
        if student.branch.lower() == branch.lower():
            result.append(student)
    return result


def findStudent(studentList):
    if isTheListEmpty(studentList):
        print("Chưa có dữ liệu")
        pressEnterToContinue()
        return

    while True:
        print("Bạn muốn tìm theo: ")
        print("1. Theo MSSV")
        print("2. Theo lớp")
        print("3. Theo tên")
        print("4. Theo ngành")
        print("0. Quay lại")

        ID_STUDENT_CHOICE = 1
        COURSE_CHOICE = 2
        NAME_CHOICE = 3
        BRANCH_CHOICE = 4
        choice = inputInteger()

        if choice == ID_STUDENT_CHOICE:
            student = findById(studentList)
            if student:
                printStudentHeading()
                print(student)
                pressEnterToContinue()
            else:
                print("Không tìm thấy sinh viên!")
                pressEnterToContinue()
        elif choice == COURSE_CHOICE:
            printStudentHeading()
            printList(findByCourse(studentList))
        elif choice == NAME_CHOICE:
            printStudentHeading()
            printList(findByName(studentList))
        elif choice == BRANCH_CHOICE:
            printStudentHeading()
            printList(findByBranch(studentList))
        elif choice == EXIT_CHOICE:
            break
        else:
            print("Không có chức năng này!")

# Hàm in ds có điểm và stt
def printStudentRank(resultList, subjectList, transcriptList):
    print(f"{"STT":<4}{"MSSV":<12} {"Họ và Tên":<20} {"Ngày sinh":<12} {"Lớp":<10} {"Ngành":<20} {"Điểm"}")
    for i in range(len(resultList)):
        print(
            f"{i + 1:<4}{resultList[i].id:<12} {resultList[i].name:<20} {resultList[i].dateOfBirth.strftime('%d/%m/%Y'):<12} {resultList[i].course:<10} {resultList[i].branch:<20} {resultList[i].getAverage(subjectList, transcriptList):.2f}")
    pressEnterToContinue()

def getAverage(studentList, subjectList, transcriptList):
    student = findById(studentList)
    if student is None:
        print("Không tìm thấy sinh viên!")
        return
    # getAverage là phương thức trong class và chỉ cần truyền transcriptList
    print(f"Điểm trung bình của sinh viên {student.name} là {student.getAverage(subjectList, transcriptList)}")
    pressEnterToContinue()

def findTopStudents(studentList, subjectList, transcriptList):
    # lấy danh sách điểm từ lớn -> bé
    sortedList = sortByAverage(studentList, subjectList, transcriptList, False)
    topStudents = []
    # Gắn ptu đầu vào vì nó là đứa có điểm cao nhất
    topStudents.append(sortedList[0])
    # So sánh từ ptu thứ 2 vì đã chắc ptu 1 là cao nhất
    for i in range(1, len(sortedList)):
        # Nếu điểm bằng cao nhất thì nó cũng cao nhất
        if sortedList[i].getAverage(subjectList, transcriptList) == sortedList[0].getAverage(subjectList, transcriptList):
            topStudents.append(sortedList[i])
        else:
            break
    return topStudents

def findBottomStudents(studentList, subjectList, transcriptList):
    # lấy danh sách điểm từ bé -> lớn
    sortedList = sortByAverage(studentList, subjectList, transcriptList, False, False)
    bottomStudents = []
    # Gắn ptu đầu vào vì nó là đứa có điểm thấp nhất
    bottomStudents.append(sortedList[0])
    for i in range(1, len(sortedList)):
        # So sánh từ ptu thứ 2 vì đã chắc ptu thứ 1 là thấp nhất
        if sortedList[i].getAverage(subjectList, transcriptList) == sortedList[0].getAverage(subjectList, transcriptList):
            bottomStudents.append(sortedList[i])
        else:
            break
    return bottomStudents

def findTopKStudents(studentList, subjectList, transcriptList):
    sortedList = sortByAverage(studentList, subjectList, transcriptList, False)  # chuyển ra ngoài
    while True:
        try:
            amount = int(input("Nhập số lượng sinh viên top cần tìm: "))
            if amount < 1:
                print("Vui lòng nhập số nguyên dương hơn 0")
                continue
            elif amount > len(sortedList):
                print(f"Chỉ có {len(sortedList)} sinh viên!")
                continue
        except ValueError:
            print("Vui lòng nhập số nguyên dương hơn 0")
            continue
        # Xuất danh sách 0 -> amount
        return sortedList[:amount]

# thống kê học lực theo hệ 4
def learningStat(studentList, subjectList, transcriptList):
    EXCELLENT_MIN_SCORE = 3.6
    GOOD_MIN_SCORE = 3.2
    FAIR_MIN_SCORE = 2.5
    AVERAGE_MIN_SCORE = 2.0
    WEAK_MIN_SCORE = 1.0

    amountOfExcellent = 0
    amountOfGood = 0
    amountOfFair = 0
    amountOfAverage = 0
    amountOfWeak = 0
    amountOfPoor = 0

    for student in studentList:
        gpa4 = student.getGPA4(subjectList, transcriptList)
        if gpa4 >= EXCELLENT_MIN_SCORE:
            amountOfExcellent += 1
        elif gpa4 >= GOOD_MIN_SCORE:
            amountOfGood += 1
        elif gpa4 >= FAIR_MIN_SCORE:
            amountOfFair += 1
        elif gpa4 >= AVERAGE_MIN_SCORE:
            amountOfAverage += 1
        elif gpa4 >= WEAK_MIN_SCORE:
            amountOfWeak += 1
        else:
            amountOfPoor += 1

    print(f"""
Số lượng Xuất sắc là {amountOfExcellent}
Số lượng Giỏi là {amountOfGood}
Số lượng Khá là {amountOfFair}
Số lượng Trung bình là {amountOfAverage}
Số lượng Yếu là {amountOfWeak}
Số lượng Kém là {amountOfPoor}
""")
    pressEnterToContinue()

def analyseLearningStat(studentList, subjectList, transcriptList):
    # Phải có dữ liệu 2 list mới thống kê được
    if isTheListEmpty(studentList) or isTheListEmpty(transcriptList):
        print("Chưa có đủ dữ liệu!")
        return

    while True:
        print("Bạn muốn: ")
        print("1. Tính điểm trung bình của 1 bạn")
        print("2. Tìm sinh viên có điểm cao nhất")
        print("3. Tìm sinh viên có điểm thấp nhất")
        print("4. Tìm top k sinh viên")
        print("5. Thống kê học lực")
        print("0. Quay lại")

        AVCERAGE_SOCRE_CHOICE = 1
        FIND_TOP_STUDENT_CHOICE = 2
        FIND_BOTTOM_STUDENT_CHOICE = 3
        FIND_TOPK_STUDENT_CHOICE = 4
        LEARNING_STAT_CHOICE = 5
        choice = inputInteger()

        if choice == AVCERAGE_SOCRE_CHOICE:
            getAverage(studentList, subjectList, transcriptList)

        elif choice == FIND_TOP_STUDENT_CHOICE:
            result = findTopStudents(studentList, subjectList, transcriptList)
            printStudentRank(result, subjectList, transcriptList)

        elif choice == FIND_BOTTOM_STUDENT_CHOICE:
            result = findBottomStudents(studentList, subjectList, transcriptList)
            printStudentRank(result, subjectList, transcriptList)

        elif choice == FIND_TOPK_STUDENT_CHOICE:
            result = findTopKStudents(studentList, subjectList, transcriptList)
            printStudentRank(result, subjectList, transcriptList)

        elif choice == LEARNING_STAT_CHOICE:
            learningStat(studentList, subjectList, transcriptList)

        elif choice == EXIT_CHOICE:
            break
        else:
            print("Không có chức năng này!")
            pressEnterToContinue()

def printMainMenu():
    print("\n===== MENU =====")
    print("1. Quản lý sinh viên")
    print("2. Quản lý môn học")
    print("3. Quản lý điểm")
    print("4. Tìm sinh viên")
    print("5. Sắp xếp sinh viên")
    print("6. Phân tích tình hình học tập")
    print("0. Thoát")

def mainChoice(studentList, subjectList, transcriptList):
    loadData(studentList, subjectList, transcriptList)
    while True:
        printMainMenu()

        STUDENT_MANAGER_CHOICE = 1
        SUBJECT_MANAGER_CHOICE = 2
        TRANSCRIPT_MANAGER_CHOICE = 3
        FIND_STUDENT_CHOICE = 4
        SORT_STUDENT_LIST_CHOICE = 5
        ANALYSE_LEARNING_STAT_CHOICE = 6
        choice = inputInteger()

        if choice == STUDENT_MANAGER_CHOICE:
            studentManager(studentList, transcriptList)
        elif choice == SUBJECT_MANAGER_CHOICE:
            subjectManager(subjectList, transcriptList)
        elif choice == TRANSCRIPT_MANAGER_CHOICE:
            transcriptManager(studentList, subjectList, transcriptList)
        elif choice == FIND_STUDENT_CHOICE:
            findStudent(studentList)
        elif choice == SORT_STUDENT_LIST_CHOICE:
            sortStudentList(studentList, subjectList, transcriptList)
        elif choice == ANALYSE_LEARNING_STAT_CHOICE:
            analyseLearningStat(studentList, subjectList, transcriptList)
        elif choice == EXIT_CHOICE:
            print("Thoát chương trình.")
            saveData(studentList, subjectList, transcriptList)
            break
        else:
            print("Chức năng chưa làm hoặc không hợp lệ!")
            pressEnterToContinue()

def main():

    # tạo chỗ chứa
    studentList = []
    subjectList = []
    transcriptList = []
    mainChoice(studentList, subjectList, transcriptList)

main()