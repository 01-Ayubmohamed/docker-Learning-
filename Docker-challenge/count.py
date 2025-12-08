import os
from flask import Flask
import redis

# Initialize Flask app, 
app = Flask(__name__)
# 

redis_host = os.getenv('REDIS_HOST', 'redis')
#

redis_port = int(os.getenv('REDIS_PORT', 6379))

# Initialize Redis client
r= redis.Redis(host=redis_host, port=redis_port,)

#Route 1: Home page
@app.route("/")
def home():
    return "Hello World! Welcome to Docker Challenge."

#Route 2: Counter page
@app.route("/count")
def count():
    # Get the current counter value from Redis
    current = r.get("count")

    # If this key does not exist yet, start at 0
    if current is None:
        current = 0
    else:
        current = int(current)
    # Increment the counter
    current += 1

    # Save the new value back to Redis
    r.set("count", current)

    return f"Hello, I have been seen {current} times."

    # Run the Flask app, accessible from any IP address on port 5002.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)