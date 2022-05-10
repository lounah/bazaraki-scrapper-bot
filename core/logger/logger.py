from datetime import datetime


class Logger:
    def __init__(self, output):
        self._output_path = output

    def log(self, msg: str):
        with open(self._output_path, 'a') as output:
            now = datetime.now().strftime('%H:%M:%S')
            output.write(f'{now} {msg}')
