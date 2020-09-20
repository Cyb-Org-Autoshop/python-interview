from cyborg.modules.locker import Locker


def get_locker():
    return Locker(None, None, None, None)


def test_start_state():
    locker = get_locker()
    assert locker.closed is True
    assert not locker.session


def test_session_after_session_start():
    locker = get_locker()
    locker.start_session('Some Name')
    assert locker.session == 'Some Name'


def test_locker_open_after_open():
    locker = get_locker()
    locker.start_session('Some Name')
    locker.open_locker()
    assert locker.closed is False


def test_locker_closed_after_close():
    locker = get_locker()
    locker.start_session('Some Name')
    locker.open_locker()
    locker.close_locker()
    assert locker.closed is True


def test_session_ends_automatically_after_close():
    locker = get_locker()
    locker.start_session('Some Name')
    locker.open_locker()
    locker.close_locker()
    assert not locker.session


def test_deny_open_if_no_session():
    locker = get_locker()
    locker.open_locker()
    assert locker.closed is True
