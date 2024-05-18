import os

from fastapi import FastAPI
from fastapi.params import Form


def init():
    import etcd3
    from time import sleep

    while True:
        try:
            etcd = etcd3.client(host="etcd", timeout=5)
            with etcd.lock("uidgen"):
                etcd.status()
            break
        except:
            sleep(2)

    key = "/services/uidgen/datacenter_count"

    with etcd.lock("uidgen"):
        state, resps = etcd.transaction(
            compare=[etcd.transactions.version(key) == 0],
            success=[etcd.transactions.put(key, "0")],
            failure=[etcd.transactions.get(key)],
        )

        count = "0" if state else resps[0][0][0].decode()
        os.environ["UIDGEN_MACHINE_ID"] = str(count)
        etcd.put(key, str(int(count) + 1))


if ("UIDGEN_MACHINE_ID" not in os.environ) or (
    "UIDGEN_DATACENTER_ID" not in os.environ
):
    init()

import uidgen

app = FastAPI()


@app.get("/")
def gen():
    return {"uid": uidgen.GenerateUID()}
