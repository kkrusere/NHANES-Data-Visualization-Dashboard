
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import matplotlib.pyplot as plt
from wordcloud import WordCloud

import json
from bs4 import BeautifulSoup
import pandas as pd
import datetime 
import random
# Import date class from datetime module
from datetime import date

import datetime
#import config

import pickle as pkle
import os.path

from streamlit_server_state import server_state, server_state_lock

import requests
import streamlit.components.v1 as components

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


st.set_page_config(page_title="YouTube_comment_Analysis_Dash_App", page_icon="", layout="wide")


with st.sidebar:
    choose = option_menu("Dash Menu", ["About the Project", "Video Summery Stats", "Topic Search", "Sentiment Analysis", "WordCloud"],
                         icons=['','', '','', ''],
                         menu_icon="youtube", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#636EFA"},
    }
    )


if choose == "About the Project":
#Add the cover image for the cover page. Used a little trick to center the image
    col1, col2, col3 = st.columns((.1,1,.1))

    with col1:
        st.write("")

    with col2:
        st.markdown(" <h1 style='text-align: center;'>YouTube Comment Analyser</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><i><b> YouTube-comments-Analyzer is a tool to analyze audience sentiment, "
                "perspective, topics, and engagement of YouTube video comments. It collects and preprocesses comments, performs "
                "sentiment analysis and topic modeling, and visualizes findings through an interactive dashboard. Beneficial for "
                "content creators, marketers, and researchers. </b></i></p>", unsafe_allow_html=True)
        st.markdown("<center><img src='https://github.com/kkrusere/Market-Basket-Analysis-on-the-Online-Retail-Data/blob/main/Assets/comments_analyzer.jpg?raw=1' width=300/></center>", unsafe_allow_html=True)

    with col3:
        st.write("")

    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown("#### **About the Project:**")

        st.markdown("""
                
                ##### **Abstract**

                
        """)

        st.markdown("##### ***Project Contributors:***")
        st.markdown("Kuzi Rusere")
        

elif choose == "Video Summery Stats":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: black;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Video Summery Stats</p>', unsafe_allow_html=True)
    keywords = ["Sentiment-Analysis"] # this is going to be our keyword 



    st.markdown("---")
    ######################################################################


#######################################################*******************************************************####################################################################

elif choose == "Topic Search":
    #Add a file uploader to allow users to upload their project plan file
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: black;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Topic Search</p>', unsafe_allow_html=True)
    #creating a list of the survey cycles that we are going to be collecting the data


    st.markdown("---")
    ######################################################################

############################################################*******************************************########################################################

elif choose == "Sentiment Analysis":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: black;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Sentiment Analysis</p>', unsafe_allow_html=True)

    st.markdown("---")
    ######################################################################
    
#######################################################*******************************************###############################################################


elif choose == "WordCloud":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: black;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">WordCloud</p>', unsafe_allow_html=True)

    st.markdown("---")
    ######################################################################