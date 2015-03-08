# tail a file (like tail -f)
import time

def tail(f):
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

f = open('LICENSE')
tail(f)