import multiprocessing
from decouple import config

HOST = config('HOST')
PORT = config('PORT')

bind = f"{HOST}:{PORT}"
workers = multiprocessing.cpu_count() * 2 + 1