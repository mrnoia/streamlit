import streamlit as st


def index(selected):
    st.title(f"You have selected {selected}")
    st.write("Hello ,I am learning how to build a streamlit app")
    st.markdown(
        "if you wonder where the sidebar icons comes from [check here](https://icons.getbootstrap.com/)"
    )
    st.caption("I am a caption and below is some code")
    st.code(
        """if selected == 'Home':
    x = 2022"""
    )
    st.latex(r""" a+a r^1+a r^2+a r^3 """)
    st.subheader("testing how to search a list and print the result")
    list = ["find", "item", "in", "list"]
    user_input = st.text_input("Enter search item below")
    st.write(list)
    if user_input in list:
        st.write(f"I found ' {user_input} ' in the list")
    else:
        st.write("not found")
