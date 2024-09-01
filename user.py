import streamlit as st
from db import mydb,mycursor
import mysql
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))


def create_user(email, name, password, phone_no):
    try:
        hashed_password = hash_password(password)
        sql = "INSERT INTO User (email, name, password, phone_no) VALUES (%s, %s, %s, %s)"
        values = (email, name, hashed_password, phone_no)
        mycursor.execute(sql, values)
        mydb.commit()
        st.success("Account created successfully!")
        st.markdown("Now Login with your email and password")

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

def login(email, password):
        try:
            # Select name, email, and password from the User table
            sql = "SELECT name, email, password FROM User WHERE email = %s"
            mycursor.execute(sql, (email,))
            user = mycursor.fetchone()
        
            if user:
                name, user_email, stored_password = user
                if check_password(stored_password, password):
                    st.success("Login successful!")
                    
                    # Store user information in the session state
                    st.session_state['username'] = name
                    st.session_state['useremail'] = user_email
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





    




def app():
    
    
    if 'username' not in st.session_state:
        st.session_state.username=''
    if 'useremail' not in st.session_state:
        st.session_state.useremail=''


    if 'signedout' not in st.session_state:
        st.session_state.signedout=True

    if st.session_state['signedout']: #means user is not signed in
        st.title('Welcome to :violet[ArtistryHub] 🎨, Enter your user credentials')

        choice = st.selectbox('Login/Signup',['Login','Sign up'])

        if choice == 'Login':
                
            # username = st.text_input("Enter your name")
            email = st.text_input('Email Address')
            password = st.text_input('Password',type='password')

            st.button('Login', on_click=login, args=(email, password))
            
        else:
            email = st.text_input('Email Address')
            password = st.text_input('Password',type='password')
            confirm_password = st.text_input('Confirm Password', type='password')
            username=st.text_input('enter your username')
            phone_no=st.text_input('Phone No: ')


            if st.button('Create my account'):
                if password != confirm_password:
                    st.error("Passwords do not match!")
                else:
                    create_user(email, username, password, phone_no)
    

    else:
        st.title('Hi there 👋, Here is your basic info')
        st.text("Name "+st.session_state.username)
        st.text("Email Id "+st.session_state.useremail)
        st.button('Sign_Out', on_click=logout)


