from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Button array
classes_keyboard = [["Bardo", "Chierico", "Druido", "Mago"],
           ["Paladino", "Ranger", "Stregone", "Warlock"]]

levels_keyboard = [["Lv. 0", "Lv. 1", "Lv. 2", "Lv. 3", "Lv. 4"],
          ["Lv. 5", "Lv. 6", "Lv. 7", "Lv. 8", "Lv. 9"]]

menu_keyboard = [["Nome", "Livello"], ["Classe e livello"], ["Recenti", "Statistiche"]]


# Create a keyboard from the array passed as parameter
def create_base_keyboard(keyboard, callback_string=""):
    res = []
    col = []
    for row in keyboard:
        for column in row:
            col.append(InlineKeyboardButton(str(column), callback_data=callback_string + "," + str(column)))
        res.append(col)
        col = []
    return res


def get_classes_keyboard():
    keyboard = create_base_keyboard(classes_keyboard, "class")
    return InlineKeyboardMarkup(keyboard)


def get_menu_keyboard():
    keyboard = create_base_keyboard(menu_keyboard, "menu")
    return InlineKeyboardMarkup(keyboard)


# Directly created InlineKeyboardButton instances, customized for levels
def get_levels_keyboard():
    keyboard = []
    col = []
    for row in levels_keyboard:
        for column in row:
            col.append(InlineKeyboardButton(str(column), callback_data="level," + str(column)[4:5]))
        keyboard.append(col)
        col = []
    return InlineKeyboardMarkup(keyboard)


# Directly created InlineKeyboardButton instances, composed by [decorated spell name,(callbackstring,spell name]
# Notice that the spell name in the callback is not the same displayed in the button
def get_spells_keyboard(list, mode):
    spells = []
    for tupla in list:
        name = tupla['Nome']
        if mode == "class":
            classe = tupla['Classe']
            str_button = name + "[" + classe + "]"
            button = InlineKeyboardButton(str_button, callback_data="name," + name)
        elif mode == "level":
            livello = tupla['Livello']
            str_button = "Lv" + str(livello) + "-" + name
            button = InlineKeyboardButton(str_button, callback_data="name," + name)
        elif mode == "classlevel":
            classe = tupla['Classe']
            livello = tupla['Livello']
            str_button = "Lv" + str(livello) + "-" + name + "[" + classe + "]"
            button = InlineKeyboardButton(str_button, callback_data="name," + name)
        elif mode == "name":
            button = InlineKeyboardButton(name, callback_data="name," + name)
        spells.append([button])
        if spells.__len__() > 70:
            break
    return InlineKeyboardMarkup(spells)
