from flask import Flask
from redis import Redis
import time

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return f'This website has been viewed {redis.get("hits")} times'

@app.route("/reset")
def reset():
    redis.set("hits", 0)
    return f"The hits have been reset"

@app.route("/save")
def save():
    id = int(time.time())
    hits = redis.get("hits")
    redis.hset("times", id, hits)
    return f"Saved {id} = {hits}"

@app.route("/report")
def report():
    res = "Hit's were recorded at:\n"
    for id, hits in redis.hgetall("times").items():
        res += f"{id}\t:\t{hits}\n"
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
