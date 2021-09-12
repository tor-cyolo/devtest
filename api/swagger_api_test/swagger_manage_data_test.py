import yaml


class swaggerManageDataClass:

    def get_all_yaml_requests(self):
        with open("respond_yaml.yaml", 'r') as f:
            """
            here we create a static dictionary with all swagger API paths and data
            """
            valuesYaml = yaml.load(f, Loader=yaml.FullLoader)
            info = (valuesYaml['paths']['/v1/company/info'])
            logo = (valuesYaml['paths']['/v1/company/logo'])
            servers_watermark = (valuesYaml['paths']['/v1/company/servers_watermark'])
            admin_console_logo = (valuesYaml['paths']['/v1/company/admin_console_logo'])
            processes = (valuesYaml['paths']['/v1/processes'])
            processes_me = (valuesYaml['paths']['/v1/processes/me'])
            certificates = (valuesYaml['paths']['/v1/certificates'])
            certificates_id = (valuesYaml['paths']['/v1/certificates/{idOrName}'])
            users = (valuesYaml['paths']['/v1/users'])
            users_id = (valuesYaml['paths']['/v1/users/{idOrName}'])
            simple_groups = (valuesYaml['paths']['/v1/simple_groups'])
            simple_groups_id = (valuesYaml['paths']['/v1/simple_groups/{idOrName}'])
            dynamic_groups = (valuesYaml['paths']['/v1/dynamic_groups'])
            dynamic_groups_id = (valuesYaml['paths']['/v1/dynamic_groups/{idOrName}'])
            policies = (valuesYaml['paths']['/v1/policies'])
            policies_id = (valuesYaml['paths']['/v1/policies/{idOrName}'])
            personal_desktop_policy = (valuesYaml['paths']['/v1/personal_desktop_policy'])
            webhooks = (valuesYaml['paths']['/v1/webhooks'])
            webhooks_id = (valuesYaml['paths']['/v1/webhooks/{idOrName}'])
            activity_log = (valuesYaml['paths']['/v1/activity_log'])
            audit_log = (valuesYaml['paths']['/v1/audit_log'])
            licenses = (valuesYaml['paths']['/v1/licenses'])
            licenses_0 = (valuesYaml['paths']['/v1/licenses/0'])
            local_idps = (valuesYaml['paths']['/v1/local_idps'])
            local_idps_id = (valuesYaml['paths']['/v1/local_idps/{idOrName}'])
            ldaps = (valuesYaml['paths']['/v1/ldaps'])
            ldaps_id = (valuesYaml['paths']['/v1/ldaps/{idOrName}'])
            samls = (valuesYaml['paths']['/v1/samls'])
            samls_id = (valuesYaml['paths']['/v1/samls/{idOrName}'])
            openids = (valuesYaml['paths']['/v1/openids'])
            openids_id = (valuesYaml['paths']['/v1/openids/{idOrName}'])
            radiuses = (valuesYaml['paths']['/v1/radiuses'])
            radiuses_id = (valuesYaml['paths']['/v1/radiuses/{idOrName}'])
            auth_1 = (valuesYaml['paths']['/v1/auth/{kind}/{id}/stage/1'])
            auth_2 = (valuesYaml['paths']['/v1/auth/stage/2'])
            users_me = (valuesYaml['paths']['/v1/users/me'])
            logout = (valuesYaml['paths']['/cyolo/v1/logout'])
            totp_key_uri = (valuesYaml['paths']['/v1/users/me/totp-key-uri'])
            verify = (valuesYaml['paths']['/v1/users/me/verify'])
            commit = (valuesYaml['paths']['/v1/users/me/commit'])
            mappings = (valuesYaml['paths']['/v1/mappings'])
            mappings_id = (valuesYaml['paths']['/v1/mappings/{idOrName}'])
            sites = (valuesYaml['paths']['/v1/sites'])
            sites_id = (valuesYaml['paths']['/v1/sites/{idOrName}'])
            generic_secret = (valuesYaml['paths']['/v1/vault/generic_secret'])
            generic_secret_id = (valuesYaml['paths']['/v1/vault/generic_secret/{id}'])
            username_password = (valuesYaml['paths']['/v1/vault/username_password'])
            username_password_id = (valuesYaml['paths']['/v1/vault/username_password/{id}'])
            private_key = (valuesYaml['paths']['/v1/vault/private_key'])
            private_key_id = (valuesYaml['paths']['/v1/vault/private_key/{id}'])
            configuration_attributes = (valuesYaml['paths']['/v1/configuration_attributes'])
            configuration = (valuesYaml['paths']['/v1/configuration'])
            constraints = (valuesYaml['paths']['/v1/constraints'])
            capabilities = (valuesYaml['paths']['/v1/capabilities'])
            mapping_attributes = (valuesYaml['paths']['/v1/mapping_attributes'])
            api_keys = (valuesYaml['paths']['/v1/api_keys'])
            api_keys_id = (valuesYaml['paths']['/v1/api_keys/{idOrName}'])
            all_api = {'/v1/company/info': info, '/v1/company/logo': logo,
                       '/v1/company/servers_watermark': servers_watermark,
                       '/v1/company/admin_console_logo': admin_console_logo, '/v1/processes': processes,
                       '/v1/processes/me': processes_me, '/v1/certificates': certificates,
                       '/v1/certificates/{idOrName}': certificates_id, '/v1/users': users,
                       '/v1/users/{idOrName}': users_id, '/v1/simple_groups': simple_groups,
                       '/v1/simple_groups/{idOrName}': simple_groups_id, '/v1/dynamic_groups': dynamic_groups,
                       '/v1/dynamic_groups/{idOrName}': dynamic_groups_id, '/v1/policies': policies,
                       '/v1/policies/{idOrName}': policies_id, '/v1/personal_desktop_policy': personal_desktop_policy,
                       '/v1/webhooks': webhooks, '/v1/webhooks/{idOrName}': webhooks_id,
                       '/v1/activity_log': activity_log, '/v1/audit_log': audit_log, '/v1/licenses': licenses,
                       '/v1/licenses/0': licenses_0, '/v1/local_idps': local_idps,
                       '/v1/local_idps/{idOrName}': local_idps_id, '/v1/ldaps': ldaps, '/v1/ldaps/{idOrName}': ldaps_id,
                       '/v1/samls': samls, '/v1/samls/{idOrName}': samls_id, '/v1/openids': openids,
                       '/v1/openids/{idOrName}': openids_id, '/v1/radiuses': radiuses,
                       '/v1/radiuses/{idOrName}': radiuses_id, '/v1/auth/{kind}/{id}/stage/1': auth_1,
                       '/v1/auth/stage/2': auth_2, '/v1/users/me': users_me, '/cyolo/v1/logout': logout,
                       '/v1/users/me/totp-key-uri': totp_key_uri, '/v1/users/me/verify': verify,
                       '/v1/users/me/commit': commit, '/v1/mappings': mappings, '/v1/mappings/{idOrName}': mappings_id,
                       '/v1/sites': sites, '/v1/sites/{idOrName}': sites_id, '/v1/vault/generic_secret': generic_secret,
                       '/v1/vault/generic_secret/{id}': generic_secret_id,
                       '/v1/vault/username_password': username_password,
                       '/v1/vault/username_password/{id}': username_password_id, '/v1/vault/private_key': private_key,
                       '/v1/vault/private_key/{id}': private_key_id,
                       '/v1/configuration_attributes': configuration_attributes, '/v1/configuration': configuration,
                       '/v1/constraints': constraints, '/v1/capabilities': capabilities,
                       '/v1/mapping_attributes': mapping_attributes, '/v1/api_keys': api_keys,
                       '/v1/api_keys/{idOrName}': api_keys_id}
            return all_api

    def check_available_get_requests(self, all_requests):
        """
        here we run on all dictionary keys and return only those with "get" method
        """
        available = all_requests
        new_get_list = []
        for key, value in available.items():
            if 'get' in value:
                new_get_list.append(key)
        return new_get_list

    def check_available_post_requests(self,all_requests):
        """
        here we run on all dictionary keys and return only those with "post" method
        """
        available = all_requests
        new_post_list = []
        for key, value in available.items():
            if 'post' in value:
                new_post_list.append(key)
        return new_post_list

    def check_available_put_requests(self, all_requests):
        """
        here we run on all dictionary keys and return only those with "put" method
        """
        available = all_requests
        new_put_list = []
        for key, value in available.items():
            if 'put' in value:
                new_put_list.append(key)
        return new_put_list

    def check_available_delete_requests(self, all_requests):
        """
        here we run on all dictionary keys and return only those with "get" method
        """
        available = all_requests
        new_delete_list = []
        for key, value in available.items():
            if 'delete' in value:
                new_delete_list.append(key)
        return new_delete_list

    def reqesuts_url_pth(self, yaml_path):
        """
        here we get the environment path and create the requests path according to it
        """
        path = ''
        if yaml_path == 'https://console.local.cyolo.io:9090/swagger-ui/swagger.yaml':
            path = 'https://console.local.cyolo.io:9090'
        elif yaml_path == 'https://console.dev.cyolo.io:9090/swagger-ui/swagger.yaml':
            path = 'https://console.dev.cyolo.io:9090'
        elif yaml_path == 'https://console.local.stg.io:9090/swagger-ui/swagger.yaml':
            path = 'https://console.stg.cyolo.io:9090'
        else:
            "print no matching url"
        return path
