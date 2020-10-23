mkdir root/shr 2>/dev/null
docker-compose up -d --no-recreate
docker-compose exec ctf-container /bin/bash