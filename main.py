import streamlit as st
import pandas as pd
st.title('تطبيق إدارة المخزن')
product_name = st.text_input('اسم المنتج')
quantity = st.number_input('الكمية', min_value=0)
if st.button('حفظ البيانات'):
    st.write(f'تم حفظ {product_name} بالكمية {quantity}')
    st.success('تم الإرسال بنجاح!')
