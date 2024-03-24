echo "BUILD START"
python3.10  -m pip3.10 install -r requirements.txt

echo "Make Migration..."
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput

python3.10 manage.py collectstatic  --noinput --clear
echo "BUILD END"