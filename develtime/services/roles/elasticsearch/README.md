Role Name
=========

Elasticsearch is a role for install `elasticsearch` service from `rpm` package

Role Variables
--------------

| Name            | Type   | Default value                                                              | Description           |
| --------------- | ------ | -------------------------------------------------------------------------- | --------------------- |
| es_version      | string | 7.14.0                                                                     | Версия Elasticsearch |
| es_port         | number | 9200                                                                       | Порт по умолчанию |
| es_package_name | string | elasticsearch-{{ es_version }}-x86_64.rpm                                  | Имя пакета |
| es_package_url  | string | https://artifacts.elastic.co/downloads/elasticsearch/{{ es_package_name }} | Ссылка на скачивание пакета |
| es_seed_hosts   | array  | [ "{{ ansible_facts['default_ipv4']['address'] }}" ]                       | Список IP адресов нод в кластере |
| es_master_nodes | array  | [ "node-1" ]                                                               | Список имен мастер нод |
| es_node_name    | string | {{ es_master_nodes[0] }}                                                   | Имя ноды |

Tags
--------------

- `elasticsearch`

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    es_version: 7.14.0
    es_master_nodes:
        - "my-master-node-1"
    es_node_name: "my-master-node-1"
  collections:
    - develtime.services
  roles:
    - elasticsearch

- hosts: servers
  roles:
    - develtime.services.elasticsearch
```

License
-------

MIT

Author Information
------------------

Develtime <smirnov.v.vadim@icloud.com>
