import os
import time
from random import randint

from prefect import flow, task


@task(log_prints=True)
def show_variable(key):
    print(key, "=>", os.getenv(key))
    time.sleep(randint(5, 10))
    print("done")


@flow(log_prints=True)
def show_env_variables():
    for i, key in enumerate(os.environ.keys(), start=1):
        print(i, key)
        show_variable(key)
        print("wait for previous tasks")
