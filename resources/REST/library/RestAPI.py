"""
REST API keywords for Robot Framework

"""
from rest_api_genderize import RestApiGenderize
__version__ = "1.0.0"


class RestAPI(RestApiGenderize):
    """
    A Class to extend RobotFramework keywords to support REST API functionalities.

    """

    ROBOT_LIBRARY_SCOPE = "TEST"
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        hostname = None
        headers = None
        session = None
        super().__init__(hostname, headers, session)
