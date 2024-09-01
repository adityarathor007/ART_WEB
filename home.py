import streamlit as st
from db import mydb,mycursor

def fetch_artworks():
    query = """
    SELECT Art_id, Name, Category, Size, Image, Availability, Price, Status, DateFirstAvailable 
    FROM Artwork_Listing
    WHERE Availability = TRUE AND Status = 'Available'
    """
    
    mycursor.execute(query)
    artworks = mycursor.fetchall()
    
   
    column_names = [column[0] for column in mycursor.description]
    artworks = [dict(zip(column_names, row)) for row in artworks]
    
    return artworks


def fetch_artwork_details(art_id):
    query = """
    SELECT 
        a.Art_id, 
        a.Name AS Artwork_Name, 
        a.Artist_Id, 
        ap.name AS Artist_Name,
        a.Category, 
        a.Size, 
        a.Image, 
        a.Availability, 
        a.Price, 
        a.Status, 
        a.DateFirstAvailable
    FROM Artwork_Listing a
    JOIN Artist_Profile ap ON a.Artist_Id = ap.Artist_Id
    WHERE a.Art_id = %s
    """
    mycursor.execute(query, (art_id,))
    artwork = mycursor.fetchone()
    column_names = [column[0] for column in mycursor.description]
    return dict(zip(column_names, artwork)) if artwork else None


def app():
    
    
    if 'selected_artwork_id' not in st.session_state:
        st.session_state.selected_artwork_id = None

    if st.session_state.selected_artwork_id:
        artwork = fetch_artwork_details(st.session_state.selected_artwork_id)
        if artwork:
            st.subheader(artwork['Artwork_Name'])
            st.image(artwork['Image'], width=400)
            st.write(f"**Category:** {artwork['Category']}")
            st.write(f"**Size:** {artwork['Size']}")
            st.write(f"**Price:** ${artwork['Price']:.2f}")
            st.write(f"**Status:** {artwork['Status']}")
            st.write(f"**Date First Available:** {artwork['DateFirstAvailable']}")
            st.write(f"**Availability:** {'Available' if artwork['Availability'] else 'Not Available'}")
            st.write(f"**Artist Name:** {artwork['Artist_Name']}")
            if st.button("Back to Listings"):
                st.session_state.selected_artwork_id = None
        else:
            st.write("Artwork details not found.")
        return
    
    artworks = fetch_artworks()
    
    if not artworks:
        st.write("No artworks available.")
        return
    
    st.title("Artwork Listings")

    num_columns = 2
    card_width = 300  # Width of each card
    card_height = 500  # Height of each card
    image_height = 250  # Height of the image within the card

    # Create cards with fixed dimensions
    for i in range(0, len(artworks), num_columns):
        cols = st.columns(num_columns)
        
        for idx, artwork in enumerate(artworks[i:i+num_columns]):
            with cols[idx]:
                if st.button(artwork['Name'], key=artwork['Art_id']):
                    st.session_state.selected_artwork_id = artwork['Art_id']

                # Define card layout
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; width: {card_width}px; height: {card_height}px; overflow: hidden;">
                        <img src="{artwork['Image']}" style="width: {card_width}px; height: {image_height}px; object-fit: cover;">
                        <h3>{artwork['Name']}</h3>
                        <p><strong>Price:</strong> ${artwork['Price']:.2f}</p>
                        <p><strong>Date First Available:</strong> {artwork['DateFirstAvailable']}</p>
                    </div>
                """, unsafe_allow_html=True)
                st.write("---")

if __name__ == "__main__":
    app()





# def app():
    # st.title("Artwork Listings")

    # artworks = fetch_artworks()
    
    # if not artworks:
    #     st.write("No artworks available.")
    #     return
    
    # num_columns = 2
    # card_width = 300  # Width of each card
    # card_height = 500  # Height of each card
    # image_height = 250  # Height of the image within the card

    # selected_artwork_name = None
    
    # # Create cards with fixed dimensions
    # for i in range(0, len(artworks), num_columns):
    #     cols = st.columns(num_columns)
        
    #     for idx, artwork in enumerate(artworks[i:i+num_columns]):
    #         with cols[idx]:
                
    #             if st.button(artwork['Name'], key=artwork['Art_id']):
    #                 selected_artwork_name = artwork['Name']


    #             # Define card layout
    #             st.markdown(f"""
    #                 <div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; width: {card_width}px; height: {card_height}px; overflow: hidden;">
    #                     <img src="{artwork['Image']}" style="width: {card_width}px; height: {image_height}px; object-fit: cover;">
    #                     <h3>{artwork['Name']}</h3>
    #                     <p><strong>Price:</strong> ${artwork['Price']:.2f}</p>
    #                     <p><strong>Date First Available:</strong> {artwork['DateFirstAvailable']}</p>
    #                 </div>
    #             """, unsafe_allow_html=True)
    #             st.write("---")
