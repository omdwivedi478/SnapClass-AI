
import streamlit as st

def footer_home():

    logo_url = "https://i.ibb.co/PZK1LxQB/a-clean-high-resolution-transparent-black-backgr.png"

    st.markdown(f"""
<div style="margin-top: 2rem; display: flex; gap: 10px; justify-content: center; align-items: center;">

<p style="margin: 0; font-size: 18px; color: white;">Created with ❤️ by</p>

<div style="background: #111827; padding: 4px 12px; border-radius: 12px; display: flex; align-items: center;">

<img src="{logo_url}" style="height: 45px; width: auto;">

</div>

</div>
""", unsafe_allow_html=True)
    

import streamlit as st


def footer_dashboard():

    logo_url = "https://i.ibb.co/PZK1LxQB/a-clean-high-resolution-transparent-black-backgr.png"

    st.markdown(f"""
<div style="margin-top: 2rem; display: flex; gap: 10px; justify-content: center; align-items: center;">

<p style="margin: 0; font-size: 18px; color: black;">Created with ❤️ by</p>

<div style="background: #111827; padding: 4px 12px; border-radius: 12px; display: flex; align-items: center;">

<img src="{logo_url}" style="height: 45px; width: auto;">

</div>

</div>
""", unsafe_allow_html=True)
    