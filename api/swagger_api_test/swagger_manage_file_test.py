import os
import requests
import yaml
from api.swagger_api_test.swagger_enums import swaggerEnumsClass


class swaggerManageFileClass:

    def __init__(self, fileName=None, environment=None, credentials=None):
        self._fileName = fileName
        self._environment = environment
        self._credentials = credentials

    @property
    def get_fileName(self):
        """
        here we get the swagger yaml file name
        """
        return self._fileName

    @property
    def get_environment(self):
        """
        here we get environment we want to run the test on
        """
        return self._environment

    @property
    def get_credentials(self):
        """
        here we get the user API key credentials
        """
        return self._credentials

    @get_fileName.setter
    def set_fileName(self, x):
        """
        here we set the swagger yaml file name
        """
        file_name = x
        print("the name of the file is: ", file_name)
        self._fileName = file_name

    @get_environment.setter
    def set_environment(self, x):
        """
        here we set the environment we want to run the test on
        """
        option_lists = [1, 2, 3]
        try:
            environment_type = int(x)
        except ValueError:
            print("please enter an integer")
            breakpoint()
        if environment_type in option_lists:
            environment_type = environment_type
        else:
            print("not a valid number, please enter a number from 1 to 3")
            raise breakpoint()
        if environment_type == 1:
            environment_type = swaggerEnumsClass.local_env.value
        elif environment_type == 2:
            environment_type = swaggerEnumsClass.dev_env.value
        elif environment_type == 3:
            environment_type = swaggerEnumsClass.staging_env.value
        self._environment = environment_type

    @get_credentials.setter
    def set_credentials(self, x):
        """
        here we set the user API key credentials
        """
        credentials = x
        self._credentials = credentials

    def name(self):
        """
        here we call the file name method and entering a value
        """
        self.set_fileName = swaggerEnumsClass.swagger_yaml_name.value
        return self._fileName

    def url(self):
        """
        here we call the environment method and entering values
        """
        self.set_environment = (input("Please select the wanted environment:\n"
                                      "1. " + swaggerEnumsClass.local_env.value + "\n"
                                        "2. " + swaggerEnumsClass.dev_env.value + "\n"
                                            "3. " + swaggerEnumsClass.staging_env.value + "\n"))
        return self._environment

    def credentials(self):
        """
        here we call the credentials method and entering values
        """
        print("API key headers example: ")
        print(swaggerEnumsClass.credentials.value)
        dictionery = {}
        self.key = input("Enter key: ")
        self.value = input("Enter value: ")
        dictionery.update({self.key: self.value})
        self.set_credentials = dictionery
        return self.set_credentials

    def create_swagger_yaml_file(self, name, path, credentials):
        """
        here we create the swagger yaml file if it doesn't exist
        """
        if os.path.exists(name):
            print("swagger yaml file exist, we don't need to create a new one")
        else:
            print("swagger yaml file doesn't exist, we need to create a new one")
            response = requests.get(path, headers=credentials)
            response.raise_for_status()
            print(yaml.safe_load(response.text))
            file = open("respond_yaml.yaml", "w")
            file.write(response.text)
            file.close()

    def delete_swagger_yaml_file(self, name):
        """
        here we delete the "respond_yaml" file
        """
        if os.path.exists(name):
            os.remove(name)
        else:
            print('there is no file to delete')