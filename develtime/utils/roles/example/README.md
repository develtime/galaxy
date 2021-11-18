Role Name
=========

'Example' is a simple role to test ansible modules

Role Variables
--------------

| Name | Type | Default value | Description |
|----------|----------|----------|----------|
| example_path | string | /tmp/example_file | Путь по которому будет создан файл |
| example_content | string | Hello world | Контен с которым будет создан файл |

Tags
--------------

- `example`

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    example_path: /tmp/some_file.txt
    example_content: Hello content
  collections:
    - develtime.utils
  roles:
    - example

- hosts: servers
  roles:
    - develtime.utils.example
```

License
-------

MIT

Author Information
------------------

Develtime <smirnov.v.vadim@icloud.com>
