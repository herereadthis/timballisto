"""Get started with guis."""

# https://www.raspberrypi.org/learning/getting-started-with-guis/worksheet/

# module that helps to create GUIs
from guizero import App, Text, TextBox, PushButton, Slider, Picture


img_url = '../resources/images/raspberry_pi_128x128.gif'


def say_my_name():
    """Refer to the Text widget welcome_message and sets its value."""
    # to what was typed into the TextBox widget my_name.
    welcome_message.set(my_name.get())


def change_text_size(slider_value):
    """Adjust the size of the text."""
    welcome_message.font_size(slider_value)


if __name__ == '__main__':
    # the GUI app begins here.
    app = App("Hello world")

    # text widget
    welcome_message = Text(
        app,
        text="Welcome to my app",
        size=40,
        font="Times New Roman",
        color="lightblue"
    )

    my_name = TextBox(app)

    # Argument 1: tells PushButton that app is its boss
    # Argument 2: command tells the button which function to call when pressed
    # Argument 3: text to be displayed
    update_text = PushButton(app, command=say_my_name, text='Display my name')

    text_size = Slider(app, command=change_text_size, start=10, end=80)

    my_image = Picture(app, image=img_url)

    # All code that creates a widget must be added before the event loop.
    # The following starts the event loop.
    app.display()
