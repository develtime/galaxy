#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: example_file

short_description: This is my example module to create file.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my example module to create file.

options:
    path:
        description: This is path to create new file.
        required: true
        type: str
    content:
        description: This is content of the target file.
        required: true
        type: str

author: Develtime <smirnov.v.vadim@icloud.com>
'''

EXAMPLES = r'''
# Example usage
- name: Example file
  develtime.utils.example_file:
    path: /tmp/example_file
    content: Hello world
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'File /tmp/example_file was created'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'Successfully created'
'''

import os
import tempfile
from shutil import copyfile

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes, to_native

def create_file(dest, content, module, result):
    changed = False

    # Generate temporary file name
    tmp_file = tempfile.mkstemp(prefix = 'example_file_')[1]
    
    # Create temporary file
    tfd = os.open(tmp_file, os.O_CREAT|os.O_RDWR)
    os.write(tfd, content)
    os.close(tfd)

    # Check destination file on changes
    if module.digest_from_file(tmp_file, 'md5') != module.digest_from_file(dest, 'md5'):
        changed = True

    # Copy only if not check_mode
    if not module.check_mode:
        copyfile(tmp_file, dest)

    # Remove temporary file
    os.remove(tmp_file)

    return changed

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    dest_path = module.params['path']
    content = to_bytes(module.params['content'])

    changed = create_file(dest_path, content, module, result)

    result['changed'] = changed
    result['original_message'] = f'File { dest_path } was created'
    result['message'] = 'Successfully created'

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
