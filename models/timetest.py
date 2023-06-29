""" Testing time response rate of function cases """
import time
def TestDisplayTime(func):
    def complexity(self):
        TimeStart = time.time()
        func(self)
        print(f"{func.__name__}() execution time: {time.time() - TimeStart}") 
        print(f"{func.__name__}() process time: {time.process_time()}") 
    return complexity