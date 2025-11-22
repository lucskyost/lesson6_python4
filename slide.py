# import streamlit as st

# name = st.text_input('Họ và tên')
# if st.button('Xác nhận',"1"):
#     st.write('Xin chào', name)


# import streamlit as st
# import time

# st.title('my progress')
# my_bar = st.progress(50)

# for percent_complete in range(100):
#     time.sleep(0.05)
#     my_bar.progress(percent_complete + 1)


import streamlit as st
st.balloons()
if st.button('Click me'):
    st.balloons()