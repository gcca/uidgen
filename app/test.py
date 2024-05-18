import json
import multiprocessing
import urllib.request


def get_uid(_):
    with urllib.request.urlopen("http://localhost:8000/gen") as res:
        body = json.load(res)
        return body["uid"]


if "__main__" == __name__:
    with multiprocessing.Pool(12) as process:
        results = process.map(get_uid, range(6000))

    assert len(results) == 6000
    assert len(results) == len(set(results))
