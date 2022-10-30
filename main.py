import streamlit as st
from streamlit_option_menu import option_menu
import home_page, pandas_page, streamlit_page, aggrid_page

# from  main import views

st.set_page_config(
    page_title="Streamlit application",
    page_icon="👋",
    layout="wide",
)
menu_ops_icons = {
    "Home": "house",
    "Streamlit Commands": "file-earmark-spreadsheet",
    "Integrating Pandas": "table",
    "Component: AgGrid": "table",
}


def streamlit_sidebar(
    menu_ops_icons, title="Topics", icon="menu-app", orientation="vertical"
):
    # build the navigation sidebar
    with st.sidebar:
        selected = option_menu(
            menu_title=title,  # required
            options=list(menu_ops_icons.keys()),  # required
            icons=list(menu_ops_icons.values()),  # optional
            menu_icon=icon,  # optional
            default_index=0,  # optional
            orientation=orientation,
        )
        return selected


# menu and sidebar builders
def streamlit_sidebar0(orientation="vertical"):
    # build the navigation sidebar
    with st.sidebar:
        selected = option_menu(
            menu_title="Topics",  # required
            options=["Home", "Pandas", "Markdown", "Widgets", "Images"],  # required
            icons=["house", "book", "envelope", "gear-wide", "image"],  # optional
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


selected = streamlit_sidebar(menu_ops_icons, title="Topics", orientation="vertical")


if selected == "Home":
    home_page.index(selected)

if selected == "Integrating Pandas":
    pandas_page.index(selected)

if selected == "Streamlit Commands":
    streamlit_page.index(selected)

if selected == "Component: AgGrid":
    aggrid_page.index(selected)


# if selected == "Markdown":
#     st.title(f"You have selected {selected}")
#     st.markdown("# this is a markdown Heading level 1")
#     st.markdown("## this is a markdown Heading level 2")
#     st.markdown("1. this is a markdown list")
#     st.markdown("2. this is a markdown lis")
#     st.markdown("Check markdown syntax [here](https://www.markdownguide.org/)")

# if selected == "Widgets":


# if selected == "Images":
#     st.title(f"You have selected {selected}")
#     st.markdown(
#         "interesting article [here](https://www.folkstalk.com/2022/09/how-to-user-upload-image-streamlit-with-code-examples.html)"
#     )

# st.sidebar.title("Python")
# st.sidebar.title("CSS")
# st.sidebar.subheader("this is the subheader")
