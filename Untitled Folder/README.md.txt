# Content-Based Movie Recommendation System 🍿

## Overview
This is a Machine Learning web application built with Python and Streamlit. It uses a Content-Based Filtering algorithm (Cosine Similarity) to recommend the top 5 most similar movies based on user selection.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, Scikit-Learn, Streamlit
* **Algorithm:** Cosine Similarity (Text Vectorization)
* **Frontend:** Streamlit

## How to Run Locally
1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. **Important Note:** Due to GitHub's file size limits (100MB), the `movie_dict.pkl` and `similarity.pkl` files are not uploaded. 
4. To generate these files, run the `Movie Recommender.ipynb` Jupyter Notebook first.
5. Once the `.pkl` files are generated, run the web app using the following command:
```bash
   streamlit run movie_app.py