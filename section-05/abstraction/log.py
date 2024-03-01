# ABSTRACTION
# Abstraction is the process of hiding the implementation details and showing only the functionality to the user.
from pathlib import Path

PATH_FILE = Path(__file__).parent / 'log.txt'

class Log:

    def _log(self, msg):
        raise NotImplementedError('Subclasses must implement this method')
    
    def log_error(self, msg):
        return self._log(f'[ERROR][{self.__class__.__name__}]: {msg}')

    def log_success(self, msg):
        return self._log(f'[SUCCESS][{self.__class__.__name__}]: {msg}')

class LogFileMixin(Log):

    def _log(self, msg):
        with open(PATH_FILE, 'a') as f:
            f.write(f"{msg}\n")

class LogPrintMixin(Log):

    def _log(self, msg):
        print(f"{msg}")


if __name__ == '__main__':
    f = LogFileMixin()
    f.log_error('Something went wrong')
    f.log_success('Everything is fine')

    p = LogPrintMixin()
    p.log_error('Something went wrong')
    p.log_success('Everything is fine')

    print('-' * 50)