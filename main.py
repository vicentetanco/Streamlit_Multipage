import streamlit as st
from SessionState import get


st.set_page_config(
    page_title="Title",
    page_icon='icon.png',
    layout="wide",
    initial_sidebar_state="expanded")



session_state = get(password='')

if session_state.password != 'password1' and session_state.password != 'password2':
    col1111, mid, col2111 = st.columns([2, 1, 2])
    logo = mid.empty()
    logo.image('logo.jpg',use_column_width=True)
    pwd_placeholder = mid.empty()
    pwd = pwd_placeholder.text_input("Password:", value="", type="password")
    session_state.password = pwd
    if session_state.password == 'password1':
        pwd_placeholder.empty()
        logo.empty()
        main()
    elif session_state.password == 'password2':
        pwd_placeholder.empty()
        logo.empty()
        main_lite()
    elif session_state.password != '':
        st.error("the password you entered is incorrect")
        with st.expander("Olvide mi contraseña"):
            st.write('Please contact Vicente Tanco  :  VTanco@nordex-online.com')
elif session_state.password == 'password1':
    main()
elif session_state.password == 'password2':
    main_lite()

hide_streamlit_style = """ 
            <style> 
            #MainMenu {visibility: hidden;} 
            footer {visibility: hidden;} 
            </style> 
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

