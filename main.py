import streamlit as st
from streamlit_option_menu import option_menu

import user,artists,home



st.set_page_config(
    page_title="ArtistryHub"
)

class MultiApp:
    def __init__(self):
        self.apps=[]
    
    def add_apps(self,title,function):
        self.apps.append({
             "title":title,
            "function":function
        })
    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='ArtistryHub',
                options=['Home','Artist','User'],
                icons=['house-fill','person-circle','key'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
       
        if app == "Home":
            home.app()
        if app == "Artist":
            artists.app()    
        if app == 'User':
            user.app()
  

    run()
     


# query = "SELECT name, pet FROM mytable"
# mycursor.execute(query)

# Fetch all rows from the executed query
# result = mycursor.fetchall()

# # Display the data in a table format using Streamlit
# st.subheader("Pets Information")
# for row in result:
#     st.write(f"Name: {row[0]}, Pet: {row[1]}")



