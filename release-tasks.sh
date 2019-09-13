npm install
npm run build --prod
python manage.py migrate --noinput
python manage.py collectstatic --noinput