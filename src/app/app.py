import streamlit as st
import json

from game.game import Game

class App:
    
    def run(self):
        st.title("Rock Paper Scissor")
        game_dict = {1:"Rock", 2:"Paper", 3:"Scissor"}
        st.json(game_dict)
        user_name = st.text_input("Enter your name: ")
        if user_name:
            game = Game(user_name)
            user_input = st.number_input('Enter number: ', min_value=1, max_value=3, step=1, value=None)

            if user_input is not None:
                st.write(f"User Choice is: {game_dict[user_input]}")
                if st.button("PLAY!"):
                    result = game.game_rps(user_input)
                    st.write(result)

