# django-elearning
Plataforma de cursos onlines desenvolvida com Django


## CACHE
`docker run --name memcache -p 11211:11211 memcached`

### Monitorando o cache
django-memcache-status # essa feature não funciona no pymemcache


### Docker Compose Error Invalid Template
Aparentemente o cli do docker-compose está com um erro de leitura para alguns caracteres contido no arquivo `.env` retornando `invalid template`.
https://github.com/docker/compose-cli/issues/1896

Para escapar desse erro, remova temporariamente a chave que contém o erro, no caso deste projeto o caractere inválido está no `SECRET_KEY` do Django.
