import streamlit as st
import os
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random
import seaborn as sns



def leaf_visualizer_page():
    st.write('**Leaf Visualizer**' '\n')
    st.info(
        f'In this section, we will visualize a sample of the images in the dataset.'
        f'The objective is to identify any noticeable patterns or differences between'
        f'healthy and powdery mildew-infected cherry leaves.'
    )

    if st.checkbox('Show difference between average healthy and infected leaf'):
        st.warning(
            f'As we can see, the average healthy leaf is much more green than the average infected leaf. '
            f'This is likely due to the fact that powdery mildew is a fungal disease that grows on the surface of leaves. '
            f'In other words, the fungus blocks the light from reaching the leaf, which causes the leaf to become less green. '
        )

        st.write('**Average Healthy Leaf**')
        st.image('outputs/v1/avg_var_healthy.png')
        st.write('**Average Infected Leaf**')
        st.image('outputs/v1/avg_var_powdery_mildew.png')

    if st.checkbox('Difference between average healthy and infected leaf in the green channel'):
        st.warning(
            f'In addition, absolute difference between the average healthy leaf and the average infected leaf is much more '
            f'pronounced in the green channel than in the red or blue channels. This is likely due to the fact that the '
            f'green channel is the most sensitive to changes in light intensity.')
        st.write('**Sample of Healthy Leaves**')
        st.image('outputs/v1/difference_plot.png')

    if st.checkbox('Show image montage'):
        st.warning(
            f'In this section, we will visualize a sample of the images in the dataset. The objective is to identify any '
            f'noticeable patterns or differences between healthy and powdery mildew-infected cherry leaves.'
        )
        data_dir = 'inputs/datasets/cherry-leaves/'
        labels = os.listdir(data_dir + '/validation')
        label_to_display = st.selectbox('Select a label to display', options=labels, index=0)
        if st.button('Generate Image Montage'):
            image_montage(data_dir=data_dir, label_to_display=label_to_display,
                          nrows=5, ncols=5, figsize=(10, 10), randomize=True)
        st.write('---')


def image_montage(data_dir, label_to_display, nrows, ncols, figsize=(15, 10), randomize=True):
    sns.set_style("white")
    label_path = os.path.join(data_dir, 'validation', label_to_display)

    if os.path.exists(label_path):
        images_list = os.listdir(label_path)

        if randomize and nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            img_idx = images_list[:nrows * ncols]

        list_rows = range(nrows)
        list_cols = range(ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(nrows * ncols):
            img = imread(os.path.join(label_path, img_idx[x]))
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px \n Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {os.listdir(os.path.join(data_dir, 'validation'))}")


leaf_visualizer_page()
