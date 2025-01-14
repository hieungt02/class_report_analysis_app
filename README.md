# Class Report Analysis Application

/HOW TO RUN/

Download the files and keep the dataset file and the applicationtest.py in the same folder

Run command: **streamlit run applicationtest.py**



--------------------
English:

Dataset used: file py4ai-score.csv

My dataset includes columns: NAME, GENDER, CLASS, PYTHON-CLASS, S1 to S10, BONUS, GPA, REG-MC4AI

Analyzed data:
- From CLASS, I made a new column CLASS_GROUP to divide the students to 10 groups: Math, Informatics, Physics, Chemistry, English, Literature, Japanese/Chinese, Bilingual, Other

The project has 3 main functionalities:
1. Data filtering:
- Allows display of the original data/part of the original data
- Filters so that users can get the desired group of students. Options for filter include: Gender (F/M), Class (114-S, 114-C, 115-S, 115-C), Group (10 groups mentioned above), Grade (10/11), and GPA
- Download function for the filtered data

2. Charts to assess students:
- 3 main categories:
    - Number of students:
      Pie charts showing the ratio of students based on Gender, Python-Class, and Groups
      Insights from the charts (in Vietnamese)
    - Grades:
      Box charts representing student grades (ASM-Average, Midterm, Final, and GPA) based on Gender, Python-Class, and Groups
      Insights from the charts (in Vietnamese)
    - Pass/Fail rates:
      Allows user to choose the GPA that decides Pass/Fail of students
      Based on the GPA chosen, show a pie charts showing the ratio of students who passed/failed
      Display a list of students who passed/failed

3. Classification:
- Allows choosing the number of groups the user would like to separate the students
- Utilized KMeans clustering from scikit-learn to separate/categorize the students
- A 3D scatter displaying the students' grades (ASM-Average, Final, GPA)
- List of students in each group + highest/lowest/average scores of each group and a download function for each group

-----------------
Vietnamese:

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

