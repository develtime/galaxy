Role Name
=========

Kibana is a role for install `kibana` service from `rpm` package

Role Variables
--------------

| Name              | Type   | Default value                                                        | Description                       |
| ----------------- | ------ | -------------------------------------------------------------------- | --------------------------------- |
| kbn_version       | string | 7.14.0                                                               | Версия Filebeat                   |
| kbn_port          | number | 5601                                                                 | Порт по умолчанию                 |
| kbn_package_name  | string | kibana-{{ kbn_version }}-x86_64.rpm                                  | Имя пакета                        |
| kbn_package_url   | string | https://artifacts.elastic.co/downloads/kibana/{{ kbn_package_name }} | Ссылка на скачивание пакета       |
| kbn_es_host_group | string | elasticsearch                                                        | Имя хоста сервера `elasticsearch` |
| kbn_es_port       | number | 9200                                                                 | Порт сервера `elasticsearch`      |


Tags
--------------

- `kibana`

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    kbn_es_host_group: elasticsearch-group
    kbn_es_port: 9200
  collections:
    - develtime.services
  roles:
    - kibana

- hosts: servers
  roles:
    - develtime.services.kibana
```

License
-------

MIT

Author Information
------------------

Develtime <smirnov.v.vadim@icloud.com>
