# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Projects():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_projects_bulk(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the projects bulk payload

        :return: A list of Project IDs
        """
        json_data = self.conn.get('projects/bulk')
        return json_data['id']

    def get_projects_bulk_by_id(self, project_ids):
        """
        Retrieve detailed information about a set of volumes

        :param volume_ids: A list of volume IDs
        :return: A list of projects
        """
        json_data = self.conn.post(url='projects/bulk',
                                   json_payload={"id": project_ids})
        return json_data['project']

    def get_project(self, project_id):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the project's information

        :return: The project's information
        """
        return self.conn.get('projects/{0}'.format(project_id))
