import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.cluster import KMeans

df = pd.read_csv('/Users/hieu/Documents/untitled folder/py4ai-score.csv')


df['S1'].fillna(0, inplace=True)
df['S2'].fillna(0, inplace=True)
df['S3'].fillna(0, inplace=True)
df['S4'].fillna(0, inplace=True)
df['S5'].fillna(0, inplace=True)
df['S6'].fillna(0, inplace=True)
df['S7'].fillna(0, inplace=True)
df['S8'].fillna(0, inplace=True)
df['S9'].fillna(0, inplace=True)
df['S10'].fillna(0, inplace=True)
df['BONUS'].fillna(0, inplace=True)
df['REG-MC4AI'].fillna('N', inplace=True)




CLASS_GROUP = []
for i in df.index:
  if "CTIN" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Chuyên Tin')
  elif "CTRN" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Trung Nhật')
  elif "CT" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Chuyên Toán')
  elif "CL" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Chuyên Lý')
  elif "CH" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Chuyên Hóa')
  elif "CA" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Chuyên Anh')
  elif "CV" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Chuyên Văn')
  elif "CSD" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Sử Địa')
  elif ("TH" in df.loc[i, 'CLASS']) or ("SN" in df.loc[i, 'CLASS']):
    CLASS_GROUP.append('Tích Hợp/Song Ngữ')
  else:
    CLASS_GROUP.append('Khác')
df['CLASS_GROUP'] = CLASS_GROUP
#print(df)


st.title(':orange[BẢNG ĐIỂM LỚP PY4AI]')

tab1, tab2, tab3 = st.tabs(['Filter','Charts','Classification'])

with tab1:
  display_orgdata = st.checkbox('Display original data')
  if display_orgdata:
    st.dataframe(df)
    datainfo = st.radio(
      "Data info:",
      ('GENDER','PYTHON-CLASS','REG-MC4AI','CLASS_GROUP'))
    st.dataframe(df[datainfo].value_counts(),use_container_width=True)
  st.subheader(':red[Filters:]')
  col1, col2, col3 = st.columns(3)
  with col1:
    option1 = st.multiselect('Gender:',  ['F', 'M'])
  with col2:
    option2 = st.multiselect('Class:', ['114-S', '114-C', '115-S', '115-C'])
  with col3:
    option4 = st.multiselect('Grade:', [10, 11])
  option3 = st.multiselect('Group:', ['Chuyên Toán', 'Chuyên Tin', 'Chuyên Lý','Chuyên Hóa','Chuyên Văn', 'Chuyên Anh', 'Trung Nhật',\
                                    'Sử Địa','Tích Hợp/Song Ngữ','Khác'])
  
  option5 = st.slider('GPA:',0.0,10.0)
  
  if option4 == [10]:
    dfapplied1 = df[(df['GENDER'].isin(option1)) & (df['CLASS_GROUP'].isin(option3)) & (df['PYTHON-CLASS'].isin(option2)) & (df['CLASS'].str.startswith('10'))]
  elif option4 == [11]:
    dfapplied1 = df[(df['GENDER'].isin(option1)) & (df['CLASS_GROUP'].isin(option3)) & (df['PYTHON-CLASS'].isin(option2)) & (df['CLASS'].str.startswith('11'))]
  else:
    dfapplied1 = df[(df['GENDER'].isin(option1)) & (df['CLASS_GROUP'].isin(option3)) & (df['PYTHON-CLASS'].isin(option2))]

  dfapplied2 = dfapplied1[dfapplied1['GPA'] <= option5]
  st.dataframe(dfapplied2)
  st.write('Số học sinh:', len(dfapplied2.index))

  @st.cache_data
  def convert_df(df):
    return df.to_csv().encode('utf-8')

  csv = convert_df(dfapplied2)
  st.download_button(
    label="Download data",
    data=csv,
    file_name='filtered_df.csv',
    mime='text/csv'
  )

