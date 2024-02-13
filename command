

sudo chown -R ideilson:www-data /var/www/site
python3 -m venv /var/www/site/.venv
source /var/www/site/.venv/bin/activate
pip install -r requirements.txt
pip install -r requirements.txt
python3 manage.py migrate
python -c "from django.core.management.utils import get_random_string; print(get_random_string(50))" > /var/www/site/secret_key.txt
cp /var/www/site/.env.example /var/www/site/.env
sudo systemctl restart site