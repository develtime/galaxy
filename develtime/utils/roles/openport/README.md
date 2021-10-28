Role Name
=========

Openport is a slim role for open port with `firewalld` service

Role Variables
--------------

| Name | Type | Default value | Description |
|----------|----------|----------|----------|
| open_port_default_proto | string | tcp | Протокол по умолчанию |
| open_ports | array | [] | Список номеров портов для открытия, предусматривает возможность указания номера порта и номера порта с протоколом. Пример: `[ 80, '21/tcp' ]` |

Tags
--------------

- `openport`

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    open_port_default_proto: udp
    open_ports:
      - 5050
      - 3000
  collections:
    - develtime.utils
  roles:
    - openport

- hosts: servers
  roles:
    - develtime.utils.openport
```

License
-------

MIT

Author Information
------------------

Develtime <smirnov.v.vadim@icloud.com>
