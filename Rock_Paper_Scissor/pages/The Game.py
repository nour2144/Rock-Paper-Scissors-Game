import streamlit as st
import random
import time
import getpass
from itertools import combinations_with_replacement
# Page configuration
st.set_page_config(page_title='Betta Ai', page_icon='📈', layout="wide", initial_sidebar_state="collapsed")
st.logo('../images/logo.png', icon_image='../images/neww.png')
st.sidebar.title("Hi There!")
st.sidebar.markdown("Take a look at my website :shark:")
# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'messages_input' not in st.session_state:
    st.session_state.messages_input = 'ask anything'
if 'prediction_steps' not in st.session_state:
    st.session_state.prediction_steps = 'welcome_message'
if 'user_details' not in st.session_state:
    st.session_state.user_details = []
if 'game_mode' not in st.session_state:
    st.session_state.game_mode = 0
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if 'first_play' not in st.session_state:
    st.session_state.first_play = 0
if 'result' not in st.session_state:
    st.session_state.result = 0
if 'scores' not in st.session_state:
    st.session_state.scores = [0,0]
if 'chooses' not in st.session_state:
    st.session_state.chooses = [0,0]
if 'players_names' not in st.session_state:
    st.session_state.players_names = ['','']


# Predefined chats
chats = {
    ('rules',): [
        '''**Players and Moves: Each player simultaneously forms one of three shapes with their hand :**
        
**Rock (a closed fist) Paper (an open hand) Scissors (a fist with the index and middle fingers extended, forming a V)**'''
    ],
    ('game','win'): [
        '''**The first player to score 3 points win the Game 😄**
        
1 - Rock crushes Scissors: Rock wins against Scissors.
        
2 - Scissors cuts Paper: Scissors win against Paper.
            
3 - Paper covers Rock: Paper wins against Rock.
            
4 - Ties: If both players choose the same shape, the game is a tie, and no one wins.'''
    ],
}

# Function to get a response based on prompt
def get_value(prompt):
    for keys in chats.keys():
        for key in keys:
            if prompt in key or key in prompt:
                return random.choice(chats[keys])
    return 'Unknown command due to limited information right now 😄..'

# Chat input field
prompt = st.chat_input(st.session_state.messages_input)
if st.session_state.prediction_steps in ['welcome_message']:
        response = '''**Welcome to the Rock-Paper-Scissors Challenge! 🥌📄✂️**

Get ready to test your skills in this classic game of strategy and chance. Will you choose rock, paper, or scissors? Each move counts, and every round is a new opportunity to outsmart your opponent. Remember, it’s not just about luck; it's about reading your opponent and making the right call.

if you need any aditional information you can write rules or how to win . or start to start playing 🎲.

**Good luck, and may the best move win! Let’s play! 😄**'''
        st.session_state.prediction_steps = 'second_phase'
        st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": response})
