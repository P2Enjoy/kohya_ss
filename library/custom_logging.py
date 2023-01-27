class FakeLogger:
    def __init__(self):
        print(f'LOG INIT')

    def debug(self, message):
        print(f'DEBUG: {message}')

    def info(self, message):
        print(f'INFO: {message}')

    def warning(self, message):
        print(f'WARNING: {message}')

    def error(self, message):
        print(f'ERROR: {message}')

    def critical(self, message):
        print(f'CRITICAL: {message}')


def setup_logging():
    return FakeLogger()
