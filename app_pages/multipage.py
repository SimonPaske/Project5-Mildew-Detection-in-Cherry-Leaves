import streamlit as st


st.set_page_config(
            page_title="Cherry Leaves Mildew Detector",
            page_icon="🍒",
            layout="wide",
            initial_sidebar_state="expanded",
        )


class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func):
        self.pages.append({'title': title, 'function': func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu',
                                self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
