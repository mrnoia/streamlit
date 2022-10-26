import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np


def streamlit_sidebar(orientation="vertical"):
    # build the navigation sidebar
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",  # required
            options=["Home", "Pandas", "Markdown"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation=orientation,
        )
        return selected


def streamlit_menu():
    selected1 = option_menu(
        menu_title=None,  # required
        options=["Home", "Pandas", "Markdown"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )


selected = streamlit_sidebar(orientation="vertical")
# selected1 = streamlit_menu()

if selected == "Home":
    st.title(f"You have selected {selected}")
    list = ["find", "item", "in", "list"]
    user_input = st.text_input("Enter search item below")
    st.write(list)
    if user_input in list:
        st.write(f"I found ' {user_input} ' in the list")
    else:
        st.write("not found")


if selected == "Pandas":
    st.title(f"You have selected {selected}")

    df = pd.DataFrame(np.random.randn(7, 5), columns=("col %d" % i for i in range(5)))
    # displaying the dataframe as an interactive object
    st.write("Displaying the dataframe in a static manner")
    st.table(df)
    st.write("Displaying the dataframe as an interactive object")
    st.dataframe(df, 1200, 500)
    st.dataframe(df.style.highlight_max(axis=0))

if selected == "Markdown":
    st.title(f"You have selected {selected}")
    st.markdown("# this is a markdown Heading level 1")
    st.markdown("## this is a markdown Heading level 2")
    st.markdown("1. this is a markdown list")
    st.markdown("2. this is a markdown lis")
    st.markdown("Check markdown syntax [here](https://www.markdownguide.org/)")


# st.sidebar.title("Python")
# st.sidebar.title("CSS")
# st.sidebar.subheader("this is the subheader")
# st.write("Hello ,let's learn how to build a streamlit app together")
# st.title("this is the app title")
# st.header("this is the markdown")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r""" a+a r^1+a r^2+a r^3 """)
