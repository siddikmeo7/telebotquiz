from connection import * 

                                # DATABASE

# CREATING TABLE OF USERS FROM TELEGRAM WHERE THEY WILL BE REGISTERED
def create_T_users ():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
        id serial primary key ,
        telegram_id numeric ,
        username varchar (50) unique ,
        registered_at timestamp default current_timestamp 
    );
    """)
    conn.commit()
    close_connection(conn,cur)

# CREATING TABLE OF PRODUCTS FOR TELEGRAM USERS 
# ADMINS CAN ADD/UPDATE/DELETE/SEE PRODUCTS
# USERS CAN ONLY SEE/ORDER PRODUCTS
def  create_T_products ():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PRODUCTS (
        id serial primary key ,
        name varchar (50) ,
        description text ,
        price int ,
        photo_prod bytea ,
        created_at timestamp default current_timestamp
    );
    """)
    conn.commit()
    close_connection(conn,cur)

# CREATING TABLE OF CARTS 
# WHERE WILL BE SAVED OUR HISTORY OF ORDING PRODUCTS
def create_T_carts():
    conn = open_connection()
    cur = conn.cursor()  # Create the cursor here
    try:
        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS CARTS (
            id serial primary key,
            user_id int references USERS (id),
            prod_id int references PRODUCTS (id),
            quantity_prod int,
            created_at timestamp default current_timestamp
        );
        """)
        conn.commit()
    except Exception as e:
        print(f"Error creating CARTS table: {e}")
    finally:
        cur.close()  # Close the cursor
        conn.close()  # Close the connection

# FUNCTION THAT WILL ADD * NEWUSERS TO DATABASE
def user_register (message):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""
    INSERT INTO USERS (telegram_id,username)
    VALUES 
    ({message.chat.id},'{message.chat.username}');
    """)
    conn.commit()
    close_connection(conn,cur)


# FUNTION THAT WILL CHECK WETHER USER IS REGISTERED OR NOT TO REGISTER NEW_USERS,
# AND TO PASS ALREADY REGISTERED USERS
def is_registered(message):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""select * from users 
                where id = {message.chat.id} 
                """)
    is_registeredd = cur.fetchone()
    close_connection(conn,cur)


    if is_registeredd:
        bot.send_message(message.chat.id,"You are already registered")
        
    else:
        bot.send_message(message.chat.id,"Hello new User!")
        return user_register(message)
   




