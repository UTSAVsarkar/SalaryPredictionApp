import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


@st.cache_data
def load_data():
    dataset = pd.read_csv("Salary Data.csv")
    dataset = dataset.dropna()
    return dataset

dataset = load_data()

def show_explore_page():
    st.title("Explore different insights 😎")

    st.write(
        """
    ###Survey 2022
    """
    )

    st.write("""#### Count of different education level""")
    dataset['Education Level'].value_counts().plot(kind='bar')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""#### Frequency of ages""")
    plt.figure(figsize=(8, 6))
    plt.hist([dataset['Age']], bins=20, edgecolor='k', alpha=0.7,)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""#### Distribution of YoE""")
    plt.figure(figsize=(8, 6))
    plt.hist([dataset['Years of Experience']], bins=20, edgecolor='k', alpha=0.7,)
    plt.xlabel('Years of Experience')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""#### Distribution of Salaries""")
    plt.figure(figsize=(8, 6))
    plt.hist([dataset['Salary']], bins=20, edgecolor='k', alpha=0.7,)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""#### Salary (US$) v Gender""")
    fig, ax = plt.subplots(1,1, figsize=(12, 7))
    dataset.boxplot('Salary', 'Gender', ax=ax)
    plt.ylabel('Salary')
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""#### Salary (US$) v Education Level""")
    fig, ax = plt.subplots(1,1, figsize=(12, 7))
    dataset.boxplot('Salary', 'Education Level', ax=ax)
    plt.ylabel('Salary')
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf())