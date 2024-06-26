#! /usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.okan_tools import format_stuff


def main():
    module_fields = {"mystring": {}}
    module = AnsibleModule(argument_spec=module_fields)
    my_string_data = module.params["mystring"]
    formatted_string = format_stuff(my_string_data)

    module.params.update({"mystring": formatted_string})
    module.params.update({"my_original_string": my_string_data})

    module.exit_json(data=module.params)

if __name__ == '__main__':
    main()
