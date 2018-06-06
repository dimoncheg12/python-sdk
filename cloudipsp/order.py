from __future__ import absolute_import, unicode_literals
from cloudipsp.resources import Resource

import cloudipsp.utils as utils
import cloudipsp.helpers as helper


class Order(Resource):
    def capture(self, data):
        """
        Method for capture order
        :param data: capture order data
        :return: api response
        """
        path = '/capture/order_id/'
        params = {
            'order_id': data.get('order_id', ''),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def reverse(self, data):
        """
        Method for reverse order
        :param data: reverse order data
        :return: api response
        """
        path = '/reverse/order_id/'
        params = {
            'order_id': data.get('order_id', ''),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def status(self, data):
        """
        Method for checking order status
        :param data: order data
        :return: api response
        """
        path = '/status/order_id/'
        params = {
            'order_id': data.get('order_id', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def transaction_list(self, data):
        """
        Method for getting order transaction list
        :param data: order data
        :return: api response
        """
        path = '/transaction_list/'
        params = {
            'order_id': data.get('order_id', '')
        }
        helper.validate_data(params)
        params.update(data)
        self.api.request_type = 'json'  # only json allowed all other methods returns 500 error
        result = self.api.post(path, data=params, headers=self.__headers__)
        return self.response(result)

    def atol_logs(self, data):
        """
        Method for getting order atol logs
        :param data: order data
        :return: api response
        """
        path = '/get_atol_logs/'
        params = {
            'order_id': data.get('order_id', '')
        }
        helper.validate_data(params)
        params.update(data)
        result = self.api.post(path, data=params, headers=self.__headers__)
        return utils.from_json(result).get('response')