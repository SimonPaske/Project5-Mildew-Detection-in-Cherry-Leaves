import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd


from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities,

)


def mildew_detector_page():
    st.info(
        f'In this section, we will use a trained model to predict '
        f'whether a cherry leaf is healthy or infected with powdery mildew.'
    )
    st.write(
        f'You can download testing images of cherry leaves from the following link:'
        f' [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)'
    )
    st.write('---')  # Moved this line here

    image_buffer = st.file_uploader(
        "Upload an image of a cherry leaf", type=["png", "jpg", "jpeg"], accept_multiple_files=True
    )

    if image_buffer is not None:
        df_report = pd.DataFrame([])
        for image in image_buffer:

            # Extract the filename from the uploaded file
            image_name = image.name if hasattr(image, 'name') else "Unknown"

            image = Image.open(image)
            st.info(f"Leaf sample: **{image_name}**")
            image = np.array(image)
            st.image(image, caption=f"Image Size: {image.shape[1]}px width x {image.shape[0]}px height")

            version = 'v1'

            resized_image = resize_input_image(img=image, version=version)
            predictions = load_model_and_predict(resized_image, version)
            plot_predictions_probabilities(pred_proba=predictions[0], pred_class=predictions[1])

            df_report = df_report.append({'Name': image_name, 'Result': predictions[1]}, ignore_index=True)

    if not df_report.empty:
        st.success("Analysis Report")
        st.table(df_report)
        st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)


mildew_detector_page()
