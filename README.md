# AutoJudge: Predicting Programming Problem Difficulty

## Project Overview
AutoJudge is a machine learning–based system that automatically predicts the difficulty of programming problems using only their textual descriptions. Given a problem statement along with its input and output descriptions, the system predicts:

- **Problem Difficulty Class:** Easy / Medium / Hard  
- **Problem Difficulty Score:** A numerical difficulty value  

The objective of this project is to automate the difficulty estimation process, which is typically performed manually on competitive programming platforms such as Codeforces, CodeChef, and Kattis.

The project also includes a deployed **web-based user interface** that allows users to obtain predictions in real time.

---
### Live Deployment
🔗 **Web Application Link:**  
https://autojudge-hxoigre646axmf2kpmdtbi.streamlit.app/

The deployed application uses the same trained models included in this repository.

---
### Demo Video
 2–3 Minute Demo Video:
https://drive.google.com/your-demo-video-link

The demo video includes:
Brief project explanation
Overview of the model approach
Live demonstration of the web interface with predictions

## Dataset Used
The dataset used in this project was **provided as part of the official project problem statement**. No external data sources were collected and no manual labeling was performed.

Each data sample contains:
- `title`
- `description`
- `input_description`
- `output_description`
- `problem_class` (Easy / Medium / Hard)
- `problem_score` (numerical value)

For modeling, the textual fields (`description`, `input_description`, and `output_description`) are concatenated into a single input text.

---

## Approach and Models Used

### Feature Engineering
- **TF-IDF features**
  - Unigrams and bigrams
  - Maximum features: 12,000
- **Handcrafted features**, including:
  - Text length
  - Mathematical symbol count
  - Algorithm keyword frequency (e.g., DP, graph, BFS)
  - Average word length
  - Sentence count
  - Constraint magnitude
  - Control-flow keyword density

TF-IDF and handcrafted features are combined and reduced using **Chi-square feature selection** (top 5000 features).

---

### Classification Model
A **hierarchical, cost-sensitive SVM approach** is used:

1. **Stage 1:** Easy vs Non-Easy  
2. **Stage 2:** Medium vs Hard (applied only to non-easy samples)

This hierarchical strategy improves robustness, particularly for the Easy class.

---

### Regression Model
A **class-conditional Linear SVR** approach is used to predict the numerical difficulty score. Separate regressors are trained for Easy, Medium, and Hard problem categories.

---

## Evaluation Metrics

### Classification
- **Final Hierarchical Accuracy:** ~80%
- Metrics reported:
  - Accuracy
  - Precision
  - Recall
  - F1-score

### Regression
- **Mean Absolute Error (MAE):** 0.795  
- **Root Mean Squared Error (RMSE):** 1.017  

All reported results correspond to the trained models included in this repository.

---

## Web Interface
A lightweight web application is built using **Streamlit**.

### Functionality
- User inputs:
  - Problem Description
  - Input Description
  - Output Description
- On clicking **Predict**, the app displays:
  - Predicted difficulty class
  - Predicted numerical difficulty score


### Author Details
Name: E.M Sanmaya
Program: Electronics And Communication Engineering (ECE)
Project Title: AutoJudge – Predicting Programming Problem Difficulty



