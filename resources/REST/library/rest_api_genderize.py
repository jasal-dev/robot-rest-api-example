"""
REST API keywords for Robot Framework

"""
from rest_api_general import RestApiGeneral
from robot.api.deco import keyword


class RestApiGenderize(RestApiGeneral):
    """
    A Class to extend RobotFramework keywords to support Genderize's
     REST API functionalities.
    https://genderize.io/

    """

    @keyword("REST Get Genderize Gender")
    def rest_get_genderize_gender(self, name: str, expected_status_code: str):
        """
            Function: rest_get_library_items
            Type: RobotFramework keyword
            Description: Get Gender for a name from Genderize
            Parameters:

                name (str): Name to request the gender for
                expected_status_code (str): Expected response status code

            Returns:

               Gender result JSON

        """
        response = self.generic_request(
           method='GET',
           log_header='get genderize gender',
           url='https://api.genderize.io'
               f'?name={name}',
           expected_status_code=expected_status_code
        )
        return response
