from flask import request, jsonify
from flask_restful import Resource
from ...resources.repository.region_fee import RegionFee
from ...domain.adapters.shipping_request import ShippingRequestAdapter


class ShippingCost(Resource):
    
    def __init__(self):
        super().__init__()
        self.request_handler = ShippingRequestAdapter(RegionFee())
    
    def post(self):
        content = request.json
        
        cost = self.request_handler.get_service_cost(
            content['zipcode'], content['quantity'])
        
        return jsonify({'cost': cost})
