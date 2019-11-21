from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ...resources.repository.region_fee import RegionFee
from ...domain.adapters.shipping_request import ShippingRequestAdapter


class ShippinCost(Resource):
    
    def __init__(self):
        super().__init__()
        self.request_handler = ShippingRequestAdapter(RegionFee())
    
    # @jwt_required
    def post(self):
        content = request.json
        
        cost = self.request_handler.get_service_cost(
            content['zipcode'], content['quantity'])
        
        return jsonify({'cost': cost})
