#! /usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():
    module_fields = {"mystring": {}}
    module = AnsibleModule(argument_spec=module_fields)
    my_string_data = module.params["mystring"]
    upper_string_data = my_string_data.upper()
    module.params.update({"mystring": upper_string_data})
    module.exit_json(data=module.params)

if __name__ == '__main__':
    main()
