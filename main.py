import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# إعدادات الربط
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# تأكد أن هذا الاسم يطابق اسم الملف المرفوع في المستودع
creds = ServiceAccountCredentials.from_json_keyfile_name('seraphic-music-420501-4e1d5407ad4e.json', scope)
client = gspread.authorize(creds)

# تأكد أن اسم ملف الشيت في جوجل درايف هو "Inventory"
sheet = client.open('Inventory').sheet1

st.title('تطبيق إدارة المخزن')

product_name = st.text_input('اسم المنتج')
quantity = st.number_input('الكمية', min_value=0)

if st.button('حفظ البيانات'):
    sheet.append_row([product_name, quantity])
    st.success(f'تم حفظ {product_name} بالكمية {quantity} في جوجل شيت!')
