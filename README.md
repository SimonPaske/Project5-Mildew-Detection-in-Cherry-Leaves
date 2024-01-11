# Project Overview

## Business Requirements

### Business Requirement 1

The study should include the following analyses:

1. **Average Images and Variability Images:**
   - Calculate average images for each class (healthy or powdery mildew).
   - Analyze variability images for each class.

2. **Differences between Average Healthy and Average Powdery Mildew Cherry Leaves:**
   - Explore and highlight distinctions between average healthy and powdery mildew cherry leaves.

3. **Image Montage:**
   - Create image montages for each class (healthy and powdery mildew).

### Business Requirement 2

Develop an ML system capable of predicting whether a cherry leaf is healthy or contains powdery mildew. Suggest using Neural Networks to map relationships between features and labels. The model consistently achieves the specified 97% accuracy on the validation set.

**Note:** Consider using an image shape smaller than 256x256 (e.g., 100x100 or 50x50) to keep the model size below 100Mb for GitHub.

## Dashboard Expectations

1. **Project Summary Page:**
   - Display project dataset summary.
   - Present client's requirements.

2. **Findings Page:**
   - Visualize key findings differentiating healthy and powdery mildew cherry leaves.

3. **Prediction Interface Page:**
   - Provide a link to download cherry leaf images for live prediction.
   - Include a user interface with a file uploader widget.
   - Display uploaded images with prediction statements and associated probabilities.
   - Show a table with image names and prediction results, along with a download button for the table.

4. **Project Hypothesis Page:**
   - Present the project hypothesis.
   - Explain how the hypothesis was validated throughout the project.

5. **Technical Page:**
   - Display model performance metrics.
   - Include details on the chosen model architecture and parameters.

## Note to Developers

When pushing files larger than 100Mb to GitHub, consider using Git LFS (Large File Storage) for a smoother process.

---

# Business Assessment Case: Farmy & Foods Cherry Leaf Detection

## Executive Summary

**Client:** Marianne McGuineys, Head of IT and Innovation at Farmy & Foods  
**Challenge:** Powdery mildew affecting cherry plantations, leading to compromised product quality.  
**Current Process:** Manual verification of cherry trees, time-consuming and not scalable.  
**Proposed Solution:** Implement an ML system for instant detection using cherry leaf images.  

## Business Problem

Farmy & Foods faces a critical issue with their cherry plantations as powdery mildew is compromising the quality of the crop. The current manual verification process is time-intensive, requiring around 30 minutes per tree, making it impractical for the large number of cherry trees across multiple farms.

## Objectives

1. **Efficiency Improvement:** Implement a solution to reduce the time spent on manual verification.
2. **Quality Assurance:** Ensure the production of high-quality cherries by early detection of powdery mildew.
3. **Scalability:** Create a solution that is scalable for the thousands of cherry trees across multiple farms.

## Proposed Solution

### Machine Learning System

The IT team suggests developing a Machine Learning (ML) system capable of instantly detecting the health status of a cherry tree based on leaf images. This would significantly reduce the time spent on manual inspections.

### Dashboard Requirements

1. **Visual Differentiation Study:**
   - Conduct a study to visually differentiate healthy cherry leaves from those containing powdery mildew.

2. **Prediction Capability:**
   - Develop an ML model capable of predicting if a cherry tree is healthy or has powdery mildew.

3. **Dashboard Deliverable:**
   - Deliver a user-friendly dashboard that meets the study and prediction requirements.

## Benefits

1. **Time Savings:** Instant detection with ML reduces the manual verification time from 30 minutes to near real-time.
2. **Quality Improvement:** Early identification of powdery mildew ensures the production of high-quality cherries.
3. **Scalability:** The success of this initiative provides a model for implementing similar solutions for other crops.

## Challenges

1. **Data Quality:** Ensure the dataset of cherry leaf images is representative and diverse.
2. **Model Accuracy:** Achieve high accuracy in predicting powdery mildew to minimize false positives/negatives.
3. **Deployment:** Smoothly deploy the ML model and integrate it into the existing farm management systems.

## Next Steps

1. **Data Collection and Preparation:**
   - Gather a diverse and representative dataset of cherry leaf images.
   - Clean and prepare the dataset for ML model training.

2. **Model Development and Training:**
   - Develop a robust ML model capable of accurate cherry leaf classification.
   - Train and validate the model using the prepared dataset.

3. **Dashboard Design and Development:**
   - Plan and design a user-friendly dashboard to meet the study and prediction requirements.
   - Implement the dashboard functionalities.

4. **Deployment and Testing:**
   - Deploy the ML model into the farm management system.
   - Conduct thorough testing to ensure the model's accuracy and reliability.

5. **Training and Adoption:**
   - Train farm personnel on the new system.
   - Ensure seamless adoption and integration into the daily workflow.

## Success Metrics

1. **Accuracy Rate:** Achieve a high accuracy rate in cherry leaf classification.
2. **Time Savings:** Demonstrate a significant reduction in the time spent on manual verification.
3. **Quality Assurance:** Verify an improvement in the overall quality of harvested cherries.

## Conclusion

By addressing the powdery mildew challenge through the implementation of an ML-based solution and an intuitive dashboard, Farmy & Foods aims to enhance efficiency, assure product quality, and pave the way for scalable solutions across their agricultural portfolio.

---


# Project Execution

## Analysis and Findings

### Average Images and Variability

- Calculated average images for healthy and powdery mildew cherry leaves.
- Analyzed variability images to understand variations within each class.

### Differences between Classes

- Explored and highlighted differences between average healthy and powdery mildew cherry leaves.

