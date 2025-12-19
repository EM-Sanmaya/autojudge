# AutoJudge – Programming Problem Difficulty Predictor

AutoJudge is a machine learning–based system that automatically predicts the **difficulty level** of programming problems using only their textual descriptions.

The system predicts:
- **Difficulty Class**: Easy / Medium / Hard  
- **Difficulty Score**: A numerical score representing problem difficulty

---

## Problem Statement

Online coding platforms classify programming problems by difficulty, but this process often depends on human judgment and user feedback.  
This project aims to **automate difficulty prediction** using only the problem’s text (description, input format, and output format).

---

## Approach

1. **Text Preprocessing**
   - Combine problem description, input description, and output description
   - Handle missing values
   - Preserve numerical and symbolic information

2. **Feature Extraction**
   - TF-IDF features (unigrams and bigrams)
   - Text length
   - Mathematical symbol count
   - Algorithm keyword frequency (graph, dp, recursion, etc.)

3. **Classification**
   - Hierarchical classification:
     - Stage 1: Easy vs Non-Easy
     - Stage 2: Medium vs Hard
   - Linear SVM models

4. **Regression**
   - Class-conditional regression using Linear SVR
   - Separate regressors for Easy, Medium, and Hard problems
   - Predicts a numerical difficulty score

5. **Web Interface**
   - Built using Streamlit
   - Users paste problem text and receive predictions instantly

---

## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
