import os
import time
from random import randint

from prefect import flow, task


@task(log_prints=True)
def show_variable(key):
    print(key, "=>", os.getenv(key))
    time.sleep(randint(5, 10))
    print("done")


@flow(name="Subflow")
def run_subflow(key):
    print(key, "=>", os.getenv(key))
    time.sleep(randint(1, 3))


@flow(log_prints=True)
def show_env_variables():
    for i, key in enumerate(os.environ.keys(), start=1):
        print(i, key)
        show_variable(key)
        run_subflow(key)
        print("wait for previous tasks")
