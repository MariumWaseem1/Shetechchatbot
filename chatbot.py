# import streamlit as st

# def rule_based_chatbot(user_input):
#     responses = {
#         "hello": "Hi there!",
#         "how are you": "I'm just a chatbot, but thanks for asking!",
#         "bye": "Goodbye! Have a great day!",
        # "What is SheTech": "SheTech is an online platform that aims to encourage women to join the tech world",
        # "Who is your founder?": "Marium waseem",
        # "What is your name?": " SheTech Bot",
        # "How old are you? " : "Few hours old ",
        # "What is your favourite color" : "Pink ",
#     }
    
#     response = responses.get(user_input.lower(), "I'm not sure how to respond to that.")
#     return response

# def main():
#     st.title("SheTech Chatbot")
#     st.markdown("<h1 style='color: #EF7E88;'>SheTech Chatbot</h1>", unsafe_allow_html=True)

#     user_input = st.text_input("You:", value="")
#     if user_input:
#         bot_response = rule_based_chatbot(user_input)
#         st.text(f"<div style='color: #FF8FC;'>Bot: {bot_response}</div>", unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()

import streamlit as st

def rule_based_chatbot(user_input):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm just a chatbot, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "What is SheTech": "SheTech is an online platform that aims to encourage women to join the tech world",
        "Who is your founder?": "Marium waseem",
        "What is your name?": " SheTech Bot",
        "How old are you? " : "Few hours old ",
        "What is your favourite color" : "Pink ",
    }
    
    response = responses.get(user_input.lower(), "I'm not sure how to respond to that.")
    return response

def main():
    # st.title("Simple Chatbot")
    st.markdown("<h1 style='color: #EF7E88;'>SheTech Chatbot</h1>", unsafe_allow_html=True)


    user_input = st.text_input("You:", value="")
    if user_input:
        bot_response = rule_based_chatbot(user_input)
        st.text(f"M3: {bot_response}")

if __name__ == "__main__":
    main()

 