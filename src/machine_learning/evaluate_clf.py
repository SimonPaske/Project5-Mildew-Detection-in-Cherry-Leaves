import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation(version):
    evaluation_data = load_pkl_file(f'outputs/{version}/evaluation.pkl')
    return {'Loss': evaluation_data['test_loss'], 'Accuracy': evaluation_data['test_accuracy']}
