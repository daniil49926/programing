import mysql.connector
import config_bot

"""
Для базы данных с товаром
"""


def select_all():
    db = mysql.connector.connect(user=config_bot.log, password=config_bot.password,
                                 host=config_bot.host, database='####')
    cur = db.cursor()
    rez = dict()
    cur.execute("SELECT * FROM my_shop")
    rows = cur.fetchall()
    for i in range(len(rows)):
        if rows[i][0] not in rez:
            rez[rows[i][0]] = [[rows[i][1], rows[i][2], rows[i][3], rows[i][4][:-1]]]

        else:
            rez[rows[i][0]].append([rows[i][1], rows[i][2], rows[i][3], rows[i][4][:-1]])

    db.commit()
    cur.close()
    db.close()
    return rez


def edit_poz_in_data(category, name, num, price):
    edit_reviewers_query = f"""
        UPDATE my_shop SET nums_item = "{num}" 
        WHERE category = "{category}" AND name_item = "{name}" 
        """

    db = mysql.connector.connect(user=config_bot.log, password=config_bot.password,
                                 host=config_bot.host, database='####')
    cur = db.cursor()
    cur.execute(edit_reviewers_query)
    db.commit()
    cur.close()
    db.close()


"""
Для базы данных с заказами
"""


def add_in_order_data(category, name, num, price, number):
    insert_reviewers_query = """
    INSERT INTO order_in_shop
    VALUES ( %s, %s, %s, %s, %s )
    """
    reviewers_records = [(category, name, num, price, number)]
    db = mysql.connector.connect(user=config_bot.log, password=config_bot.password,
                                 host=config_bot.host, database='####')
    cur = db.cursor()
    cur.executemany(insert_reviewers_query,
                    reviewers_records)
    db.commit()
    cur.close()
    db.close()
