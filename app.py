import streamlit as st
import joblib
import numpy as np
import re
from scipy.sparse import hstack

# -------------------------
# Load models
# -------------------------
tfidf = joblib.load("tfidf.pkl")
selector = joblib.load("selector.pkl")
scaler = joblib.load("extra_feature_scaler.pkl")
stage1 = joblib.load("stage1_easy_vs_noneasy.pkl")
stage2 = joblib.load("stage2_medium_vs_hard.pkl")
svr_models = joblib.load("svr_models.pkl")

ALGO_KEYWORDS = [
    "dp", "dynamic programming", "graph", "dfs", "bfs", "tree",
    "segment tree", "bitmask", "mask", "flow", "geometry",
    "binary search", "greedy", "recursion"
]

def extract_features(text):
    text = text.lower()
    words = text.split()

    text_length = len(text)
    math_symbols = len(re.findall(r"[+\-*/%=<>]", text))
    keyword_freq = sum(text.count(k) for k in ALGO_KEYWORDS)
    avg_word_len = np.mean([len(w) for w in words]) if words else 0
    sentence_count = text.count(".")
    has_algorithm = int(keyword_freq > 0)
    numbers = [int(n) for n in re.findall(r"\d+", text)]
    max_constraint = max(numbers) if numbers else 0
    control_tokens = len(re.findall(r"\b(if|for|while)\b", text))

    return np.array([
        text_length,
        math_symbols,
        keyword_freq,
        avg_word_len,
        sentence_count,
        has_algorithm,
        max_constraint,
        control_tokens
    ]).reshape(1, -1)

# -------------------------
# UI
# -------------------------
st.title("AutoJudge – Programming Difficulty Predictor")

desc = st.text_area("Problem Description")
inp = st.text_area("Input Description")
out = st.text_area("Output Description")

if st.button("Predict"):
    combined_text = desc + " " + inp + " " + out

    X_text = tfidf.transform([combined_text])
    X_extra = extract_features(combined_text)
    X_extra = scaler.transform(X_extra)

    X_full = hstack([X_text, X_extra])
    X_selected = selector.transform(X_full)

    # Classification
    if stage1.predict(X_selected)[0] == "easy":
        pred_class = "easy"
    else:
        pred_class = stage2.predict(X_selected)[0]

    # Regression
    svr = svr_models[pred_class]
    pred_score = svr.predict(X_selected)[0]
    pred_score = np.clip(pred_score, 1.0, 10.0)

    st.success(f"Predicted Difficulty Class: {pred_class.upper()}")
    st.success(f"Predicted Difficulty Score: {pred_score:.2f}")
