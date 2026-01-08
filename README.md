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
https://drive.google.com/file/d/1IokO9SjrEuRZKD6JsBTLoXDdO70IJP1D/view?usp=sharing

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

## Classification Model

The difficulty classification component is implemented using a **hierarchical, cost-sensitive Support Vector Machine (SVM) architecture**, designed to handle class imbalance and overlapping semantic complexity across difficulty levels.

Instead of treating difficulty prediction as a flat three-class classification problem, the model decomposes the task into a **two-stage hierarchical decision process**, which better reflects the intrinsic structure of problem difficulty.

### Stage 1: Easy vs Non-Easy Classification

In the first stage, a **binary Linear SVM classifier** is trained to distinguish *Easy* problems from *Non-Easy* problems (Medium and Hard combined). This stage is explicitly optimized to improve robustness for the *Easy* class, which is more susceptible to misclassification due to limited structural complexity and weaker algorithmic cues.

To address this, **cost-sensitive learning** is applied by assigning a higher misclassification penalty to the *Easy* class. This encourages the model to reduce false negatives for Easy problems and ensures that simpler problems are not incorrectly promoted to higher difficulty levels.

This stage acts as a coarse-grained filter, separating low-complexity problems based on linguistic simplicity, constraint magnitude, and absence of advanced algorithmic patterns.

### Stage 2: Medium vs Hard Classification

Problems classified as *Non-Easy* in Stage 1 are passed to a second **Linear SVM classifier** trained exclusively on *Medium* and *Hard* samples.

This stage focuses on learning finer distinctions between higher-difficulty problems, where semantic features such as algorithmic keywords, control-flow indicators, and constraint density exhibit significant overlap. Balanced class weighting is used to ensure stable learning across both classes.

By restricting this classifier to only higher-complexity samples, the model avoids unnecessary confusion introduced by Easy-class characteristics and achieves more precise separation between Medium and Hard problems.

### Rationale for Hierarchical Design

The hierarchical formulation is motivated by the observation that *Easy* problems form a qualitatively distinct group, while *Medium* and *Hard* problems lie on a more continuous difficulty spectrum. A flat multi-class classifier would force a single decision boundary to model all interactions simultaneously, leading to reduced interpretability and instability under class imbalance.

The two-stage architecture improves robustness, enhances interpretability of decision boundaries, and allows targeted optimization for each difficulty transition.

---

## Regression Model

The numerical difficulty prediction task is formulated using a **class-conditional linear Support Vector Regression (SVR) framework** to estimate continuous difficulty scores.

Rather than fitting a single global regression model across all difficulty levels, the system trains **independent Linear SVR models for each difficulty class** (*Easy*, *Medium*, and *Hard*). Each regressor is trained exclusively on samples belonging to its respective class and is applied only to test instances of that class.

This design acknowledges that the relationship between textual features and numerical difficulty is **class-dependent**. For example, small structural changes may significantly affect the score of Easy problems, while Hard problems exhibit higher tolerance to variation due to complex algorithmic requirements.

### Class-Conditional Training Strategy

For each difficulty category:
- A separate Linear SVR model is trained using class-specific samples
- The ε-insensitive loss function is used to balance precision and robustness
- Predictions are generated only for instances belonging to the corresponding class

By conditioning regression on the predicted difficulty class, the model avoids forcing a single regression function to approximate heterogeneous score distributions across difficulty levels.

### Advantages of the Regression Approach

This class-conditional regression strategy:
- Reduces bias introduced by overlapping score ranges
- Improves numerical stability across difficulty regimes
- Produces smoother and more interpretable score predictions
- Aligns more closely with human-annotated difficulty progression

Overall, the regression component complements the hierarchical classifier by providing fine-grained difficulty estimation while respecting the structural differences between problem categories.

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





