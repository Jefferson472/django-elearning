# django-elearning
Plataforma de cursos onlines desenvolvida com Django

<div align="center" id="badges">
    <img src="https://img.shields.io/badge/STATUS-WIP-red"/>
</div>
---

## CACHE
`docker run --name memcache -p 11211:11211 memcached`

### Monitorando o cache
django-memcache-status # essa feature não funciona no pymemcache


### Docker Compose Error Invalid Template
Aparentemente o cli do docker-compose está com um erro de leitura para alguns caracteres contido no arquivo `.env` retornando `invalid template`.
https://github.com/docker/compose-cli/issues/1896

Para escapar desse erro, remova temporariamente a chave que contém o erro, no caso deste projeto o caractere inválido está no `SECRET_KEY` do Django.

### Know Issues
Se estiver utilizando qualquer SO baseado em Unix ou Docker, a dependência twisted-iocpsupport==1.0.2 não será necessária, pois ela é utilizada para conectar aos sockets do windows.


### Channels Daphne

`daphne -u /tmp/daphne.sock src.setup.asgi:application`

### Config Comandos

`python manage.py enroll_reminder --days=20`

Cron

`crontab -e`

`0 8 * * * python path/to/project/manage.py enroll_reminder --20=days --setings=setup.settings.prod`

### Executando o servidor com Nginx localmente
/etc/hosts
C:\Windows\System32\drivers\etc
127.0.0.1   www.django-elearning.com
127.0.0.1   django-elearning.com
