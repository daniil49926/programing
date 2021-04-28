import PySimpleGUI as Psg
import connect_data
import subprocess


def main():
    Psg.theme("DarkGrey1")
    main_layout = [[Psg.Text(size=(1, 1))],
                   [Psg.Text(size=(1, 1)), Psg.Button("Редактор", key="editor_", size=(20, 3)), Psg.Text(size=(1, 1))],
                   [Psg.Text(size=(1, 1)), Psg.Button("Заказы", key="order_", size=(20, 3)), Psg.Text(size=(1, 1))],
                   [Psg.Text(size=(1, 1))]]
    main_window = Psg.Window("Menu", main_layout, button_color="#00A949")

    while True:
        event, values = main_window.read()
        if event == Psg.WINDOW_CLOSED:
            main_window.close()
            break
        if event == "editor_":
            main_window.close()
            editor_()
            break
        if event == "order_":
            main_window.close()
            order_()
            break


def editor_():
    if admin():
        Psg.theme("DarkGrey1")
        layout = [[Psg.Text("Редактор базы данных", size=(50, 2), font="Helvitica 22 italic")],

                  [Psg.Text("Добавить позицию", size=(20, 1),
                            font="Helvitica", text_color="yellow")],

                  [Psg.Text(size=(10, 1)),
                   Psg.Text("Название", size=(18, 1)),
                   Psg.Text("Категория", size=(17, 1)),
                   Psg.Text("Количество", size=(9, 1)),
                   Psg.Text("Цена за шт", size=(10, 1))],

                  [Psg.Text(size=(10, 1)),
                   Psg.Input(key="name_add", size=(20, 1)),
                   Psg.Input(key="category_add", size=(20, 1)),
                   Psg.Input(key="num_add", size=(10, 1)),
                   Psg.Input(key="price_add", size=(10, 1)),
                   Psg.Button("Описание", button_color="grey", key="description_add", size=(10, 1)),
                   Psg.Button("Добавить", key="but_add", size=(10, 1))],

                  [Psg.Text(size=(0, 1))],
                  [Psg.Text("Изменить значения по названию и категории", size=(40, 1),
                            font="Helvitica", text_color="yellow")],

                  [Psg.Text(size=(10, 1)),
                   Psg.Text("Название", size=(18, 1)),
                   Psg.Text("Категория", size=(17, 1)),
                   Psg.Text("Количество", size=(9, 1)),
                   Psg.Text("Цена за шт", size=(10, 1))],

                  [Psg.Text(size=(10, 1)),
                   Psg.Input(key="name_edit", size=(20, 1)),
                   Psg.Input(key="category_edit", size=(20, 1)),
                   Psg.Input(key="num_edit", size=(10, 1)),
                   Psg.Input(key="price_edit", size=(10, 1)),
                   Psg.Button("Описание", button_color="grey", key="description_edit", size=(10, 1)),
                   Psg.Button("Редактировать", key="but_edit", size=(10, 1))],

                  [Psg.Text(size=(0, 1))],
                  [Psg.Text("Удалить позицию по названию и категории", size=(40, 1),
                            font="Helvitica", text_color="yellow")],

                  [Psg.Text(size=(10, 1)),
                   Psg.Text("Название", size=(18, 1)),
                   Psg.Text("Категория", size=(17, 1))],

                  [Psg.Text(size=(10, 1)),
                   Psg.Input(key="name_rem", size=(20, 1)),
                   Psg.Input(key="category_rem", size=(20, 1)),
                   Psg.Button("Удалить", key="but_rem", size=(10, 1))],

                  [Psg.Text(size=(0, 2))],

                  [Psg.Button("Просмотреть базу данных",
                              key="view_data", size=(20, 2)),
                   Psg.Text(size=(60, 2), key='-OUTPUT-', font="Arial")]]
        window = Psg.Window('Data editor',
                            layout,
                            button_color="#00A949")

        des_add = ""
        des_edit = ""
        while True:
            try:
                event, values = window.read()
                if event == Psg.WINDOW_CLOSED:
                    break
                if event == "but_add":
                    category_add = str(values["category_add"])
                    name_add = str(values["name_add"])
                    num_add = int(values["num_add"])
                    price_add = int(values["price_add"])
                    if name_add and num_add and price_add and category_add and des_add:
                        window['-OUTPUT-'].update(f"Вы добавили позицию {name_add},"
                                                  f" в количестве {num_add},"
                                                  f" по цене {price_add}", text_color="white")
                        window["description_add"].update(button_color="grey")
                        connect_data.add_in_data(category_add, name_add, num_add, price_add, des_add)

                if event == "but_rem":
                    name_rem = str(values["name_rem"])
                    category_rem = str(values["category_rem"])
                    if category_rem and name_rem:
                        if connect_data.select_poz(category_rem, name_rem):
                            window['-OUTPUT-'].update(f"Вы удалили позицию {name_rem}", text_color="white")
                            connect_data.rem_in_data(category_rem, name_rem)
                        else:
                            window['-OUTPUT-'].update(f"Такой позиции нет в базе",
                                                      text_color="white")

                if event == "but_edit":
                    category_edit = str(values["category_edit"])
                    name_edit = str(values["name_edit"])
                    num_edit = int(values["num_edit"])
                    price_edit = int(values["price_edit"])
                    if name_edit and num_edit and price_edit and category_edit:
                        if connect_data.select_poz(category_edit, name_edit):
                            connect_data.edit_poz_in_data(category_edit, name_edit, num_edit, price_edit, des_edit)
                            window['-OUTPUT-'].update(f"Позиция {name_edit} успешно отредоктированна",
                                                      text_color="white")
                            window["description_edit"].update(button_color="grey")
                        else:
                            window['-OUTPUT-'].update(f"Такой позиции нет в базе",
                                                      text_color="white")

                if event == "view_data":
                    view_data_font = ('Courier New', 14)
                    view_data_text = connect_data.select_all()
                    view_data_column = [[Psg.Text(view_data_text, font=view_data_font)]]

                    view_data_layout = [
                        [Psg.Column(view_data_column, size=(900, 500), scrollable=True, key="Column")]
                    ]

                    view_data_window = Psg.Window('view_data', view_data_layout, finalize=True)

                    while True:
                        event, values = view_data_window.read()
                        if event == Psg.WIN_CLOSED:
                            break

                    view_data_window.close()

                if event == "description_add":
                    des_data_layout = [
                        [Psg.Text("Введите описание", size=(18, 2), font="Helvitica 22 italic", text_color="yellow")],
                        [Psg.Text("Вводите каждое ключевое слово\n"
                                  "или ключевые словосочетания для данной позиции через ';'", size=(50, 2))],
                        [Psg.Multiline(size=(50, 8), key="-DES_ADD-")],
                        [Psg.Button("Сохранить", key="des_add", size=(10, 1))]
                    ]

                    des_data_window = Psg.Window('description', des_data_layout, size=(500, 300))

                    while True:
                        event, values = des_data_window.read()
                        if event == Psg.WIN_CLOSED:
                            break
                        if event == "des_add":
                            des_add = str(values["-DES_ADD-"])
                            window["description_add"].update(button_color="green")

                    des_data_window.close()

                if event == "description_edit":
                    des2_data_layout = [
                        [Psg.Text("Введите описание", size=(18, 1), font="Helvitica 22 italic", text_color="yellow")],
                        [Psg.Text("Если вам не нужно менять описание этого товара\n"
                                  "ничего не вводите в этом окне", text_color="red")],
                        [Psg.Text("Вводите каждое ключевое слово\n"
                                  "или ключевые словосочетания для данной позиции через ';'", size=(50, 2))],
                        [Psg.Multiline(size=(50, 8), key="-DES_EDIT-")],
                        [Psg.Button("Сохранить", key="des_edit", size=(10, 1))]
                    ]

                    des2_data_window = Psg.Window('description', des2_data_layout, size=(500, 300))

                    while True:
                        event, values = des2_data_window.read()
                        if event == Psg.WIN_CLOSED:
                            break
                        if event == "des_edit":
                            des_edit = str(values["-DES_EDIT-"])
                            window["description_edit"].update(button_color="green")

                    des2_data_window.close()

            except ValueError:
                window['-OUTPUT-'].update(f"Ошибка ввода", text_color="red")


