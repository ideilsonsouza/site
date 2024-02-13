

sudo chown -R ideilson:www-data /var/www/site
python3 -m venv /var/www/site/.venv
source /var/www/site/.venv/bin/activate
pip install setuptools
pip install -r requirements.txt
SECRET_KEY=$(python -c "from django.core.management.utils import get_random_string; print(get_random_string(50))")
sed -i "s|SECRET_KEY=.*|SECRET_KEY=$SECRET_KEY|g" /var/www/site/.env
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
sudo systemctl restart site