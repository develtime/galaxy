Role Name
=========

Filebeat is a role for install `filebeat` service from `rpm` package

Role Variables
--------------

| Name            | Type   | Default value                                                              | Description           |
| --------------- | ------ | -------------------------------------------------------------------------- | --------------------- |
| fb_version      | string | 7.14.0                                                                     | Версия Filebeat |
| fb_package_name | string | filebeat-{{ fb_version }}-x86_64.rpm                                  | Имя пакета |
| fb_package_url  | string | https://artifacts.elastic.co/downloads/beats/filebeat/{{ fb_package_name }} | Ссылка на скачивание пакета |
| fb_modules   | array  | [ "system" ]                       | Список устанавливаемых модулей |
| fb_output_logstash    | boolean | false | Парметр задает значение указывающее выходной канал, `logstash` или `elasticsearch`, по умолчанию используется `elasticsearch` |
| fb_output_host_group    | string | elasticsearch | Имена группы хостов для отправки данных |
| fb_output_port    | number | 9200 | Порт для отправки данных |
| fb_kbn_host    | string | kibana | Имя хоста сервера `kibana` |
| fb_kbn_port    | number | 5601 | Порт сервера `kibana` |
| fb_setup_dashboards    | boolean | false | Экстра аргумент указывающий необходимость настройки дашбордов на сервере `kibana`. Пример: `ansible-playbook site.yml -e fb_setup_dashboards=true` |

Tags
--------------

- `filebeat`

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    fb_output_logstash: true
    fb_output_host_group: logstash-group
    fb_output_port: 5044
  collections:
    - develtime.services
  roles:
    - filebeat

- hosts: servers
  roles:
    - develtime.services.filebeat
```

License
-------

MIT

Author Information
------------------

Develtime <smirnov.v.vadim@icloud.com>
