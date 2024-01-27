import os
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import load_test_evaluation
from collections import Counter


def count_images_and_labels(data_dir):
    messages = []

    for set_type in ['train', 'validation', 'test']:
        set_dir = os.path.join(data_dir, set_type)

        for label in os.listdir(set_dir):
            label_dir = os.path.join(set_dir, label)
            num_images = len(os.listdir(label_dir))

            messages.append(f"Set: {set_type.capitalize()}, Label: {label}, Number of images: {num_images}\n")

    st.warning('\n'.join(messages))
    return


def model_performance():
    data_dir = "inputs/datasets/cherry-leaves"
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    count_images_and_labels(data_dir)
    st.write("---")

    st.write("### Model History")
    st.info(
        f'The depicted graphs offer a visual illustration of the learning cycle for the machine learning model. '
        f'In these plots, both accuracy and loss are tracked throughout the training process. '
        f'Accuracy is the fraction of correctly classified images, while loss is a measure of error. '
        f'In general, the goal is to maximize accuracy and minimize loss. ''\n'
        f'The observed patterns suggest a typical learning curve, indicating that the model is neither overfitting '
        f'nor underfitting. The balance between accuracy improvement and loss reduction suggests that the model is '
        f'effectively learning from the training data without exhibiting signs of overemphasis on the training set ')

    st.write(" **Model Training Accuracy**")
    model_acc = plt.imread(f"keras_tuner_dir/tune_model/model_training_acc.png")
    st.image(model_acc, caption='Model Training Accuracy')

    st.write(" **Model Training Losses**")
    model_loss = plt.imread(f"keras_tuner_dir/tune_model/model_training_losses.png")
    st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalized Performance on Test Set")

    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Results']))

    st.write("---")


model_performance()
