# Импортируем необходимые библиотеки
from pynput import keyboard
import paho.mqtt.client as mqtt 
import ctypes

# Функция для отправки сообщений по MQTT
def mqtt_send_msg(topic, msg):
    # Создаем клиента с именем P1
    client = mqtt.Client("P1")
    # Данные для аутентификации
    client.username_pw_set("логин", "пароль")
    # Подключаемся к брокеру по IP-адресу
    client.connect("192.168.1.5")
    # Опубликовываем сообщение в заданную тему
    client.publish(topic, msg)
    # Отключаемся от брокера
    client.disconnect()

# Функция для выхода из программы
def quit_this():
    # Показываем диалоговое окно с вопросом
    tmp = ctypes.windll.user32.MessageBoxW(0, "Вы хотите выключить hotkey_mqtt?", "Информация", 4)
    # Если пользователь нажал "Да", то выходим из программы
    if tmp == 6:
        quit()

# Создаем словарь горячих клавиш и соответствующих им функций
hotkeys = {
    # контрл + альт + вин + минус
    '<ctrl>+<alt>+<cmd>+-': lambda: mqtt_send_msg('powerpc/keyboard', 'small_light'),
    # контрл + альт + вин + плюс
    '<ctrl>+<alt>+<cmd>++': lambda: mqtt_send_msg('powerpc/keyboard', 'big_light'),
    # контрл + альт + вин + слеш
    '<ctrl>+<alt>+<cmd>+/': quit_this
}

# Регистрируем горячие клавиши и запускаем цикл обработки событий
with keyboard.GlobalHotKeys(hotkeys) as h: 
    h.join()