df2 = df.copy()
df2['ASM'] = (df2['S1'] + df2['S2'] + df['S3'] + df['S4'] + df['S5'] + df['S7'] + df['S8'] + df['S9'])/8
with tab2:
  tab4, tab5, tab10 = st.tabs(['Students','Grades','Pass/Fail'])
  with tab4:
    figtab41 = px.pie(df, names='GENDER')
    st.plotly_chart(figtab41, use_container_width=True)
    st.info("**Kết luận**: Số lượng học sinh nam (chiếm 61.6%) nhiều hơn\
                học sinh nữ (chiếm 38.4%).")
    
    figtab42 = px.pie(df, names='PYTHON-CLASS')
    st.plotly_chart(figtab42, use_container_width=True)
    st.info("**Kết luận**: Lớp có số học sinh đông nhất là lớp 114-Chiều,\
                song tỷ lệ học sinh các lớp khá đều nhau.")

    figtab43 = px.pie(df, names='CLASS_GROUP')
    st.plotly_chart(figtab43, use_container_width=True)
    st.info("**Kết luận**: Trong các khối lớp chuyên, lớp chuyên Toán có hứng thú\
                với AI nhiều nhất (22,3%), theo sau là chuyên Anh (12,5%).\
             Ngoài ra, các bạn thuộc các lớp không nêu tên ở đây chiếm phần lớn (24,1%).")

  with tab5:
    tab6, tab7, tab8, tab9 = st.tabs(['Assignments', 'Midterm','Final','GPA'])
    with tab6:
      figtab61 = px.box(df2,x='GENDER', y='ASM')
      st.plotly_chart(figtab61, use_container_width=True)
      st.info("**Kết luận**: Học sinh nữ có điểm trung bình các bài Assignment\
              cao hơn các học sinh nam. Bên học sinh nam cũng có nhiều điểm thấp hơn, đặc biệt có điểm 0.")

      figtab62 = px.box(df2,x='PYTHON-CLASS', y='ASM')
      st.plotly_chart(figtab62, use_container_width=True)
      st.info("**Kết luận**: Trong tất cả các lớp thì lớp 114-Sáng có điểm trung bình các bài Assignment\
              cao nhất, lớp 114-Chiều có điểm thấp nhất.")

      figtab63 = px.box(df2,x='CLASS_GROUP', y='ASM')
      st.plotly_chart(figtab63, use_container_width=True)
      st.info("**Kết luận**: Trong các khối lớp, lớp chuyên Tin có điểm TB các Assignment cao nhất,\
              lớp chuyên Anh có điểm TB thấp nhất.")

    with tab7:
      figtab71 = px.box(df2,x='GENDER', y='S6')
      st.plotly_chart(figtab71, use_container_width=True)
      st.info("**Kết luận**: Điểm giữa kì trung bình của các học sinh Nam (9) cao hơn nhiều so với\
              điểm của các học sinh Nữ (7)")

      figtab72 = px.box(df2,x='PYTHON-CLASS', y='S6')
      st.plotly_chart(figtab72, use_container_width=True)
      st.info("**Kết luận**: Trong tất cả các lớp thì lớp 115-Chiều có điểm trung bình giữa kì cao nhất\
            , lớp 115-Sáng có điểm giữa kì thấp nhất.")

      figtab73 = px.box(df2,x='CLASS_GROUP', y='S6')
      st.plotly_chart(figtab73, use_container_width=True)
      st.info("**Kết luận**: Trong các khối lớp, lớp chuyên Tin, Toán và Lý có điểm TB giữa kì cao nhất (9),\
              lớp Tích Hợp/Song Ngữ có điểm TB thấp nhất (5).")


    with tab8:
      figtab81 = px.box(df2,x='GENDER', y='S10')
      st.plotly_chart(figtab81, use_container_width=True)
      st.info("**Kết luận**: Điểm cuối kì trung bình của các học sinh Nam (6) cao hơn so với\
              điểm cuối kì của các học sinh Nữ (5)")

      figtab82 = px.box(df2,x='PYTHON-CLASS', y='S10')
      st.plotly_chart(figtab82, use_container_width=True)
      st.info("**Kết luận**: Trong tất cả các lớp thì lớp 114-Sáng có điểm trung bình cuối kì cao nhất\
              (6.5), lớp 115-Chiều có điểm giữa kì thấp nhất.\
               Ngoài ra thì các lớp đều có điểm trải từ 0-10, trừ lớp 114-Sáng có điểm thấp nhất là 1.")

      figtab83 = px.box(df2,x='CLASS_GROUP', y='S10')
      st.plotly_chart(figtab83, use_container_width=True)
      st.info("**Kết luận**: Lớp chuyên Tin có điểm TB cuối kì cao nhất (9),\
              2 lớp Sử Địa và Trung Nhật có điểm TB thấp nhất (3). \
              Có 5/10 khối lớp có điểm 10 cuối kì.")
    
    with tab9:
      figtab91 = px.box(df,x='GENDER',y='GPA')
      st.plotly_chart(figtab91, use_container_width=True)
      st.info("**Kết luận**: Điểm GPA trung bình của các học sinh Nam (6.9) cao hơn so với\
              điểm GPA của các học sinh Nữ (6.1).")

      figtab92 = px.box(df2,x='PYTHON-CLASS', y='GPA')
      st.plotly_chart(figtab92, use_container_width=True)
      st.info("**Kết luận**: Lớp 114-Sáng có điểm GPA trung bình cao nhất (7.3)\
              , lớp 115-Sáng có điểm GPA trung bình thấp nhất (6.1).")

      figtab93 = px.box(df2,x='CLASS_GROUP', y='GPA')
      st.plotly_chart(figtab93, use_container_width=True)
      st.info("**Kết luận**: Lớp chuyên Tin có điểm GPA trung bình cao nhất (9),\
              lớp Sử Địa có điểm TB thấp nhất (3.825). \
              4/10 khối lớp có điểm GPA trung bình 10, ngoài ra lớp chuyên Văn là lớp có điểm khá đều.")

  with tab10:
    df4 = df.copy()
    pass_grade = st.slider('Mininum GPA to pass:',0.0, 10.00)
    PF = []
    for i in df4.index:
      if df4.loc[i, 'GPA'] >= pass_grade:
        PF.append('Pass')
      else:
        PF.append('Fail')
    df4['Pass/Fail'] = PF
    figtab10 = px.pie(df4, names='Pass/Fail')
    st.plotly_chart(figtab10, use_container_width=True)
    pass_or_fail = ['Pass','Fail']
    studentlist = st.radio('Lists of students:', pass_or_fail)
    if studentlist == 'Pass':
      df5 = df4[df4['Pass/Fail'] == 'Pass']
      df5 = df5[['NAME','GENDER','CLASS','PYTHON-CLASS','GPA']]
      st.dataframe(df5, use_container_width=True)
      st.write('Số học sinh:', len(df5.index))

    else:
      df5 = df4[df4['Pass/Fail'] == 'Fail']
      df5 = df5[['NAME','GENDER','CLASS','PYTHON-CLASS','GPA']]
      st.dataframe(df5, use_container_width=True)
      st.write('Số học sinh:', len(df5.index))



X = np.array(df2[['ASM','S10','GPA']])
with tab3:
  
  cluster = st.select_slider(
    'Number of groups:',
    options=[2, 3, 4, 5, 6, 7, 8, 9, 10])
  kmeans = KMeans(n_clusters=cluster, n_init='auto')
  kmeans.fit(X)
  df2['Nhóm'] = kmeans.labels_.tolist()
  scatter = px.scatter_3d(df2, x=X[:, 0], y=X[:, 1], z=X[:, 2], color=kmeans.labels_)
  st.plotly_chart(scatter)
  st.caption("x-axis: **Assignments**, y-axis: **Final**, z-axis: **GPA**")

  for i in range(cluster):
    df3 = df2[df2['Nhóm']==i]
    stats = np.array(df3['GPA'])
    st.write('(Group', i,')', 'Highest GPA:', np.max(stats),'Lowest GPA:', np.min(stats), 'Average:', np.round_(np.average(stats),1))
    st.dataframe(df3[['NAME','GENDER','CLASS','PYTHON-CLASS','ASM','S10','GPA']],use_container_width=True)
                 

