"""
REST API Data Class to share variables between separate keyword files
"""


class RestDataClass:
    """
    A Class to extend RobotFramework keywords to support REST API functionalities.

    """
    class RestAPIError(Exception):
        """REST API error"""
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return f'{self.message}'

    def __init__(self, hostname, headers, session, **kwargs):
        self.hostname = hostname
        self.headers = headers
        self.session = session
        self.json_header = 'application/json'
        super().__init__(**kwargs)

    def set_hostname(self, hostname):
        """
             Function: set_hostname
             Type: Class internal
             Description: Set hostname
             Parameters:

             Returns:
         """
        self.hostname = hostname

    def set_headers(self, headers):
        """
             Function: set_headers
             Type: Class internal
             Description: Set headers
             Parameters:

             Returns:
         """
        self.headers = headers

    def set_session(self, session):
        """
             Function: set_session
             Type: Class internal
             Description: Set session
             Parameters:

             Returns:
         """
        self.session = session
