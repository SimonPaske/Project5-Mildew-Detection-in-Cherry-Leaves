import streamlit as st


def summary_page():
    st.title("Project Summary")

    st.info(f"Powdery mildew is a common plant disease caused by various fungi belonging to the order Erysiphales. "
        f"It affects a wide range of plants, including ornamental plants, crops, and trees. The characteristic "
        f"symptom of powdery mildew is the presence of a white to grayish, powdery substance on the surfaces of leaves, "
        f"stems, and sometimes flowers. This powdery appearance is due to the fungal spores and mycelium covering the "
        f"plant's tissues. The fungi responsible for powdery mildew thrive in warm and dry conditions. Unlike some other fungal diseases, "
        f"powdery mildew doesn't require water on the plant surface for infection. Instead, it can spread through airborne "
        f"spores. The affected plants may exhibit stunted growth, yellowing of leaves, and premature leaf drop, leading to "
        f"reduced overall plant health and productivity. Control measures for powdery mildew include cultural practices, such as providing adequate spacing between plants "
        f"for good air circulation, using resistant plant varieties, and applying fungicides when necessary. Additionally, "
        f"managing environmental conditions, like reducing humidity and avoiding overcrowding of plants, can help prevent and "
        f"control powdery mildew infections.")
    '\n'

    st.warning('**Project Dataset**' '\n'
             'The dataset used in this project is a collection of images of cherry leaves infected with powdery mildew.'' \n'
             'Dataset can be found at [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)'' \n'
             'The Dataset contains 4.218 images taken from client'' \n'
             'The images are divided into 2 folders: "healthy" and "powdery mildew" \n')

    st.write(f'For additional info, please visit and read the [README file](https://github.com/SimonPaske/Project5-Mildew-Detection-in-Cherry-Leaves/blob/main/README.md).')

    st.success(
               f'Project requirements:' '\n'
               f'\n''1 - Highlight distinctions between average healthy and powdery mildew cherry leaves.' "\n"
               f'\n''2 - Create a model that can detect powdery mildew in cherry leaves.')