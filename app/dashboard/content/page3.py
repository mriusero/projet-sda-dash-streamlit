import streamlit as st
from ..components import create_candlestick_chart2
from ..functions import text_analysis, predict, resample
import pandas as pd
def page_3(market_data, tweet_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#3 Preprocessing</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Description_</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Twitter data_ </div>', unsafe_allow_html=True)
    st.dataframe(tweet_data)

    st.markdown('<div class="subheader">Process_ </div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Results_ </div>', unsafe_allow_html=True)
    frequency = st.selectbox("Select a period", ['60min', '6H', '12H', 'Daily', 'Weekly'])



    size = st.selectbox("Select the size analyse", ['100%', '50%', '25%', '10%', '1%'])
    datasize = len(tweet_data['text']) + 1

    if size == '100%':
        arg_size = datasize
    elif size == '50%':
        arg_size = round(datasize * 0.5)
    elif size == '25%':
        arg_size = round(datasize * 0.25)
    elif size == '10%':
        arg_size = round(datasize * 0.1)
    elif size == '1%':
        arg_size = round(datasize * 0.01)

    st.markdown("Launch analyse:")
    clicked1 = st.button("►")
    if clicked1:
        preprocessed_df, daily_sentiment = text_analysis(tweet_data.head(arg_size), frequency)
        st.dataframe(daily_sentiment)

    clicked2 = st.button("Predict")
    if clicked2:
        predictions = predict(market_data, frequency)

        date_limit = pd.Timestamp('2021-03-12 23:59:14+00:00')
        filtered_data = market_data[market_data['Timestamp'] < date_limit]

        display_data = resample(filtered_data, frequency)
        candlestick_chart = create_candlestick_chart2(display_data, predictions)

        st.markdown("branch_structure_initialisation")
        st.plotly_chart(candlestick_chart)
        st.dataframe(predictions)