def admin():
    Psg.theme("DarkGrey1")
    layout = [[Psg.Text("Чтобы вносить изменения в базу данных авторизуйтесь", font="Arial")],
              [Psg.Text("Логин", size=(18, 1)), Psg.Text("Пароль", size=(20, 1))],
              [Psg.Input(key="login", size=(20, 1)), Psg.Input(key="password", size=(20, 1))],
              [Psg.Button("Войти", size=(5, 1))],
              [Psg.Text(key="error_log", size=(50, 1))]]
    window = Psg.Window("logon",
                        layout,
                        button_color="#00A949")

    i = 5
    while True:
        event, values = window.read()
        if event == Psg.WINDOW_CLOSED or i == 0:
            window.close()
            return False
        if values["login"] == "admin" and values["password"] == "admin":
            window.close()
            return True
        window["error_log"].update(f"Неверный логин или пароль."
                                   f"Осталось попыток {i}")
        i -= 1


def order_():
    order_list = []
    order_text = ""
    for i in str(subprocess.getoutput("../c-script/course/course/Source.cpp")).split("\n"):
        order_text += (i + ".")
        order_list.append([Psg.Text(u"{}\n".format(i)),
                           Psg.Button("Готово", key=u"add{}\n".format(i), size=(10, 1)),
                           Psg.Button("Отмена", key=u"cancel{}\n".format(i), size=(10, 1))])
    order_list.append([Psg.Button("Обновить", key="update", size=(20, 1))])
    order_layout = order_list
    order_window = Psg.Window("order", order_layout, button_color="grey")

    while True:

        event, values = order_window.read()
        if event == "update":
            order_window.close()
            order_()
        if event == Psg.WINDOW_CLOSED:
            order_window.close()
            break
        order_text = order_text.split(".")
        for i in order_text:
            if event == "add{}\n".format(i):
                list_poz = i.split(" | ")
                connect_data.delete_in_order(list_poz[0], list_poz[1], list_poz[4])
                order_window.close()
                order_()
        for i in order_text:
            if event == "cancel{}\n".format(i):
                list_poz = i.split(" | ")
                connect_data.cancel_order(list_poz[0], list_poz[1])
                connect_data.delete_in_order(list_poz[0], list_poz[1], list_poz[4])
                order_window.close()
                order_()


if __name__ == '__main__':
    main()
