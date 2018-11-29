git clone https://github.com/eliasful/heros-api.git
cd heros-api  
python3 -m venv env
. env/bin/activate
pip3 install -r requirements.txt
python3 manage.py runserver
