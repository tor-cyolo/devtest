from api.swagger_api_test.swagger_api_calls_test import SwaggerApiCallsClass
from api.swagger_api_test.swagger_manage_file_test import swaggerManageFileClass
from api.swagger_api_test.swagger_manage_data_test import swaggerManageDataClass


class swaggerRunnerClass:

    def main(self):
        """
        here we will manage the test actions flow
        """
        start = swaggerManageFileClass(fileName=None, environment=None, credentials=None)
        name = start.name()
        yaml_path = start.url()
        credentials = start.credentials()
        start.create_swagger_yaml_file(name, yaml_path, credentials)
        all_requests = swaggerManageDataClass.get_all_yaml_requests(self)
        get_requests = swaggerManageDataClass.check_available_get_requests(self, all_requests)
        post_requests = swaggerManageDataClass.check_available_post_requests(self, all_requests)
        put_requests = swaggerManageDataClass.check_available_put_requests(self, all_requests)
        delete_requests = swaggerManageDataClass.check_available_delete_requests(self, all_requests)
        requests_path = swaggerManageDataClass.reqesuts_url_pth(self, yaml_path)
        SwaggerApiCallsClass.test_get(self, credentials, get_requests, requests_path)
        # SwaggerApiCallsClass.test_post(self, credentials, post_requests, requests_path)
        # SwaggerApiCallsClass.test_put(self, credentials, put_requests, requests_path)
        # SwaggerApiCallsClass.test_delete(self, credentials, delete_requests, requests_path)
        start.delete_swagger_yaml_file(name)