# 🎥 Movie Recommendation System 📽️
- A content-based movie recommendation system built using Python, Pandas, and Scikit-learn. The system suggests similar movies based on the selected movie using cosine similarity between movie feature vectors. 

- Deployed with **Streamlit** for an interactive web experience and containerized with **Docker** for easy deployment.
  
---

## 🚀 Live Demo

👉 [Streamlit Live App](https://movie-recommendation-7sqmb5nw2gbblae5fsfjxe.streamlit.app/)  
👉 [Docker Hub Image](https://hub.docker.com/repository/docker/jatinag12/movierecommender/general)

---

## 🚀 Features

- 🎬 Movie suggestions based on content similarity.
- 📈 Uses cosine similarity on combined features.
- 📊 Clean, interactive Streamlit web UI.
- 🐳 Docker support for containerized deployment.
- 📦 Jupyter Notebook for development and analysis.

---

## 📂 Project Structure

.  
├── .gitignore # Git ignore file  
├── Dockerfile # Docker configuration  
├── Movie_Recommendation.ipynb # Jupyter Notebook for development & analysis   
├── app.py # Streamlit application code  
├── movies.pkl # Serialized movie metadata  
├── requirements.txt # Python dependencies  
├── similarity.zip # Compressed similarity matrix  
├── tmdb_5000_credits.csv # Dataset: movie credits info  
├── tmdb_5000_movies.csv # Dataset: movies info  
└──  README.md # Project documentation

---

## 🖥️ Running Locally

### 🔧 Prerequisites
- Make sure you have **Python 3.x** and **pip** installed on your system.
- Recommended to use a **virtual environment** (optional).

---

### ⬇️ Step-by-step Instructions

#### 1. Clone the Repository

```bash
https://github.com/jatin-agrawal17/Movie-Recommendation.git 
cd Real-Estate-Project
```
#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the App
```bash
streamlit run app.py 
```

## 💡 Deployment Notes

Since similarity.pkl is larger than GitHub’s file limit (100 MB), it is compressed into a .zip file. Ensure it’s unzipped before running locally or deploying to Streamlit Cloud.

## 📊 Dataset Used

[tmdb_5000_credits.csv](https://github.com/jatin-agrawal17/Movie-Recommendation/blob/main/tmdb_5000_credits.csv)  
[tmdb_5000_movies.csv](https://github.com/jatin-agrawal17/Movie-Recommendation/blob/main/tmdb_5000_movies.csv)

## 📌 Limitations

📌 Movie Poster Integration Not Added:
I intended to fetch and display movie posters using the TMDb API, but encountered persistent issues accessing poster URLs on my local setup. This will be addressed in a future version once the environment compatibility is resolved.

## 👤 Author

Jatin Agrawal  
📬 [LinkedIn](https://www.linkedin.com/in/jatin-agrawal-b80092367/)

## 📎 License

This project is open-source and available under the MIT License.


