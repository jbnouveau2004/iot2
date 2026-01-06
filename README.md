COMMUNICATION AVEC LE GPIO (27 pour la led et 4 pour le bouton)

sudo apt-get install python3-flask python3-lgpio python3-flask-cors

cd backend
sudo python3 gpio_api.py
lancer pytghon avec sudo sinon: sudo usermod -aG gpio pi

cd frontend 
python3 -m http.server 8080 --bind 0.0.0.0

TEST:
Aluumer la led
curl -X POST http://RASPBERRY_IP:3000/led \
  -H "Content-Type: application/json" \
  -d '{"value": true}'

Eteindre la led
curl -X POST http://RASPBERRY_IP:3000/led \
  -H "Content-Type: application/json" \
  -d '{"value": false}'

Test bouton
curl http://RASPBERRY_IP:3000/button