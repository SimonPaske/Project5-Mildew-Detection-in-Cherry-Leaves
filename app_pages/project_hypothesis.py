import streamlit as st


def project_hypothesis_page():
    st.write('**Project Hypothesis**' '\n')
    st.success(hypothesis_1)
    st.success(hypothesis_2)
    st.success(hypothesis_3)


hypothesis_1 = ("* Powdery mildew-infected cherry leaves are expected to display identifiable visual patterns, "
                "particularly along the edges, which set them apart from healthy cherry leaves.")

hypothesis_2 = ("* An Image Montage is anticipated to reveal distinct patterns along the edges of leaves affected "
                    "by powdery mildew. To validate this hypothesis, an exploratory data analysis (EDA) will be conducted "
                    "on the dataset. The objective is to visualize samples of both healthy and affected cherry leaves, "
                    "aiming to identify noticeable patterns or differences that can be leveraged for accurate classification.")

hypothesis_3 = (f"* The performance of the machine learning pipeline was assessed, demonstrating its ability "
                f"to distinguish between a healthy leaf and an infected leaf with an accuracy of at least 97%.")