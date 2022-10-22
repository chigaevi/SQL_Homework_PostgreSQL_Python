import psycopg2

with psycopg2.connect(database="clients_db", user='postgres', password="treeWQ1846VjJ") as conn:
    with conn.cursor() as cur:

        def drop_table():
            cur.execute("""
            DROP TABLE phone_numbers;
            DROP TABLE clients;
            """)

        def create_table():
            cur.execute("""
            create table if not exists clients(
                id_client SERIAL PRIMARY KEY,
                client_name VARCHAR(40) UNIQUE,
                client_email VARCHAR(60) UNIQUE
                );
            """)
            cur.execute("""
                create table if not exists phone_numbers(
                id_num SERIAL PRIMARY KEY,
                number VARCHAR(11) NOT NULL,
                id_client SERIAL REFERENCES clients(id_client) 
                );
            """)
            conn.commit()

        def create_client(name, email): # Функция, позволяющая добавить нового клиента
            cur.execute("""
            insert into clients(client_name, client_email) values (%s,%s)
            """, (name,email))

        def add_number(id_client, number): # Функция, позволяющая добавить телефон для существующего клиента
            cur.execute("""
            insert into phone_numbers(id_client, number) values (%s,%s)
            """, (id_client, number))

        def change_data(id, name = None, email = None): # Функция, позволяющая изменить данные о клиенте
            cur.execute("""
            SELECT id_client FROM clients;
            """)
            ids = cur.fetchall()
            ids_list = []
            for c in ids:
                ids_list += list(c)
            if id in ids_list and name is not None:
                cur.execute("""
                UPDATE clients SET client_name = %s WHERE id_client = %s
                """, (name, id))
                print('Имя изменено')
            if id in ids_list and email is not None:
                cur.execute("""
                UPDATE clients SET client_email = %s WHERE id_client = %s
                """, (email, id))
                print('email изменен')
            else: print('Клиент с таким id не найден')

        def del_number(): #Функция, позволяющая удалить телефон для существующего клиента




        # drop_table()
        # create_client('Rita', 'email3@email.com')
        # add_number('1','8952684528')
        # change_data(3,'Piter','email_piter@mail.com')

