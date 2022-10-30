import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd


def index(selected):
    st.title(f"{selected}")
    st.markdown(
        """#### [Installation docs](https://github.com/PablocFonseca/streamlit-aggrid) and [here](https://streamlit-aggrid.readthedocs.io/en/docs/Usage.html#simple-use) also many examples by Pablo Fonseca can by found in the [Streamlit Ag-Grid app](https://pablocfonseca-streamlit-aggrid-examples-example-jyosi3.streamlitapp.com/)
        """
    )

    st.subheader("1 Grid from CSV file imported into a pandas df")

    df = pd.read_csv(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv"
    )
    st.markdown(
        "The data in this example comes from [this CSV file](https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv)"
    )

    st.write(f"shape:{df.shape}")
    st.write(f"columns:{df.columns}")
    # df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    options_builder = GridOptionsBuilder.from_dataframe(df)
    # options_builder.configure_column("col1", editable=True)
    options_builder.configure_selection("single")
    options_builder.configure_pagination(
        paginationAutoPageSize=False, paginationPageSize=10
    )
    grid_options = options_builder.build()
    grid_return = AgGrid(df, grid_options)
    selected_rows = grid_return["selected_rows"]
    st.write(selected_rows)
