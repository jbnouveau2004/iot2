sudo apt-get install python3-flask python3-lgpio

cd backend
sudo python3 gpio_api.py
lancer pytghon avec sudo sinon: sudo usermod -aG gpio pi

cd frontend 
python3 -m http.server 8080 --bind 0.0.0.0