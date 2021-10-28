Role Name
=========

Logstash is a role for install `logstash` service from `rpm` package

Role Variables
--------------

| Name                 | Type   | Default value                                                         | Description                                             |
| -------------------- | ------ | --------------------------------------------------------------------- | ------------------------------------------------------- |
| ls_user              | string | logstash                                                              | Имя пользователя для выдачи прав на дирректории сервиса |
| ls_group             | string | logstash                                                              | Имя группы для выдачи прав на дирректории сервиса       |
| ls_version           | string | 7.14.0                                                                | Версия Filebeat                                         |
| ls_port              | number | 9600                                                                  | Порт по умолчанию                                       |
| ls_beats_port        | number | 5044                                                                  | Порт по умолчанию для beats                             |
| ls_package_name      | string | logstash-{{ ls_version }}-x86_64.rpm                                  | Имя пакета                                              |
| ls_package_url       | string | https://artifacts.elastic.co/downloads/logstash/{{ ls_package_name }} | Ссылка на скачивание пакета                             |
| ls_node_name         | string | node-1                                                                | Имя ноды                                                |
| ls_output_host_group | string | elasticsearch                                                         | Имя хоста сервера `elasticsearch`                       |
| ls_output_port       | number | 9200                                                                  | Порт сервера `elasticsearch`                            |
| ls_install_plugins   | array  | [ "logstash-input-beats", "logstash-filter-multiline" ]               | Список плагинов для установки                           |
| ls_home              | string | /usr/share/logstash                                                   | Домашняя директория logstash                            |
| ls_log_directory     | string | {{ ls_home }}/logs                                                    | Директория для логов                                    |
| ls_conf_directory    | string | /etc/logstash                                                         | Директория для файлов настроек                          |


Tags
--------------

- `logstash`

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    ls_output_host_group: elasticsearch-group
    ls_output_port: 9200
  collections:
    - develtime.services
  roles:
    - logstash

- hosts: servers
  roles:
    - develtime.services.logstash
```

License
-------

MIT

Author Information
------------------

Develtime <smirnov.v.vadim@icloud.com>
