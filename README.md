# Google Play Store Analysis

Welcome to the **Google Play Store Analysis** repository! This project provides a deep dive into the rich dataset of apps available on the Google Play Store. The analysis covers a variety of aspects including app ratings, installations, categories, and more. By leveraging data cleaning, exploration, and visualization techniques, this project aims to uncover key insights and trends within the mobile app market.

## Repository Overview

This repository is organized into several key components:

### Dataset

- **[googleplaystore.csv](./googleplaystore.csv):**  
  This is the original dataset containing information on thousands of apps from the Google Play Store. It includes attributes such as app name, category, rating, number of installs, size, price, and more. This raw data serves as the foundation for all subsequent analysis.

### Data Analysis & Cleaning

- **[analyse.ipynb](./analyse.ipynb):**  
  This Jupyter notebook is dedicated to the exploration and visualization of the dataset. The notebook includes:
  - **Data Cleaning:** Steps to prepare the data by handling missing values, duplicates, and inconsistencies, ensuring the analysis is based on accurate and reliable data.
  - **Exploratory Data Analysis (EDA):** Detailed examination of the dataset to reveal patterns, relationships, and trends among the different app attributes.
  - **Visualizations:** A variety of charts and graphs to help visualize the insights gained from the data.

### Processed Data

- **[cleaned_googleplaystore.csv](./cleaned_googleplaystore.csv):**  
  This file contains the cleaned and processed version of the dataset, which has been refined to remove noise and prepare it for further analysis and visualization.

### Interactive Dashboard

- **[Streamlit App](https://app-play-store-analysis-ctr36djqdxmh9brhvvmu6r.streamlit.app/):**  
  A Streamlit-based web application that showcases the visualizations derived from the Google Play Store data. The app is designed to be both aesthetically pleasing and user-friendly, providing an interactive way to explore the data.

### Streamlit App Details

- **[app.py](./app.py):**  
  This Python script contains the code for the Streamlit app used to create interactive visualizations of the Google Play Store data. Here's an overview of the components within `app.py`:

  - **Imports and Setup:**  
    The script begins by importing necessary libraries such as `streamlit` for building the web application, `pandas` for data manipulation, and `plotly.express` for creating visualizations. It also sets up the Streamlit page configuration.

  - **Data Loading:**  
    The cleaned dataset (`cleaned_googleplaystore.csv`) is loaded into a DataFrame. The app initializes with a title and sidebar for selecting different visualizations.

  - **User Interface:**  
    Streamlit's sidebar is used to create interactive widgets such as radio buttons that allow users to choose the type of graph they want to display. The options include:
    - Distribution of Ratings
    - Number of Apps in Each Category
    - Distribution of App Prices
    - Distribution of App Sizes
    - Ratings vs. Size of Apps
    - Pairplot of Rating, Price, and Size
    - Number of Apps Released per Year
    - Boxplot of Ratings by Category

  - **Visualizations:**  
    Depending on the user's selection, various visualizations are generated using Plotly. These include histograms, bar charts, scatter plots, and box plots. Each visualization is customized for clarity and aesthetics.

  - **Metrics and Insights:**  
    Each visualization is accompanied by key metrics and insights, such as average ratings, most common categories, and correlations. This provides users with a comprehensive understanding of the data.

  - **Footer and Contact Information:**  
    The sidebar and main page include footers with information about the project, creator, and contact details. It also provides links to the dataset source and GitHub repository.

## Features

This project is rich in features, providing a comprehensive framework for analyzing and visualizing data:

- **Comprehensive Data Cleaning:**  
  Rigorous data cleaning processes to ensure the dataset is accurate and ready for analysis.

- **Exploratory Data Analysis (EDA):**  
  In-depth analysis of the dataset, revealing key trends and insights about the apps on the Google Play Store.

- **Interactive Visualizations:**  
  The web application includes dynamic visualizations that allow users to explore the data interactively, offering a deeper understanding of the mobile app ecosystem.

- **User-Friendly Interface:**  
  The Streamlit app is designed with usability in mind, providing an intuitive interface for navigating through the visualizations.

## Project Goals

The primary goals of this project are:

- **Data-Driven Insights:**  
  To provide meaningful insights into the mobile app market by analyzing and visualizing the vast amount of data available on the Google Play Store.

- **Interactive Exploration:**  
  To create a web application that allows users to interact with the data in a visually engaging and informative way.

- **Educational Value:**  
  To serve as a resource for those interested in data analysis, cleaning, and visualization techniques, particularly in the context of real-world datasets like that of the Google Play Store.

## Future Enhancements

While the current state of the project offers valuable insights, there are opportunities for further development:

- **Advanced Analytics:**  
  Implementing machine learning models to predict app success metrics based on available data.

- **Expanded Dataset:**  
  Incorporating additional data points such as user reviews, update history, and developer information to provide a more holistic view of the app market.

## Conclusion

The **Google Play Store Analysis** project is a powerful tool for understanding the dynamics of the mobile app market. Through thorough data cleaning, analysis, and visualization, this repository provides valuable insights that can inform both developers and consumers in the app ecosystem.

Feel free to explore the data, interact with the visualizations, and contribute to the project. Your feedback and contributions are always welcome!
