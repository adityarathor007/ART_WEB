import mysql.connector
import os
from dotenv import load_dotenv
import bcrypt
import mysql

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

mycursor=mydb.cursor()
print("Connection Established")

# def hash_password(password):
#     """Encrypt the password using bcrypt."""
#     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# def insert_user(password, name, email, phone_no):
#     """Insert a new user into the database with hashed password."""
#     hashed_password = hash_password(password)
#     sql = "INSERT INTO Artist_Profile (password, name, email, biography) VALUES (%s, %s, %s, %s)"
#     values = (hashed_password, name, email, phone_no)
#     mycursor.execute(sql, values)
#     mydb.commit()
#     print(f"Inserted user: {name}")

# # Data to be inserted
# artist_data = [
#    ('artistPass123', 'Ravi Sharma', 'ravi.sharma@artmail.com', 'I am Ravi Sharma, a painter with a passion for vibrant landscapes and modern abstract art. My works have been showcased in various galleries across India, and I strive to capture the essence of life through my paintings.'),
#     ('creativePass456', 'Sita Patel', 'sita.patel@artmail.com', 'I am Sita Patel, specializing in contemporary sculpture and mixed media art. My innovative pieces have won several awards and have been featured in international exhibitions. I love exploring new materials and techniques in my art.'),
#     ('artisticPass789', 'Arjun Reddy', 'arjun.reddy@artmail.com', 'I am Arjun Reddy, a digital artist dedicated to exploring the intersection of technology and art. I have been a pioneer in the digital art space, participating in numerous digital art festivals and pushing the boundaries of digital creativity.')
# ]

# # Insert each user into the database
# for password, name, email, bio in artist_data:
#     insert_user(password, name, email, bio)

# print("All users have been inserted with encrypted passwords.")

# # Close database connection
# mycursor.close()
# mydb.close()