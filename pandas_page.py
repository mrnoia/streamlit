import streamlit as st
import pandas as pd
import numpy as np


def index(selected):
    st.title(f"{selected}")

    st.write("Create a random dataframe")
    st.code(
        """df = pd.DataFrame(np.random.randn(7, 5), columns=("col %d" % i for i in range(5)))"""
    )
    df = pd.DataFrame(np.random.randn(7, 5), columns=("col %d" % i for i in range(5)))

    st.write("Dataframe shape")
    st.code("df.shape()")
    st.write(df.shape)

    st.write("Return the first n rows")
    st.code("df.head(n=5)")
    st.write(df.head(n=5))

    # st.help(df)
    # displaying the dataframe as an interactive object
    st.write("Displaying the dataframe in a static manner")
    st.table(df)
    st.write("Displaying the dataframe as an interactive object")
    st.dataframe(df, 1200, 500)
    st.dataframe(df.style.highlight_max(axis=0))
