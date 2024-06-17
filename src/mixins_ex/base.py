class LogMixin:
    def log(self, message):
        print(f'[{self.__class__.__name__}] {message}')


class DataService(LogMixin):
    def __init__(self, data):
        self.data = data

    def process_data(self):
        self.log('Processing data...')


data_service = DataService([1, 2, 3, 4, 5])
data_service.process_data()
