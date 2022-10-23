import psycopg2

with psycopg2.connect(database="clients_db", user='postgres', password="treeWQ1846VjJ") as conn:
    with conn.cursor() as cur:

        def drop_table():
            cur.execute("""
            DROP TABLE phone_numbers;
            DROP TABLE clients;
            """)

        def create_table(cursor):
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients(
            id_client SERIAL PRIMARY KEY,
            client_name VARCHAR(40) UNIQUE,
            client_email VARCHAR(60) UNIQUE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS phone_numbers(
            id_num SERIAL PRIMARY KEY,
            number VARCHAR(11) NOT NULL,
            id_client SERIAL REFERENCES clients(id_client) 
            );
            """)
            conn.commit()
        def create_client(name, email): # Функция, позволяющая добавить нового клиента
            cur.execute("""
            INSERT INTO clients(client_name, client_email) values (%s,%s)
            """, (name,email))
        def add_number(id_client, number): # Функция, позволяющая добавить телефон для существующего клиента
            cur.execute("""
            INSERT INTO phone_numbers(id_client, number) values (%s,%s)
            """, (id_client, number))
            print('номер ', number, ' для клиента ', id_client, ' добавлен')
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
            else:
                print('Клиент с таким id не найден')
        def del_number(id_client, id_num = None, number = None): #Функция, позволяющая удалить телефон для существующего клиента
            cur.execute("""
                        SELECT id_client FROM clients;
                        """)
            ids = cur.fetchall()
            ids_list = []
            for id in ids:
                ids_list += list(id)
            if id_client in ids_list and id_num is not None:
                cur.execute("""
                            DELETE FROM phone_numbers WHERE id_num = %s
                            """, (id_num,))
                print('номер с id ',id_num,' для клиента ',id_client,' удален (если он существовал :) )')
            elif id_client in ids_list and number is not None:
                cur.execute("""
                            DELETE FROM phone_numbers WHERE number = %s
                            """, (number,))
                print('номер ',number,' для клиента ',id_client,' удален (если он существовал :) )')
            else:
                print('Клиент с такими данными не найден ')


        def del_client(id_client = None, name = None): # Функция, позволяющая удалить существующего клиента
            cur.execute("""
                       DELETE FROM phone_numbers WHERE id_client = %s
                       """, (id_client,))
            cur.execute("""
                       DELETE FROM clients WHERE id_client = %s
                       """, (id_client,))
            cur.execute("""
                       DELETE FROM clients WHERE client_name = %s
                       """, (name,))




        # Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)


        # drop_table()
        # create_table(cur)
        # create_client('Adam', 'bog1313@email.com')
        # add_number('4','89996845328')
        # change_data(3,'Piter','email_piter@mail.com')
        # del_number(3,id_num='7')
        # del_number(4, number='89996845328')
        del_client(id_client=1)
