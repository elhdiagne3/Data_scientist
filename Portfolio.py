#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Elhadji Diaraff Diagne - Data Scientist Portfolio", layout="wide")

# css for mobile responsiveness and improved styling
st.markdown("""
    <style>
    /* Title Styling */
    h1 {
        color: #2C3E50;
        text-align: center;
        margin-bottom: 10px;
        font-family: 'Bahnschrift Light SemiCondensed';
        font-size: 28px;  
    }

    /* Subheader Styling */
    h3 {
        color: #2C3E50;
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Bahnschrift Light SemiCondensed';
        font-size: 20px;
    }

    /* Horizontal Menu Styling */
    .css-16huue1 {
        justify-content: center;
        font-family: 'Bahnschrift Light SemiCondensed';
    }

    /* Section Headers */
    h2 {
        color: #2980B9;
        border-bottom: 2px solid #2980B9;
        padding-bottom: 5px;
        font-family: 'Bahnschrift Light SemiCondensed';
        font-size: 24px;
    }

    /* Content Styling */
    .content {
        font-size: 18px;
        line-height: 1.6;
        color: #2C3E50;
        text-align: justify;
        font-family: 'Bahnschrift Light SemiCondensed';
        margin: 0 auto;
        max-width: 800px;
        padding: 15px; /* Added padding for better mobile readability */
    }

    /* Mobile adjustments */
    @media (max-width: 768px) {
        h1 {
            font-size: 24px;
        }

        h2 {
            font-size: 20px;
        }

        .content {
            font-size: 16px;
        }
    }

    /* Bold and Dark Blue Styling */
    .content b {
        color: #2980B9;
        font-weight: bold;
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        margin-top: 10px;
        padding: 10px;
        color: #ffffff;
        background-color: #2980B9;
        font-family: 'Bahnschrift Light SemiCondensed';
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("Elhadji Diaraff DIAGNE")
st.subheader("Statistician and Data Scientist")

# Horizontal menu with icons
selected = option_menu(
    None, 
    ["About Me", "Skills", "Projects", "Experience", "Education", "Contact"], 
    icons=["person", "bar-chart", "briefcase", "award", "book", "envelope"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal"
)

# About Me Section
if selected == "About Me":
    st.header("About Me")
    st.markdown("""
        <div class="content">
        As a skilled <b>statistician</b> and <b>data scientist</b>, I excel in <b>project coordination</b> and managing large datasets, including <b>Big Data</b>. My expertise
        extends to <b>overseeing data collection operations</b> and leading <b>teams of interviewers</b> for <b>surveys and census projects</b>. Proficient in various
        <b>data mining tools</b>, I possess the flexibility to meet diverse technical requirements and achieve project objectives effectively. With a keen
        eye for detail and strong analytical abilities, I specialize in <b>synthesizing complex datasets</b> and <b>deriving meaningful insights</b>. My technical
        prowess, coupled with intellectual curiosity and rigorous approach, ensures successful execution of statistical analysis projects in
        dynamic environments.
        </div>
    """, unsafe_allow_html=True)

# Skills Section
elif selected == "Skills":
    st.header("📶 Skills")
    st.markdown("""
        <div class="content">
        👉 <b>Exploratory statistics & Data Science skills</b><br>
            Linear model, Logistic regression, Discriminant analysis, Inferential Statistics, Multidimensional data analysis (PCA, CFA, MCA),
            Time Series Forecasting, Machine learning (Decision trees, Ensemble Models, support vector machines), Neural networks and deep learning,
            Natural language processing (NLP), Text mining and sentiment analysis, Web scraping<br>
        👉 <b>Big Data Technologies:</b> Spark, Pyspark<br>
        👉 <b>Database Management:</b> SQL, NoSQL<br>
        👉 <b>Data Visualization Tools:</b> Power BI, SAS Viya, Streamlit, Dash, Shiny<br>
        👉 <b>Statistical Software Proficiency:</b> R, Python, SAS, SQL, Stata<br>
        👉 <b>Experimental Design and Hypothesis Testing</b><br>
        👉 <b>Bayesian Statistics</b><br>
        👉 <b>Geomatics:</b> Area map making, Geo-referencing, Representation of digital data in a map (Arcgis, Qgis, Philcarto)
        </div>
    """, unsafe_allow_html=True)

# Projects Section
elif selected == "Projects":
    st.header("✅ Projects")
    st.markdown("""
        <div class="content">
        <b>👉 <a href="https://elhdiagne3.github.io/Portfolio/Projects/Water_Level_Predict1-checkpoint.html" target="_blank"> Sea level forcast</a></b><br>
        Forecast and prediction of daily sea level for the stations of Saint-Joseph, Saint-François and Vieux-Québec;.<br>
        
        <b> 👉 <a href="https://frauddatascraping-bkp.streamlit.app" target="_blank">Web & social Media scraping</a></b><br>
        This is a streamlit web scrapping app to extract insights about fraud data in social media .<br>
        
        <b>Project 3: <a href="https://link_to_project_3.com" target="_blank">School Statistics Dashboard</a></b><br>
        Created a Power BI dashboard to compile and visualize school statistics for the Montreal School Service Center.
        </div>
    """, unsafe_allow_html=True)

# Experience Section 
elif selected =="Experience":
    st.header(" 💻 Experience")
    st.markdown("""
        <div class="content">
        - <b>Data Analyst Fraud and Income Insurance, Orange-Mali</b> (Since Nov. 2020)<br>
            Data processing and analysis (SAS Viya, Python, SQL); <br> Predictive modeling to anticipate fraud (Python), BI Development (Python SAS VIYA).<br>
        - <b>Artificial Intelligence Developer, Maritime Innovation Rimouski</b> (Mar. 2020 - July 2020)<br>
            Processing and analysis of sea level data, Forecast and prediction of daily sea level for the stations of Saint-Joseph, Saint-François, and Vieux-Québec.<br>
        - <b>Data Analyst, Montreal School Service Center (CSDM) Montreal, Canada</b> (Aug. 2020 - Nov. 2020)<br>
            Processing, analysing and reporting on educational achievement data, Development of online data collection applications.<br>
        - <b>Research and Teaching Assistant, UQTR</b> (May 2018 - Sept. 2019)<br>
            Implementation of three machine learning applications for comparison of discriminant analysis models and the Multilayer Perceptron (PMC), Responsible for assisting undergraduate students in Statistics and Probability.<br>
        - <b>Statistician & Regional Manager, National Agency for Statistics and Demography (ANSD) Dakar, Senegal</b> (Feb. 2016 - Jan. 2018)<br>
            Training of survey agents, Regional supervisor of 15 teams of survey agents, Management, processing and analysis of collected data, Member of the analysis report writing team.<br>
        - <b>Intern Statistician, Poison Control Center (PAC) of the Ministry of Health and Social Action Dakar, Senegal</b> (Aug. 2015 - Jan. 2016)<br>
            Development of the data entry application, processing, and analyzing the collected data.
        </div>
    """, unsafe_allow_html=True)

# Education Section
elif selected == "Education":
    st.header("📚 Education")
    st.markdown("""
        <div class="content">
        - <b> Master's degree in Applied Mathematics and Computer Science with thesis</b> - University of Quebec at Trois-Rivieres, Quebec, Canada</b><br>
        <b>  🔍 Research topic: <a href="https://depot-e.uqtr.ca/id/eprint/9412/1/eprint9412.pdf" target="_blank"> Discriminant Analysis and Multilayer Perception - Formal links and applications.<br></b></a> 
        - <b>Machine Learning Module</b> - HEC of the University of Montreal, Canada<br>
            Projects and prediction models via: Decision trees, random forests, neural networks, SVM, regression methods; Association rules applied to business data; Customer segmentation, credit scoring.<br>
        - <b>Bachelor's degree in Applied Statistics and Computer Science</b> - Institute for Studies and Training in Statistics and Project Management and Evaluation (INEFSAGEP), Dakar, Senegal<br>
        - <b>Senior Statistical Technician</b> - National School of Statistics and Economic Analysis (ENSAE), Dakar, Senegal.
        </div>
    """, unsafe_allow_html=True)

# Contact Section
elif selected == "Contact":
    st.header("Contact")
    st.markdown("""
        <div class="content">
        Feel free to reach out to me through the following channels:<br><br>
        - 📨 diagnediaraff@yahoo.fr<br
        - 🏠 178th Street, Fasu Kanu, Bamako, Mali<br>
        - 📞 +223 76 29 98 69<br>
        - 🌍 North Africa, West Africa, North America (Canada)
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Designed by Elhadji Diaraff DIAGNE | © 2024 All Rights Reserved.
    </div>
""", unsafe_allow_html=True)

