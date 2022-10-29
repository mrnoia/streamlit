import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components


def index(selected):
    st.title(f"{selected}")
    st.subheader("st.markdown")
    st.code(
        """st.markdown("Use  markdown syntax to create a link:[check makdown syntax here](https://www.markdownguide.org/basic-syntax/)")"""
    )
    st.markdown(
        "Use  markdown syntax to create a link:[check makdown syntax here](https://www.markdownguide.org/basic-syntax/)"
    )
    st.subheader("st.code")
    st.code(
        '''st.code(
        """def my_function():
    return""",
        language="python")'''
    )
    st.code(
        """def my_function():
    return""",
        language="python",
    )
    st.subheader("st.caption")
    st.code('st.caption("I am a caption")')
    st.caption("I am a caption")

    st.subheader("st.write")
    st.write("some generic text")

    st.subheader("st.latex")
    st.latex(r""" a+a r^1+a r^2+a r^3 """)

    st.subheader("st.text_input")
    user_input = st.text_input("input box label")

    st.subheader("st.columns")

    st.code(
        """
        col1, col2, col3 =  st.columns([1, 1, 1])

    with col1:
        st.header("img1")
        st.image("https://picsum.photos/300/300")

    with col2:
        st.header("img2")
        st.image("https://picsum.photos/300/300")

    with col3:
            st.header("img3")
            st.image("https://picsum.photos/300/300")
            """
    )
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.header("img1")
        st.image("https://picsum.photos/300/300")

    with col2:
        st.header("img2")
        st.image("https://picsum.photos/300/300")

    with col3:
        st.header("img3")
        st.image("https://picsum.photos/300/300")

    col1, col2 = st.columns([2, 1])
    data = np.random.randn(10, 5)

    col1.subheader("A wide column with a chart")
    col1.line_chart(data)

    col2.subheader("A narrow column with the data")
    col2.write(data)

    df = pd.DataFrame(
        data={"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}, index=["a", "b", "c"]
    )
    # df = df.reset_index(drop=True)
    table = df.to_numpy()
    st.write(df)

    st.button("Click me")
    st.checkbox("I agree")
    st.radio("Pick one", ["cats", "dogs"])
    st.selectbox("Pick one", ["cats", "dogs"])
    st.multiselect("Buy", ["milk", "apples", "potatoes"])
    st.slider("Pick a number", 0, 100)
    st.select_slider("Pick a size", ["S", "M", "L"])
    st.text_input("First name")
    st.number_input("Pick a number", 0, 10)
    st.text_area("Text to translate")
    st.date_input("Your birthday")
    st.time_input("Meeting time")
    st.file_uploader("Upload a CSV")
    st.camera_input("Take a picture")
    st.color_picker("Pick a color")
    st.markdown("Cheat Sheet [here](https://docs.streamlit.io/library/cheatsheet)")
    # bootstrap 4 collapse example
    components.html(
        """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
        height=600,
    )
