# 📩 Spam Detection System

A **machine learning-based Spam Detection system** built with **Python, Scikit-Learn, and Streamlit**. This project classifies messages as **Spam or Ham** using **Natural Language Processing (NLP) techniques**.

## Features

- **Text Preprocessing**: Tokenization, Stopword Removal, and TF-IDF Vectorization.
- **Machine Learning Model**: Trained using **Naive Bayes / Logistic Regression / Random Forest**.
- **Streamlit Web App**: User-friendly interface for real-time spam classification.
- **Hosted on Streamlit Cloud**: Easily accessible online.

## Dataset

- Uses the **SMS Spam Collection** dataset from UCI Machine Learning Repository.
- Contains labeled messages as **spam or ham**.

## Tech Stack

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-Learn, NLTK, Streamlit
- **Deployment**: Hosted on **Streamlit Cloud**

## Installation

1. Clone this repository:
  ```sh
  git clone https://github.com/yourusername/spam-detection.git
  cd spam-detection
  ```
2. Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
3. Run the Streamlit app:
  ```sh
  streamlit run app.py
  ```

## Usage
1. Open the Streamlit web app.
2. Enter a text message.
3. Click the "Predict" button.
4. The app will classify the message as Spam or Ham.

## Demo 
[Click here for Live Demo](https://spamdetectiontq.streamlit.app/)
