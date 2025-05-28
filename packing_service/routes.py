from flask import Blueprint, request, jsonify
from services.loader import load_packing_templates

packing_routes = Blueprint("packing_routes", __name__)
packing_templates = load_packing_templates()

@packing_routes.route("/getPackingList", methods=["POST"])
def get_packing_list():
    data = request.get_json()

    if not data or "trip_type" not in data:
        return jsonify({
            "status": "error",
            "message": "'trip_type' is required in the request body."
        }), 400

    trip_type = data["trip_type"].lower()

    if trip_type in packing_templates:
        return jsonify({
            "status": "success",
            "trip_type": trip_type,
            "packing_list": packing_templates[trip_type]
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid trip type. Please check available trip types."
        }), 400
