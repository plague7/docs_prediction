import streamlit as st
import pandas as pd
import os
import os.path

DATA_PATH = os.path.join(os.path.dirname('__file__'), 'best_scores.csv')
#DATA_PATH = r"C:\Users\clagneau\Desktop\CF reco\front end\best_scores.csv"

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
