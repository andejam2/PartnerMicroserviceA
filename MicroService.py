from flask import Flask, request, jsonify

app = Flask(__name__)

# Step 1: Hardcoded packing list dictionary
packing_templates = {
    "beach": [
        "Swimsuit", "Sunscreen", "Sunglasses", "Flip flops", "Beach towel", "Hat", "Water bottle"
    ],
    "business": [
        "Business attire", "Laptop", "Charger", "Notebook", "Pens", "Toiletries", "Dress shoes"
    ],
    "city": [
        "Comfortable walking shoes", "Guidebook", "Map", "Umbrella", "Daypack", "Phone charger", "Reusable water bottle"
    ],
    "camping": [
        "Tent", "Sleeping bag", "Flashlight", "Bug spray", "Portable stove", "Map", "First aid kit"
    ]
}

# Step 2: Create POST endpoint
@app.route("/getPackingList", methods=["POST"])
def get_packing_list():
    data = request.get_json()

    # Step 3: Check if 'trip_type' is provided
    trip_type = data.get("trip_type", "").lower()

    # Step 4: Validate and respond
    if trip_type in packing_templates:
        return jsonify({
            "status": "success",
            "trip_type": trip_type,
            "packing_list": packing_templates[trip_type]
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid trip type. Must be one of: beach, business, city, camping."
        }), 400

# Step 5: Run the app locally
if __name__ == "__main__":
    app.run(debug=True)