# If there is input, add it to the conversation history
if prompt:
    if st.session_state.game_mode != 1:
        st.session_state.messages.append({"name": "User", "avatar": '../images/user.png', "message": f"{prompt}"})
    if st.session_state.prediction_steps in ['second_phase']:
        if 'win' in prompt or 'rules' in prompt :
            response = get_value(prompt)
        elif 'start' in prompt :
            st.session_state.prediction_steps = 'decide'
            start_response = '''**Welcome, brave challenger, to the arena of Rock-Paper-Scissors!** 🎮

The stage is set, the opponents are ready, and the stakes are high. Every choice you make could lead to glory or defeat. Are you ready to put your wits to the test and claim victory? 🎖️

**Let the games begin... and may the odds be ever in your favor! 🔥**'''
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": start_response})
            
            # Show toast messages
            msg = st.toast('Starting the Game ...')
            time.sleep(1)
            msg.toast('Game is ON', icon='🔥')
            time.sleep(1)
            msg.toast('Ready!', icon="🥞")
            
            # Automatically move to the decision phase message
            response = '**Hello! Ready to play? 🎮** Do you want to challenge a friend (1 vs 1) or face the computer (1 vs Computer)? Please type "1" for a friend or "2" for the computer.'
    elif st.session_state.prediction_steps in ['decide']:
        if prompt == '1':
            st.session_state.game_mode = 1
            response = '''Enter your name player 1, valiant challenger, and prepare for an epic 1 vs 1 duel! Your name will be etched in the history of this grand battle! 🎖️'''
            message = '**Fantastic!** You’ve chosen to battle it out with a friend in an epic 1 vs 1 showdown! Get ready to throw down, strategize, and see who reigns supreme! Let’s rock this game! 🚀'
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
        
        else:
            st.session_state.game_mode = 2
            response = '''Enter your name player 1, brave one, so that I may know you and your name will be immortalized in the annals of history! 🎖️'''
            message = '**🤖 Awesome choice!** You’re going head-to-head with the computer in a thrilling 1 vs Computer match! Can you outsmart the machine? Let’s find out! Game on! 💥💣 '
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
            
        st.session_state.prediction_steps = 'players'
    elif st.session_state.prediction_steps in ['players']:
        if st.session_state.game_mode == 1:
            if st.session_state.counter == 0:
                message = f'Welcome, {prompt}! You are now set for an epic 1 vs 1 battle. Prepare yourself for a thrilling showdown'
                st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                response = 'Enter your name Player 2, worthy adversary, and get ready for an epic 1 vs 1 showdown.'
                st.session_state.players_names[0] = prompt
                st.session_state.counter = 1
            else :
                message = f'Welcome, {prompt}! You are now set for an epic 1 vs 1 battle against {st.session_state.players_names[0]} ({prompt}⚔️{st.session_state.players_names[0]})'
                st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                st.session_state.players_names[1] = prompt
                st.session_state.counter = 0
                response = '''Let’s see who will have the honor of starting first... 🤔
The anticipation builds as we wait to see which warrior will make the first move in this epic battle! 🥁✨'''
                st.session_state.first_to_play = random.randint(0,1)
                message = f'''{st.session_state.players_names[0-st.session_state.first_to_play]} is playing first then {st.session_state.players_names[1-st.session_state.first_to_play]}'''
                st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                message = '🔥 "The game has ignited! May the best player emerge victorious!" 🔥'
                st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                response = f'''🔥 The game has begun! 🔥

Player {st.session_state.players_names[0-st.session_state.first_to_play]}, it's your turn to choose! Will you pick rock, paper, or scissors? (1,2,3) Make your choice wisely and prepare for an epic battle! 💥'''
                st.session_state.prediction_steps = 'play'
        else :
            message = f"Welcome, {prompt}! You are now set to take on the ultimate challenge against the computer. Prepare yourself for an exhilarating battle of wits and strategy—it's you versus the machine!"
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
            st.session_state.players_names[0] = prompt
            st.session_state.players_names[1] = 'Computer'
            message = '''Let’s see who will have the honor of starting first... 🤔
The anticipation builds as we wait to see which warrior will make the first move in this epic battle! 🥁✨'''
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
            st.session_state.first_to_play = 0 #random.randint(0,1)
            message = f'''{st.session_state.players_names[0-st.session_state.first_to_play]} is playing first then {st.session_state.players_names[1-st.session_state.first_to_play]}'''
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
            message = '🔥 "The game has ignited! May the best player emerge victorious!" 🔥'
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
            response = f"{st.session_state.players_names[0-st.session_state.first_to_play]}, it's your turn to choose! Will you pick rock, paper, or scissors? (1,2,3) Make your choice wisely"
#             if st.session_state.players_names[0-st.session_state.first_to_play] == 'Computer':
#                 st.session_state.messages.append({"name": "Deep Ai", "avatar": 'images/robot.png', "message": message})
#                 choice = random.randint(1,3)
#                 st.session_state.chooses[0-st.session_state.first_to_play] = choice
#                 st.session_state.messages.append({"name": "Deep Ai", "avatar": 'images/robot.png', "message": f'{choice}'})
#                 response = f"{st.session_state.players_names[1-st.session_state.first_to_play]}, it's your turn to choose! Will you pick rock, paper, or scissors? (1,2,3)"
#             else:
#                 response = message
                
            st.session_state.prediction_steps = 'play'
