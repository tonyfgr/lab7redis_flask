from flask import Flask, request, render_template
import redis
import os

# Inicializar la aplicación Flask
app = Flask(__name__)

# Conexión al servidor Redis
r = redis.Redis(host='redis', port=6379)

# Ruta principal con soporte para GET y POST
@app.route('/', methods=['GET', 'POST'])
def vote():
    option_a = "Cats"
    option_b = "Dogs"
    
    # Si se envía el formulario
    if request.method == 'POST':
        vote = request.form['vote']
        if vote == 'a':
            r.incr('votes_cats')  # Incrementa el voto para Cats
        elif vote == 'b':
            r.incr('votes_dogs')  # Incrementa el voto para Dogs

    # Obtener los votos actuales
    vote_a = r.get('votes_cats') or 0
    vote_b = r.get('votes_dogs') or 0
    
    # Renderizar la plantilla HTML con los datos
    return render_template('index.html', option_a=option_a, option_b=option_b, 
                           vote=request.form.get('vote'), hostname=os.getenv('HOSTNAME'),
                           vote_a=int(vote_a), vote_b=int(vote_b))

# Comprobar si el script se está ejecutando directamente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
