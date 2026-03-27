'''
Hệ thống Quản lý và Phân tích Kết quả Học tập Sinh viên

Chương trình quản lý sinh viên viết bằng Python, hỗ trợ lưu trữ dữ liệu qua file CSV, tìm kiếm, sắp xếp và phân tích kết quả học tập.

Cấu trúc file project/
├── main.py           # Logic chính, menu, CRUD, tìm kiếm, sắp xếp, phân tích
├── student.py        # Class Student
├── subject.py        # Class Subject
├── transcript.py     # Class Transcript
├── rank.py           # Enum Rank (xếp loại học lực)
├── students.csv      # Dữ liệu sinh viên (tự tạo khi lưu lần đầu)
├── subjects.csv      # Dữ liệu môn học (tự tạo khi lưu lần đầu)
└── transcripts.csv   # Dữ liệu bảng điểm (tự tạo khi lưu lần đầu)

Chức năng:
1. Quản lý sinh viên
2. Quản lý môn học
3. Quản lý bảng điểm
4. Tìm kiếm sinh viên
5. Sắp xếp sinh viên
6. Phân tích học tập
'''