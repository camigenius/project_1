import random
import streamlit as st



st.title("My first program Streamlit")

options = ['Piedra','Papel','Tijeras']

user_select = st.selectbox('Select one option : ' , options )

random_options = (random.randint(0,2))
computer_option = options[random_options]

st.write("User select 🤖:",user_select)
st.write("Computer select 👨‍💻: " ,computer_option)


# print(user_select)
# print(computer_option)

if user_select == computer_option:
    st.header("Empate!! 😖")

elif user_select == 'Piedra':
    if computer_option == 'Tijeras':
        st.header('Usuario Gana Piedra rompe Tijeras 😀')
    else :
        if computer_option == 'Papel':
            st.header('Computador Gana papel tapa a Piedra 🤖')

elif user_select == 'Papel':
    if computer_option == 'Tijeras':
        st.header("Computador Gana Tijeras corta Papel 😢🤖")
    else :
        if computer_option == 'Piedra':
            st.header("Usuario Gana Papel tapa a piedra🤪") 

elif user_select == 'Tijeras':
    if computer_option == 'Piedra':
        st.header("Computador Gana Piedra rompe Tijeras😢🤖")
    else :
        if computer_option == 'Papel':
            st.header("Usuario Gana Tijeras corta Papel🤪")