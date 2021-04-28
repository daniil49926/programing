import mysql.connector
import config_data


def select_all():
    db = mysql.connector.connect(user=config_data.log, password=config_data.password,
                                 host=config_data.host, database='####')
    cur = db.cursor()
    rez = ""
    cur.execute("SELECT * FROM my_shop")
    rows = cur.fetchall()
    for i in range(len(rows)):
        rez += ("Элемент №{}\n\tКатегория: {}\n\tНазвание: {}\n\tКол-во: {}\n\tСтоимость: {}\n".format(
            i + 1,
            rows[i][0],
            rows[i][1],
            rows[i][2],
            rows[i][3]
        ))
    db.commit()
    cur.close()
    db.close()
    return rez


def add_in_data(category, name, num, price, des):
    insert_reviewers_query = """
    INSERT INTO my_shop
    VALUES ( %s, %s, %s, %s, %s )
    """
    reviewers_records = [(category, name, num, price, des)]
    db = mysql.connector.connect(user=config_data.log, password=config_data.password,
                                 host=config_data.host, database='####')
    cur = db.cursor()
    cur.executemany(insert_reviewers_query,
                    reviewers_records)
    db.commit()
    cur.close()
    db.close()


def rem_in_data(category, name):
    delete_reviewers_query = f"""
        DELETE FROM my_shop WHERE category = "{category}" AND name_item = "{name}"
        """

    db = mysql.connector.connect(user=config_data.log, password=config_data.password,
                                 host=config_data.host, database='####')
    cur = db.cursor()
    cur.execute(delete_reviewers_query)
    db.commit()
    cur.close()
    db.close()


def edit_poz_in_data(category, name, num, price, des):
    if des == "":
        edit_reviewers_query = f"""
            UPDATE my_shop SET nums_item = "{num}", price_item = "{price}" 
            WHERE category = "{category}" AND name_item = "{name}" 
            """
    else:
        edit_reviewers_query = f"""
                    UPDATE my_shop SET nums_item = "{num}", price_item = "{price}", description_of_goods = "{des}" 
                    WHERE category = "{category}" AND name_item = "{name}" 
                    """
    db = mysql.connector.connect(user=config_data.log, password=config_data.password,
                                 host=config_data.host, database='####')
    cur = db.cursor()
    cur.execute(edit_reviewers_query)
    db.commit()
    cur.close()
    db.close()


def select_poz(category, name):
    edit_reviewers_query = f"""
            SELECT * FROM my_shop WHERE category = "{category}" AND name_item = "{name}"
            """
    db = mysql.connector.connect(user=config_data.log, password=config_data.password,
                                 host=config_data.host, database='####')
    cur = db.cursor()
    cur.execute(edit_reviewers_query)
    check_row = cur.fetchall()
    db.commit()
    cur.close()
    db.close()
    if check_row:
        return True
    else:
        return False


def delete_in_order(category, name, number):
    delete_reviewers_query = f"""
            DELETE FROM order_in_shop WHERE category = "{category}" 
            AND name_item = "{name}" AND number_phone = "{number}"
            """

    db = mysql.connector.connect(user=config_data.log, password=config_data.password,
                                 host=config_data.host, database='####')
    cur = db.cursor()
    cur.execute(delete_reviewers_query)
    db.commit()
    cur.close()
    db.close()


def cancel_order(category, name):
    edit_reviewers_query = f"""
                UPDATE my_shop SET nums_item = nums_item + 1 
                WHERE category = "{category}" AND name_item = "{name}" 
                """

    db = mysql.connector.connect(user=config_data.log, password=config_data.password,
                                 host=config_data.host, database='####')
    cur = db.cursor()
    cur.execute(edit_reviewers_query)
    db.commit()
    cur.close()
    db.close()
