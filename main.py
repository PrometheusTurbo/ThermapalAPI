import database
from flask import Flask, request
import msgpack
from binary import Temperature

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    unparsed = msgpack.unpackb(request.data)
    byte_array = unparsed.get("devices")
    if byte_array:
        byte_array_items = byte_array[0]
        items = ""
        for number in byte_array_items:
            items += f"{number} "
        temp = Temperature(items)
        database.insert(unparsed["mac"], temp.wrapper())
    else:
        print(unparsed)

    return "Hello, world"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
