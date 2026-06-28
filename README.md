# DermaDiagnosis
## Two-Stage Deep Learning Based Skin Disease Classification System

DermaDiagnosis is a Final Year Project (FYP) focused on developing an intelligent skin disease classification system using deep learning and computer vision techniques.

The proposed system uses a **two-stage hierarchical classification approach**. In Stage 1, the model identifies the disease group from a skin image. In Stage 2, a specialized model is used to classify the specific disease within the predicted group.

This approach helps reduce classification errors between visually similar skin diseases and improves scalability compared with traditional single-stage classification methods.

---

# Project Objectives

- Develop an automated skin disease classification system.
- Improve prediction accuracy using deep learning techniques.
- Reduce confusion between visually similar diseases.
- Implement a hierarchical two-stage classification pipeline.
- Compare multiple deep learning architectures.
- Provide an easy-to-use graphical interface for image prediction.

---

# System Architecture

The proposed workflow:
Input Skin Image
|
↓
Image Preprocessing
|
↓
Stage 1 Model
Disease Group Classification
|
↓
Predicted Disease Group
|
↓
Stage 2 Model
Specific Disease Classification
|
↓
Final Prediction


---

# Dataset

The dataset was collected from publicly available dermatology image sources including:

- Kaggle
- DermNet
- UCI
- ISIC

The dataset was reorganized into a hierarchical structure according to disease groups.

## Disease Groups and Classes

### Acneiform
- Acne
- Folliculitis
- Rosacea

### Healthy
- Dry Skin
- Normal Skin
- Oily Skin

### Inflammatory
- Dermatitis
- Eczema
- Psoriasis

### Pigmentation
- Carcinoma
- Keratosis
- Melanoma

### Pox
- Chickenpox
- Measles
- Monkeypox

---

# Deep Learning Models

Multiple models were trained and evaluated:

## Proposed Model

### MobileNetV2

MobileNetV2 was selected as the proposed model because of:

- Lightweight architecture
- Efficient feature extraction
- Faster inference
- Suitability for real-time applications

---

## Comparison Models

The following architectures were also implemented:

- Custom CNN
- ResNet50
- VGG19
- EfficientNetB0
- LSTM-based model

---

# Methodology

The project consists of two stages:

## Stage 1: Disease Group Classification

The first model predicts the disease group:

Example:

Input Image → MobileNetV2 → Inflammatory Group


## Stage 2: Disease Classification

A separate classifier predicts the exact disease inside the selected group:

Example:


Inflammatory Group
↓
Inflammatory Model
↓
Psoriasis / Eczema / Dermatitis


---

# Data Preprocessing

Images were processed using:

- Image resizing
- Normalization
- Data augmentation

Augmentation techniques:

- Rotation
- Flipping
- Zoom
- Brightness adjustment
- Image shifting

---

# Technologies Used

- Python
- TensorFlow
- Keras
- MobileNetV2
- CNN Architectures
- OpenCV
- NumPy
- Pandas
- Scikit-learn
- Gradio

---

# Repository Structure


dermadiagnosis_fyp/

│
├── Stage1_Models/
│
├── Stage2_Models/
│
├── Comparison_Models/
│
├── src/
│
├── results/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md


---

# Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The proposed two-stage MobileNetV2 approach improved classification performance by reducing misclassification between similar skin diseases.

---

# GUI Application

The system includes a graphical interface that allows users to:

- Upload a skin image
- Select a deep learning model
- Get disease prediction
- View confidence score

---

# Future Improvements

Future enhancements include:

- Mobile application deployment
- Real-time camera-based diagnosis
- Cloud-based deployment
- Addition of more disease categories

---

# Author

Final Year Project

**DermaDiagnosis**  
Two-Stage Deep Learning Based Skin Disease Classification System
