from utils import read_file
import hashlib

values = read_file(4, str, False)

secret = values[0]

for i in range(1000000000):
    new_secret = secret + str(i)
    res = hashlib.md5(new_secret.encode()).hexdigest()
    leading_zeros = len(res) - len(res.lstrip('0'))
    if leading_zeros == 5:
        print(f'Part 1: {i}')
        break