import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import load_test_evaluation


def model_performance():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")

    st.write("### Model History")

    st.write(" **Model Training Accuracy**")
    model_acc = plt.imread(f"keras_tuner_dir/tune_model/model_training_acc.png")
    st.image(model_acc, caption='Model Training Accuracy')

    st.write(" **Model Training Losses**")
    model_loss = plt.imread(f"keras_tuner_dir/tune_model/model_training_losses.png")
    st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")

    st.dataframe(pd.DataFrame(load_test_evaluation(version),index=['Results']))
    



model_performance()
