import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Google Play Store Analysis",
    page_icon="📱",
    layout="wide"
)

# Load data
df = pd.read_csv("cleaned_googleplaystore.csv")

# Header
st.title("📊 Google Play Store Data Visualizations")

## Sidebar for selecting visualizations
st.sidebar.title("Select Visualization")
visualization = st.sidebar.radio(
    "Choose a graph to display",
    [
        "Distribution of Ratings",
        "Number of Apps in Each Category",
        "Distribution of App Prices",
        "Distribution of App Sizes",
        "Ratings vs. Size of Apps",
        "Pairplot of Rating, Price, and Size",
        "Number of Apps Released per Year",
        "Boxplot of Ratings by Category",
    ]
)

# Define visualizations and numerical analysis
if visualization == "Distribution of Ratings":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Average Rating", round(df['Rating'].mean(), 2))
    with col2:
        st.metric("Total Apps", df['Rating'].count())
    with col3:
        st.metric("Median Rating", round(df['Rating'].median(), 2))
    fig = px.histogram(df, x='Rating', nbins=30, marginal='rug', title='Distribution of Ratings')

elif visualization == "Number of Apps in Each Category":
    col1, col2, col3 = st.columns(3)
    with col1:
        top_category = df['Category'].mode()[0]
        st.metric("Most Common Category", top_category)
    with col2:
        st.metric("Number of Categories", df['Category'].nunique())
    with col3:
        st.metric(f"Number of Apps in {top_category}", df[df['Category'] == top_category].shape[0])
    category_counts = df['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'count']
    fig = px.bar(category_counts, x='Category', y='count', title='Number of Apps in Each Category')

elif visualization == "Distribution of App Prices":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Most Expensive App", f"${df['Price'].max():.2f}")
    with col2:
        st.metric("Average Price", f"${df['Price'].mean():.2f}")
    with col3:
        st.metric("Number of Free Apps", df[df['Price'] == 0].shape[0])
    fig = px.histogram(df, x='Price', nbins=50, marginal='rug', title='Distribution of App Prices')

elif visualization == "Distribution of App Sizes":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Largest App Size", f"{df['Size'].max()} MB")
    with col2:
        st.metric("Average App Size", f"{df['Size'].mean():.2f} MB")
    with col3:
        st.metric("Smallest App Size", f"{df['Size'].min()} MB")
    fig = px.histogram(df, x='Size', nbins=50, marginal='rug', title='Distribution of App Sizes')

elif visualization == "Ratings vs. Size of Apps":
    col1, col2 = st.columns(2)
    with col1:
        correlation = df['Size'].corr(df['Rating'])
        st.metric("Correlation (Size vs. Rating)", round(correlation, 2))
    fig = px.scatter(df, x='Size', y='Rating', title='Ratings vs. Size of Apps', opacity=0.5)

elif visualization == "Pairplot of Rating, Price, and Size":
    st.subheader("Pairwise Relationship Analysis")
    st.write("Analyzing the relationships between Rating, Price, and Size.")
    fig = px.scatter_matrix(df, dimensions=['Rating', 'Price', 'Size'], title='Pairplot of Rating, Price, and Size')

elif visualization == "Number of Apps Released per Year":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Earliest Release Year", int(df['Year'].min()))
    with col2:
        st.metric("Most Recent Release Year", int(df['Year'].max()))
    with col3:
        st.metric("Most Active Release Year", int(df['Year'].mode()[0]))
    fig = px.histogram(df, x='Year', title='Number of Apps Released per Year', nbins=len(df['Year'].unique()))

elif visualization == "Boxplot of Ratings by Category":
    col1, col2, col3 = st.columns(3)
    with col1:
        top_category_rating = df.groupby('Category')['Rating'].mean().idxmax()
        st.metric("Highest Rated Category", top_category_rating)
    with col2:
        st.metric("Average Rating in Highest Category", round(df.groupby('Category')['Rating'].mean().max(), 2))
    with col3:
        st.metric("Lowest Rated Category", df.groupby('Category')['Rating'].mean().idxmin())
    fig = px.box(df, x='Category', y='Rating', title='Boxplot of Ratings by Category')

# Customize Plotly figures
fig.update_layout(
    template="plotly_dark",
    title_font=dict(size=24, color='orange'),
    font=dict(size=14),
    xaxis_title=dict(font=dict(size=16, color='orange')),
    yaxis_title=dict(font=dict(size=16, color='orange'))
)

# Display the selected visualization
st.plotly_chart(fig, use_container_width=True)

# Footer in the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <h3>Created by Eldeeb   </h3>
        <p>Built using <strong>Streamlit</strong> and <strong>Plotly</strong></p>
        <p>Enhancing data insights with beautiful visualizations.</p>
        <p>For any feedback or suggestions, please reach out!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer at the bottom of the main page
st.markdown("---")
st.markdown(
    """
    ## Google Play Store Analysis

    This app provides various visualizations and insights into Google Play Store data.

    - **Data Source**: [Google Play Store Dataset on Kaggle](https://www.kaggle.com/lava18/google-play-store-apps)
    - **Developed by**: [Abd El-Rahman Eldeeb](https://www.linkedin.com/in/abd-el-rahman-eldeeb-a9bab6251/)
    - **Source Code**: [GitHub Repository](https://github.com/ElDEEB21/google-play-store-analysis)

    ### About the App
    This app analyzes and visualizes data from the Google Play Store to provide insights into app ratings, categories, prices, sizes, and more. The visualizations are powered by Plotly, and the app is built with Streamlit for an interactive experience.

    ### Contact
    If you have any questions or feedback, feel free to [contact me](mailto:omer84484@gmail.com).
    """
)

