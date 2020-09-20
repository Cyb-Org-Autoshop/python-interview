class Locker:

    def __init__(self, on_session_start, on_session_end, on_locker_open, on_locker_close):
        self.on_session_start = on_session_start or (lambda: ())
        self.on_session_end = on_session_end or (lambda: ())
        self.on_locker_open = on_locker_open or (lambda: ())
        self.on_locker_close = on_locker_close or (lambda: ())

        self.closed = True
        self.session = ''

    def start_session(self, name):
        if not name:
            self.end_session()
            return
        self.session = name
        self.on_session_start()
        # TODO - if a new session was started, and the locker was not opened within 3 seconds,
        #  the session should be automatically ended.

    def end_session(self):
        self.session = ''
        self.on_session_end()

    def open_locker(self):
        self.closed = False
        self.on_locker_open()

    def close_locker(self):
        self.closed = True
        self.on_locker_close()
