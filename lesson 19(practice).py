import datetime

def timer(func):

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func()
        end = datetime.now()
        print(f'Time taken :{(end - start).second}seconds.')
        return result