### Image Montages

- Created visually appealing image montages for both healthy and powdery mildew cherry leaves.

## Model Development

- Utilized Neural Networks to map relationships between features and labels.
- Adopted an image shape smaller than 256x256 to meet GitHub size constraints.

## Dashboard Implementation

### Project Summary Page

- Displayed dataset summary and client's requirements.

### Findings Page

- Visualized key findings to differentiate healthy and powdery mildew cherry leaves.

### Prediction Interface Page

- Provided a link to download cherry leaf images for live prediction.
- Implemented a user-friendly interface with a file uploader widget.
- Displayed uploaded images with prediction statements and probabilities.
- Included a table with image names and prediction results, with a download button for the table.

### Project Hypothesis Page

- Stated the project hypothesis and provided evidence of validation.

### Technical Page

- Showcased model performance metrics.
- Shared details on the chosen model architecture and parameters.
---

## Project Breakdown

### Epics and User Stories

1. **Information Gathering and Data Collection**
   - User Story: As a data scientist, I want to gather relevant information and collect labeled cherry leaf images for analysis.

2. **Data Visualization, Cleaning, and Preparation**
   - User Story: As a data analyst, I need to visualize average and variability images for healthy and powdery mildew classes.
   - User Story: As a data engineer, I must clean and prepare the dataset for training.

3. **Model Training, Optimization, and Validation**
   - User Story: As a machine learning engineer, I will train a neural network to predict leaf health.
   - User Story: As a researcher, I will optimize and validate the model's performance.

4. **Dashboard Planning, Designing, and Development**
   - User Story: As a UI/UX designer, I will plan and design a dashboard based on client requirements.
   - User Story: As a developer, I will implement the dashboard functionalities.

5. **Dashboard Deployment and Release**
   - User Story: As a project manager, I will oversee the deployment and release of the dashboard.

### Ethical and Privacy Concerns

- Data provided under NDA; only share with authorized project personnel.

### Model Selection and Image Shape Considerations

We suggest using neural networks for the ML system due to the complex relationships between features (leaf images) and labels (healthy/powdery mildew). To address the file size concern, consider using an image shape smaller than 256x256, such as 100x100 or 50x50, while ensuring the model still meets the 97% accuracy requirement.

---

## Dashboard Expectations

### Pages:

1. **Project Summary Page**
   - Display dataset summary and client requirements.

2. **Visual Differentiation Study Findings**
   - Provide analysis on average images, variability, and differences between healthy and powdery mildew cherry leaves.

3. **Live Prediction Interface**
   - Include a file uploader widget for multiple images.
   - Display uploaded images with predictions and associated probabilities.
   - Present a table with image names and prediction results.
   - Include a download button for the prediction table.

4. **Project Hypothesis and Validation**
   - Explain the project hypothesis and how it was validated.

5. **Technical Page - Model Performance**
   - Display model performance metrics.

## Model Selection and Transformations

We recommend using neural networks, specifically for image classification tasks. Convolutional Neural Networks (CNNs) are well-suited for image analysis. The pipeline should include:
- Image resizing to a smaller shape (e.g., 100x100) for efficient processing.
- Data augmentation to enhance model generalization.
- Normalization to scale pixel values.
- Cross-entropy loss for binary classification.
- Optimization techniques (e.g., Adam optimizer) for model training.

---

# Project Plan: Visual Differentiation of Cherry Leaves

## Project Steps and Milestones

### Step 1: Information Gathering and Data Collection
- **Milestone 1:** Complete collection of labeled cherry leaf images.
  - User Stories:
    - As a data scientist, I want to identify and gather relevant information for the project.
    - As a researcher, I want to compile a dataset of labeled cherry leaf images for analysis.

### Step 2: Data Visualization, Cleaning, and Preparation
- **Milestone 2:** Visualize average and variability images for healthy and powdery mildew classes.
  - User Stories:
    - As a data analyst, I want to create visualizations of average and variability images.
    - As a data engineer, I need to clean and prepare the dataset for training.

### Step 3: Model Training, Optimization, and Validation
- **Milestone 3:** Train a neural network to predict leaf health.
  - User Stories:
    - As a machine learning engineer, I will develop and optimize the model.
    - As a researcher, I will validate the model's performance against a test set.

### Step 4: Dashboard Planning, Designing, and Development
- **Milestone 4:** Plan and design the dashboard based on client requirements.
  - User Stories:
    - As a UI/UX designer, I will create wireframes and design the dashboard layout.
    - As a developer, I will implement the dashboard functionalities.

### Step 5: Dashboard Deployment and Release
- **Milestone 5:** Deploy and release the dashboard.
  - User Stories:
    - As a developer, I will ensure the dashboard is released to meet client expectations.

## User Stories

1. **Information Gathering and Data Collection**
   - As a data scientist, I want to identify relevant information for the project.
   - As a researcher, I want to compile a dataset of labeled cherry leaf images for analysis.

2. **Data Visualization, Cleaning, and Preparation**
   - As a data analyst, I want to create visualizations of average and variability images.
   - As a data engineer, I need to clean and prepare the dataset for training.

3. **Model Training, Optimization, and Validation**
   - As a machine learning engineer, I will develop and optimize the model.
   - As a researcher, I will validate the model's performance against a test set.

4. **Dashboard Planning, Designing, and Development**
   - As a UI/UX designer, I will create wireframes and design the dashboard layout.
   - As a developer, I will implement the dashboard functionalities.

5. **Dashboard Deployment and Release**
   - As a developer, I will ensure the dashboard is released to meet client expectations.

---
