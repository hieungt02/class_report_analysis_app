import numpy as np
import pandas as pd
import streamlit as st

url = f"https://docs.google.com/spreadsheets/d/152-kU15YDY-UxcZHzva3ZhGzjMcGZL3qHRS9VC7_u8I/edit?usp=sharing"
df = pd.read_csv(url, dtype=str)

#print(df)
#print(df.isna().sum())

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


#print(df.isna().sum())

CLASS_GROUP = []
for i in df.index:
  if "CTIN" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Chuyên Tin')
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
  elif "CTRN" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Trung Nhật')
  elif "CSD" in df.loc[i, 'CLASS']:
    CLASS_GROUP.append('Sử Địa')
  elif ("TH" in df.loc[i, 'CLASS']) or ("SN" in df.loc[i, 'CLASS']):
    CLASS_GROUP.append('Tích Hợp/Song Ngữ')
  else:
    CLASS_GROUP.append('Khác')
df['CLASS_GROUP'] = CLASS_GROUP
#print(df)

st.title(':PURPLE[BẢNG ĐIỂM LỚP PY4AI]')
st.dataframe(df)
