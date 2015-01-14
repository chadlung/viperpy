# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class ViperpyException(Exception):
    """
    This is a custom ViperPy Exception class to better handle
    errors that ViPR can return in HTML format rather than JSON
    """

    def __init__(self, message=None, http_status_code=None, vipr_message=None):
        """
        This is a custom ViperPy Exception class to handle

        :param message: A custom
        :param http_status_code:
        :param vipr_message:
        :return:
        """
        if message is None:
            self.message = 'The ViPR endpoint has thrown an error, check ' \
                           'the http_status_code and vipr_message attributes ' \
                           'of this exception for more details.'
        else:
            self.message = message

        self.http_status_code = http_status_code
        self.vipr_message = vipr_message

        super(ViperpyException, self).__init__(
            message, http_status_code, vipr_message)
