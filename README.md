git clone https://github.com/eliasful/hero-api.git
cd hero-api  
python3 -m venv env
. env/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate        
python3 manage.py runserver
