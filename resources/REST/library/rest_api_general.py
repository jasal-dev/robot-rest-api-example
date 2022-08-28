"""
REST API keywords for Robot Framework

"""
from json import JSONDecodeError
import requests
from rest_api_data_class import RestDataClass
from robot.api import logger
from robot.api.deco import not_keyword


class RestApiGeneral(RestDataClass):
    """
    A Class to extend RobotFramework keywords to support REST API functionalities.

    """

    @not_keyword
    def return_headers(self, headers):
        """
            Description: helper function for generic_request function.
        """
        if headers is None:
            headers = self.headers
        return headers

    @not_keyword
    def request_handler(self, expected_status_code, **kwargs):
        """
            Description: Generic request handler.
        """
        try:
            log_header: str = kwargs.get('log_header', '')
            kwargs.pop('log_header')
            method: str = kwargs.get('method', 'GET')
            url: str = kwargs.get('url', None)
            headers = kwargs.get('headers', None)
            cookies: dict = kwargs.get('cookies', None)
            json = kwargs.get('json', '')
            timeout = kwargs.get('timeout', 30)
            logger.info(f'req handler: {kwargs}')
            removable_kwargs = ['method', 'url', 'headers', 'cookies', 'json',
                                'timeout']
            keys = kwargs.keys()
            for removable in removable_kwargs:
                if removable in keys:
                    kwargs.pop(removable)
            headers = self.return_headers(headers)
            logger.info(
                f'{method} - {log_header}: '
                f'{url}'
                f' headers: {headers}'
                f' cookies: {cookies}'
                f' json: {json}'
                f' expected_status_code: {expected_status_code}'
                f' kwargs: {kwargs}'
            )
            response = self.session.request(
                method=method,
                url=url,
                cookies=cookies,
                json=json,
                timeout=timeout,
                headers=headers,
                **kwargs
            )
        except Exception as err:
            logger.info(err)
            raise err
        return response

    @staticmethod
    @not_keyword
    def return_correct_response(response,
                                return_type,
                                expected_status_code):
        """
            Description: helper function for generic_request function.
        """
        if expected_status_code in ('200', '202') and return_type == 'json':
            try:
                ret_val = response.json()
            except JSONDecodeError:
                ret_val = response.text
        else:
            ret_val = response.text
        return ret_val

    @not_keyword
    def generic_request(self, **kwargs):
        """
            Description: Generic Wrapper for Python requests.
        """
        expected_status_code: str = kwargs.get('expected_status_code', '200')
        return_type: str = kwargs.get('return_type', 'json')
        removable_kwargs = ['expected_status_code',
                            'return_type']
        keys = kwargs.keys()
        for removable in removable_kwargs:
            if removable in keys:
                kwargs.pop(removable)
        self.set_session(requests.Session())
        response = self.request_handler(expected_status_code, **kwargs)
        self.log_returned_response(response)
        self.status_code_should_be(response, expected_status_code)
        ret_val = self.return_correct_response(
           response,
           return_type,
           expected_status_code
        )
        return ret_val

    @staticmethod
    @not_keyword
    def status_code_should_be(response, expected_status_code):
        """
            Function: status_code_should_be
            Type: internal
            Description: confirms request was successful
            Parameters:
                response (Response): Response from request
                expected_status_code (str): Expected status code

            Returns:
        """
        request_status = str(response.status_code)
        if request_status != expected_status_code:
            raise RestDataClass.RestAPIError(
                "request returned status code " + request_status)

    @staticmethod
    @not_keyword
    def log_returned_response(response):
        """
            Function: log_returned_response
            Type: internal
            Description: Log status code and textual response
            Parameters:

            Returns:
        """
        logger.info(f'Response: {response.status_code} - {response.text}')
