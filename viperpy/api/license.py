
class License():
    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_license(self):
        """
        Retrive licensing information by performing a GET call

        Example JSON result from the API:

        {"user": "root"}
        """
        return self.conn.get('license')

    def post_license(self, params):
        """"
        Upload a new license
        """
        return self.conn.post('license', params)
