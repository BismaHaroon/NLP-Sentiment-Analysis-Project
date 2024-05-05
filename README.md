# NLP-Sentiment-Analysis-Project
This repository contains code and resources for a sentiment analysis project, including data preprocessing, model training, aspect-based sentiment analysis, and a Flask web application for deploying the sentiment analysis model.

### Directory Structure

- **data/**: Contains the dataset used for sentiment analysis.
- **models/**: Directory for storing trained model artifacts.
- **notebooks/**: Jupyter notebooks for data preprocessing, model training, and aspect-based sentiment analysis.
- **app/**:
  - **templates/**: HTML templates for the Flask web application.
  - **app.py**: Flask application for deploying the sentiment analysis model.
  - **Dockerfile**: Dockerfile for containerizing the Flask application
  - **requirements.txt**: List of Python dependencies required for the application.
- **README.md**: Instructions and information about the project.
- **requirements.txt**: List of Python dependencies required for the project.

### Tasks Performed

- **Data Preprocessing and Exploration**: The `data_preparation_and_exploration.ipynb` notebook performs data preprocessing tasks such as loading the dataset, preprocessing text, exploring the distribution of sentiment across different aspects of employment, and identifying patterns and trends in text data.

- **Model Training**: The `sentiment_analysis_model_training.ipynb` notebook implements a random forest model for sentiment analysis and performs hyperparameter tuning using grid search. The trained model is then saved along with the TF-IDF vectorizer.

- **Aspect-Based Sentiment Analysis**: The `aspect_based_sentiment_analysis.ipynb` notebook performs aspect-based sentiment analysis by training separate models for different aspects of employment.

- **Flask Web Application**: The `app.py` file contains a Flask application for deploying the sentiment analysis model. It exposes an endpoint `/predict` for analyzing the sentiment of user-provided text.

- **Dockerfile**: The `Dockerfile` specifies the instructions for building a Docker image containing the Flask application.

### Running the Application

To run the Flask web application using Docker, follow these steps:

1. Clone the repository.
2. Navigate to the `app/` directory.
3. Build the Docker image using the provided `Dockerfile`. Use the command: 'docker build -t sentiment-analysis-app .'
4. Run the Docker container. Use the command: 'docker run -d -p 8080:5000 sentiment-analysis-app'
5. Access the application in your web browser at `http://localhost:8080`.

### Deployment
The application is deployed at: [https://nlpmodel1.azurewebsites.net/](https://nlpmodel1.azurewebsites.net/)

