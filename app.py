from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/lookup", methods=["GET"])
def lookup_zip():
    zipcode = request.args.get("zip")

    # Placeholder response (replace with real DB later)
    return jsonify({
        "zip": zipcode,
        "branch": "Tampa Branch",
        "team": "Care Ops Team",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)
