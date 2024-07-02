import base64
import streamlit as st
import time

from video import show_video,render_image

start = st.button("Start")

code = [
    "Episode 100	Average Score: -164.29",
    "Episode 200	Average Score: -113.19",
    "Episode 300	Average Score: -49.61",
    "Episode 400	Average Score: -16.79",
    "Episode 500	Average Score: 129.39",
    "Episode 551	Average Score: 200.98",
    "Environment solved in 451 episodes!	Average Score: 200.98"]

if start:

    progress_text = "model traing in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    tim=[15,30,45,60,75,85,99]
    tim1={15:0,30:1,45:2,60:3,75:4,85:5,99:6}
    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
        if percent_complete in tim:
            a=tim1[percent_complete]
            st.code(code[a])
    time.sleep(1)
    my_bar.empty()

    st.title("plot for score awarding in episodes")

    render_image("score chart.png")
    
    st.title("short video of model training mostly fail landings")

    show_video("fail landing.gif")
    
    st.title("short video of model training better control landings")

    show_video("okay landing.gif")

    st.title("short video of model training mostly perfect landings")

    show_video("final landing.gif")

    