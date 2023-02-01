import streamlit as st
import pandas as pd
import os
import os.path

valid_pwd = 'password'
valid_login = 'login'

def check_password():
    """Returns True if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == valid_pwd and st.session_state["login"] == valid_login:
            st.session_state["password_correct"] = True 
            del st.session_state["password"]  # don't store password
            del st.session_state["login"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Login", on_change=password_entered, key="login"
        )
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Login", on_change=password_entered, key="login"
        )
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Username/password is incorrect")
        return False
    else:
        # Password correct.
        return True



a = check_password()
if a == True:

    DATA_PATH = os.path.join(os.path.dirname('__file__'), 'best_scores.csv')
    #DATA_PATH = "C:/Users/clagneau/Desktop/CF reco/git frontend/best_scores.csv"

    df = pd.read_csv(DATA_PATH)

    st.title('Prédiction de recommandation pour Efalia Docs')
    list_of_users = []
    Users = (df['distinct_id'])
    for i in Users:
        list_of_users.append(i)

    user = (st.selectbox('Choisissez l\'utilisateur',list_of_users))
    recommandations = (df.loc[df['distinct_id'] == user])
    values = recommandations.iloc[0].tolist()
    # for j in recommandations.values:
    #     values.append(j)

    if st.button('Voir les recommandations'):
        st.write('Voici vos 5 documents qui peuvent vous intéresser !')
        st.write(values[1:6])
        st.write('Nous avons estimé un score pour l\'intéret de chaque document')
        st.write(values[6:11])
