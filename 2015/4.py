from aoc import get_input
import hashlib

secret_key = 'yzbqklnj'
i = 0
while True:
    secret_key_check = secret_key + str(i)
    m = hashlib.md5(secret_key_check.encode('utf-8')).hexdigest()
    if m.startswith('000000'):
        print(i)
        break
    i += 1