#   222222222222
    elif st.session_state.prediction_steps in ['play']:
        if  st.session_state.game_mode == 1 :
            if st.session_state.counter == 0 :
                response = f"{st.session_state.players_names[1-st.session_state.first_to_play]}, it's your turn to choose! Will you pick rock, paper, or scissors? (1,2,3)"
                st.session_state.chooses[0-st.session_state.first_to_play] = prompt
                st.session_state.counter = 1
            else:
                message = "⚔️ The choices are in! ⚔️ Player 1 and Player 2 have both made their moves. Let's see who emerges victorious in this thrilling round! Stay tuned for the results... 🥳"
                st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                st.session_state.chooses[1-st.session_state.first_to_play] = prompt
                st.session_state.result = 1
                st.session_state.counter = 0
        elif st.session_state.game_mode == 2 :
            st.session_state.chooses[0-st.session_state.first_to_play] = prompt
            message = f"{st.session_state.players_names[1-st.session_state.first_to_play]}, it's your turn to choose! Will you pick rock, paper, or scissors? (1,2,3)"
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
            choice = random.randint(1,3) 
            st.session_state.chooses[1-st.session_state.first_to_play] = str(choice)
            message = "⚔️ The choices are in! ⚔️ Player 1 and Player 2 have both made their moves. Let's see who emerges victorious in this thrilling round! Stay tuned for the results... 🥳"
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
            st.session_state.result = 1
            st.session_state.counter = 0
        if st.session_state.result == 1 :
                
                player_1_choose = st.session_state.chooses[0-st.session_state.first_to_play]
                player_2_choose = st.session_state.chooses[1-st.session_state.first_to_play]
                if player_1_choose == player_2_choose:
                    message = '''🤝 It's a Tie! 🤝

Both players have made equally matched moves, resulting in a draw. No winner this round 🌟'''
                    st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                elif (player_1_choose == '1' and player_2_choose == '3') or (player_1_choose == '2' and player_2_choose == '1') or (player_1_choose == '3' and player_2_choose == '2') :
                    st.session_state.scores[0-st.session_state.first_to_play]+=1
                    message = f'''🌟 Well Done, player {st.session_state.players_names[0-st.session_state.first_to_play]}! 🌟

You've scored a point and are one step closer to victory! Keep up the great work and stay focused. The next round could be the game-changer! 🏅🔥'''
                    st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                else:
                    st.session_state.scores[1-st.session_state.first_to_play]+=1
                    message = f'''🌟 Well Done, player {st.session_state.players_names[1-st.session_state.first_to_play]}! 🌟

You've scored a point and are one step closer to victory! Keep up the great work and stay focused. The next round could be the game-changer! 🏅🔥'''
                    st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                message = f'''🏆 Current Score 🏆

Player {st.session_state.players_names[0-st.session_state.first_to_play]}: { st.session_state.scores[0-st.session_state.first_to_play]} | Player {st.session_state.players_names[1-st.session_state.first_to_play]}: { st.session_state.scores[1-st.session_state.first_to_play]}

The battle is heating up! Keep playing to see who will claim victory. May the best player win! 🔥✨'''
                st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                if st.session_state.scores[0] == 3 or st.session_state.scores[1] == 3:
                    if st.session_state.scores[0-st.session_state.first_to_play] == 3:
                        message = f'''🎉 Congratulations, {st.session_state.players_names[0-st.session_state.first_to_play]}! You have won the game! 🏆

Your strategy and skills have led you to victory. Well played! Enjoy your triumph, champion! 🔥🚀'''
                        st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                    else :
                        message = f'''🎉 Congratulations, {st.session_state.players_names[1-st.session_state.first_to_play]}! You have won the game! 🏆

Your strategy and skills have led you to victory. Well played! Enjoy your triumph, champion! 🔥🚀'''
                        st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
                    st.session_state.scores = [0,0]
                    response = '''Would you like to play another round and continue the fun, or is it time to call it a day?

Type "play again" to start a new game, or "end game" if you’re done for now. The choice is yours! 🎮✨'''
                    st.session_state.prediction_steps = 'check'
                else :
                    response = f'''Player {st.session_state.players_names[0-st.session_state.first_to_play]}, it's your turn to choose! Will you pick rock, paper, or scissors? (1,2,3) Make your choice wisely and prepare for an epic battle! 💥'''
                st.session_state.result = 0
    elif st.session_state.prediction_steps == 'check':
        if 'play' in prompt or 'again' in prompt or prompt.startswith('p'):
            response = f'''Player {st.session_state.players_names[0-st.session_state.first_to_play]}, it's your turn to choose! Will you pick rock, paper, or scissors? (1,2,3) Make your choice wisely and prepare for an epic battle! 💥'''
            message = "Fantastic choice! 🎉 Get ready for another exciting round. Let's see if you can keep the winning streak going or turn the tables this time. Game on! 🚀"
            st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": message})
            st.session_state.prediction_steps = 'play'
        else:
            response = "Thank you for playing! 🎮 It’s been a thrilling ride. Whether you won or lost, you played well! Until next time, champion. Farewell and keep that competitive spirit alive! 🏆👋"
            st.session_state.messages_input = 'ask anything'
            st.session_state.prediction_steps = 'second_phase'
            st.session_state.user_details = []
            st.session_state.game_mode = 0
            st.session_state.counter = 0
            st.session_state.first_play = 0
            st.session_state.result = 0
            st.session_state.scores = [0,0]
            st.session_state.chooses = [0,0]
            st.session_state.players_names = ['','']
    st.session_state.messages.append({"name": "Deep Ai", "avatar": '../images/robot.png', "message": response})
            
        
# Display the conversation history
for chat in st.session_state.messages:
    st.chat_message(name=chat["name"], avatar=chat["avatar"]).write(chat["message"])
