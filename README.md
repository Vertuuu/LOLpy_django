
with terminal in project root:
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pip install -i https://test.pypi.org/simple/ LOLpy_Vertuuu==0.0.10

to run django app, still in project root:
cd LOLpy_django
py manage.py runserver

after that, you open your browser on the port 8000