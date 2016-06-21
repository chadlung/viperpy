
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

        {
          'license_feature': [{
            'expired_ind': False,
            'issued_date': '06/21/2016',
            'license_id_indicator': 'U',
            'licensed_ind': True,
            'model': 'ViPR_Controller',
            'notice': 'ACTIVATED TO License Site Number: 391561492',
            'product': 'SDSD23S45ZY',
            'serial': 'SDSD23S45ZY',
            'site_id': 'UNKNOWN',
            'storage_capacity': '12457845',
            'trial_license_ind': False,
            'version': '1.0'}
          ], 'license_text': '#######...'
        }
        """
        return self.conn.get('license')

    def post_license(self, params):
        """"
        Upload a new license
        """
        return self.conn.post('license', params)
