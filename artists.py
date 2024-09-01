import streamlit as st
from db import mydb,mycursor
import bcrypt
import mysql


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

def login(email, password):
        try:
            # Select name, email, and password from the User table
            sql = "SELECT name, email, password,biography FROM Artist_Profile WHERE email = %s"
            mycursor.execute(sql, (email,))
            user = mycursor.fetchone()
        
            if user:
                name, user_email, stored_password,biography = user
                if check_password(stored_password, password):
                    st.success("Login successful!")
                    
                    # Store user information in the session state
                    st.session_state['username'] = name
                    st.session_state['useremail'] = user_email
                    st.session_state['bio']=biography
                    st.session_state.signedout=False
                else:
                    st.error("Invalid password")
            else:
                st.error("User not found")


        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

    
def logout():
        st.session_state.signedout=True
        
        st.session_state.username=''
        st.session_state.useremail=''
        st.session_state.bio=''

def create_artist(email, name, password, bio):
    try:
        hashed_password = hash_password(password)
        sql = "INSERT INTO Artist_Profile (email, name, password, biography) VALUES (%s, %s, %s, %s)"
        values = (email, name, hashed_password, bio)
        mycursor.execute(sql, values)
        mydb.commit()
        st.success("Account created artist successfully!")
        st.markdown("Now Login with your email and password")

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

def app():
    
    
    if 'username' not in st.session_state:
        st.session_state.username=''
    if 'useremail' not in st.session_state:
        st.session_state.useremail=''

    if 'bio' not in st.session_state:
        st.session_state.bio=''

    if 'signedout' not in st.session_state:
        st.session_state.signedout=True

    

    if st.session_state['signedout']: #means user is not signed in
        st.title('Welcome to :violet[ArtistryHub] 🎨, Enter your artist credentials')

        choice = st.selectbox('Login/Signup',['Login','Sign up'])

        if choice == 'Login':
                
            email = st.text_input('Email Address')
            password = st.text_input('Password',type='password')

            st.button('Login', on_click=login, args=(email, password))
            
        else:
            email = st.text_input('Email Address')
            password = st.text_input('Password',type='password')
            confirm_password = st.text_input('Confirm Password', type='password')
            username=st.text_input('enter your username')
            biography=st.text_input('enter your bio')


            if st.button('Create my account'):
                if password != confirm_password:
                    st.error("Passwords do not match!")
                else:
                    create_artist(email, username, password,biography)
    

    else:
        st.title('Hi there 👋, Here is your basic info')
        st.text("Name "+st.session_state.username)
        st.text("Email Id "+st.session_state.useremail)
        st.text("Bio "+st.session_state.bio)

        st.button('Sign_Out', on_click=logout)


