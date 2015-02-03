
class Authentication():
    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def logout(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        log an authenticated user out, thereby invalidating their
        authentication token.

        Example JSON result from the API:

        {"user": "root"}
        """

        logout_resp = self.conn.get('logout')

        # Remove cached authorization token from disk, as the session is
        # now terminated.
        self.conn.remove_cached_token()

        return logout_resp
