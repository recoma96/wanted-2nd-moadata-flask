from threading import Lock


def lock_while_using_file(locker: Lock):
    def __lock_while_using_file(func):
        def __wrapper(*args, **kwargs):
            locker.acquire()
            try:
                output = func(*args, **kwargs)
            except Exception as e:
                locker.release()
                raise e
            else:
                locker.release()
            return output
        return __wrapper
    return __lock_while_using_file