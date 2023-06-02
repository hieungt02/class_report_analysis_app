# Hieu_mc4ai_project
Dataset được sử dụng: file py4ai-score.csv
Data gồm các cột NAME, GENDER, CLASS, PYTHON-CLASS, từ S1 đến S10, BONUS, GPA, REG-MC4AI

Các thông tin được phân tích:
- Từ cột Class cho ra cột mới CLASS_GROUP để chia tổng học sinh thành 10 khối lớp bao gồm Chuyên Toán, Tin, Lý, Hoá, Anh, Văn, Sử Địa, Trung Nhật, Tích hợp/Song Ngữ, Khác
- Project gồm 3 chức năng chính:
1. Filter: Lọc Data
  - Cho phép xem data gốc và một số info của data gốc
  - Có các bộ lọc để nguơi dùng có thể lấy ra được danh sách học sinh mong muốn:
    Các bộ lọc gồm: Gender (F/M), Class (114-S, 114-C, 115-S, 115-C), Group (10 khối lớp), Grade(10/11) và GPA
  - Ngoài ra còn có nút download để tải data đã lọc về máy

2. Charts: Biểu đồ
  - Gồm 3 phần chính:
    - Số lượng hoc sinh (Students):
      Biểu đồ pie thể hiện tỉ lệ số lượng học sinh theo:
      Gender, Python-Class và Khối lơp (Group)
      Kết luận từ biểu đồ
    - Điểm (Grades):
      Biểu đồ Box thể hiện điểm (ASM-trung bình, Midterm, Final và GPA) của học sinh theo:
      Gender, Python-Class và Khối lớp (Group)
      Kết luận tư biểu đồ
    - Tỷ lệ đậu/trượt (Pass/Fail):
      Cho phep chọn điểm GPA để xem học sinh pass/fail
      Tuỳ theo điểm mà đưa ra biểu đồ pie thể hiện ti lệ học sinh pass/fail
      Có đi kèm danh sách học sinh pass/fail
      
3. Classification: Phân loại
  - Cho phép lựa chọn số nhóm muốn chia
  - Sử dụng KMeans từ scikit-learn để phân loại học sinh
  - Biểu đồ scatter 3D thể hiện điểm học sinh gồm (TB ASM, Final và GPA)
  - In ra danh sách học sinh của từng nhóm + điểm cao nhất/thấp nhất/trung bình của từng nhóm

