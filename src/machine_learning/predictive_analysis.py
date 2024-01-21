import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """
    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'Uninfected': 0, 'Infected': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)


def resize_input_image(img, version):
    target_size = (100, 100) if version == 'v1' else (224, 224)
    img_resized = np.resize(img, target_size + (3,))
    my_image = np.expand_dims(img_resized, axis=0) / 255

    return my_image



def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f'outputs/{version}/optimized_model.keras')
    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'Uninfected': 0, 'Infected': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the leaf sample is "
        f"**{pred_class.lower()}** with mildew.")

    return pred_proba, pred_class
