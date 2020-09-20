import PySimpleGUI as Gui
from cyborg.modules.locker import Locker


class LockerGui:

    WIDTH = 100
    HEIGHT = 200
    EXTRA = 40
    SPARE = 10

    def __init__(self):
        Gui.theme('Default')  # Add a touch of color
        Gui.change_look_and_feel('DefaultNoMoreNagging')
        canvas = Gui.Canvas(
            background_color='white',
            size=(self.WIDTH * 2 + self.SPARE * 2, self.HEIGHT + self.SPARE * 2 + self.EXTRA),
            key='locker',
            visible=True,
            border_width=4)
        label = Gui.Text('No session' + ' ' * 50, background_color='red', font=('default', 14))
        button = Gui.Button('Open', key='locker_toggle')
        layout = [[Gui.Text('Welcome to Cyb-org!', font=('default', 25))],
                  [Gui.Text('Here is a test locker for trials.', font=('default', 18))],
                  [Gui.Text('In order to open the locker, you must start a locker session first.',
                            font=('default', 18))],
                  [Gui.Text('')],
                  [Gui.Text('Enter client name'), Gui.InputText(default_text='John Doe'),
                   Gui.Button('Start  Session', key='start_session')],
                  [label],
                  [canvas],
                  [button]]

        # Create the Window
        window = Gui.Window('Test Locker', layout)
        window.finalize()

        def on_session_start():
            self.start_session()

        def on_session_end():
            self.end_session()

        def on_locker_open():
            self.open_locker()

        def on_locker_close():
            self.close_locker()

        self.locker = Locker(on_session_start, on_session_end, on_locker_open, on_locker_close)
        self.window = window
        self.canvas = canvas
        self.label = label
        self.button = button
        self.__draw_locker(canvas, True)

    def run(self):
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = self.window.read()
            if event == Gui.WIN_CLOSED:  # if user closes window
                break
            if event == 'start_session':
                self.locker.start_session(values[0])
            if event == 'locker_toggle':
                if self.closed:
                    self.locker.open_locker()
                else:
                    self.locker.close_locker()

    @property
    def closed(self):
        return self.locker.closed

    @property
    def session(self):
        return self.locker.session


    def start_session(self):
        self.label.update(value=self.session, background_color='green')


    def end_session(self):
        self.label.update(value='No session', background_color='red')

    def open_locker(self):
        self.button.update(text='Close')
        self.__draw_locker(self.canvas, self.closed)

    def close_locker(self):
        self.button.update(text='Open')
        self.__draw_locker(self.canvas, self.closed)

    def close_window(self):
        self.window.close()

    def __str__(self):
        session = f'{self.label.get()} - ' if self.session else ''
        state = 'closed' if self.closed else 'opened'
        return f'{session}Locker {state}'

    @classmethod
    def __draw_locker(cls, canvas, closed):
        w = cls.WIDTH
        h = cls.HEIGHT
        e = cls.EXTRA
        s = cls.SPARE
        canvas.tk_canvas.delete("all")
        if closed:
            # Closed frame
            canvas.tk_canvas.create_line(s, s * 2, s + w, s * 2, width=5)
            canvas.tk_canvas.create_line(s + w, s * 2, s + w, s * 2 + h, width=5)
            canvas.tk_canvas.create_line(s + w, s * 2 + h, s, s * 2 + h, width=5)
            canvas.tk_canvas.create_line(s, s * 2 + h, s, s * 2, width=5)
            # Handle
            canvas.tk_canvas.create_line(s * 2, s * 2 + h / 2 - 8, s * 2, s * 2 + h / 2 + 8, width=3)
            # Extra
            canvas.tk_canvas.create_line(s, s * 2 + h, s + w, s * 2 + h, width=5)
            canvas.tk_canvas.create_line(s + w, s * 2 + h, s + w, s * 2 + h + e, width=5)
            canvas.tk_canvas.create_line(s + w, s * 2 + h + e, s, s * 2 + h + e,  width=5)
            canvas.tk_canvas.create_line(s, s * 2 + h + e, s, s * 2 + h, width=5)
            # Shelves
            canvas.tk_canvas.create_line(s * 2, s * 2 + h * 0.2, w, s * 2 + h * 0.2)
            canvas.tk_canvas.create_line(s * 2, s * 2 + h * 0.4, w, s * 2 + h * 0.4)
            canvas.tk_canvas.create_line(s * 2, s * 2 + h * 0.6, w, s * 2 + h * 0.6)
            canvas.tk_canvas.create_line(s * 2, s * 2 + h * 0.8, w, s * 2 + h * 0.8)
        else:
            # Closed frame
            canvas.tk_canvas.create_line(s, s * 2, s + w, s * 2, width=2)
            canvas.tk_canvas.create_line(s + w, s * 2, s + w, s * 2 + h, width=2)
            canvas.tk_canvas.create_line(s + w, s * 2 + h, s, s * 2 + h, width=2)
            canvas.tk_canvas.create_line(s, s * 2 + h, s, s * 2, width=2)
            # Extra
            canvas.tk_canvas.create_line(s, s * 2 + h, s + w, s * 2 + h, width=5)
            canvas.tk_canvas.create_line(s + w, s * 2 + h, s + w, s * 2 + h + e, width=5)
            canvas.tk_canvas.create_line(s + w, s * 2 + h + e, s, s * 2 + h + e, width=5)
            canvas.tk_canvas.create_line(s, s * 2 + h + e, s, s * 2 + h, width=5)
            # Open frame
            canvas.tk_canvas.create_line(s + w, s * 2, w * 2, s, width=5)
            canvas.tk_canvas.create_line(w * 2, s, w * 2, s * 3 + h, width=5)
            canvas.tk_canvas.create_line(w * 2, s * 3 + h, s + w, s * 2 + h, width=5)
            canvas.tk_canvas.create_line(s + w, s * 2 + h, s + w, s * 2, width=5)
            # Handle
            canvas.tk_canvas.create_line(w * 2 - s, s * 2 + h / 2 - 9, w * 2 - s, s * 2 + h / 2 + 9, width=3)
            # Shelves
            canvas.tk_canvas.create_line(s * 2, s * 2 + h * 0.2, w, s * 2 + h * 0.2)
            canvas.tk_canvas.create_line(s * 2, s * 2 + h * 0.4, w, s * 2 + h * 0.4)
            canvas.tk_canvas.create_line(s * 2, s * 2 + h * 0.6, w, s * 2 + h * 0.6)
            canvas.tk_canvas.create_line(s * 2, s * 2 + h * 0.8, w, s * 2 + h * 0.8)
