mkdir root\shr 2>NUL
docker-compose up -d --no-recreate
docker-compose exec ctf-container /bin/bash