accesslog = "-"  # here "-" means stdout

# Gunicorn está configurado para escuchar en todas las interfaces de red en el puerto 5000
# es seguro porque se ejecuta en una red Docker aislada y solo el proxy inverso (Nginx) tiene acceso a él
bind = "0.0.0.0:5000"

errorlog = "-"  # here "-" means stdout

wsgi_app = "src.app:app"
