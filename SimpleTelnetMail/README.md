# 📧 Cliente SMTP con Adjuntos vía Telnet en Python

Este proyecto implementa un cliente SMTP **simple pero funcional** usando **Telnet** en Python. Permite enviar correos electrónicos con archivos adjuntos en formato `.txt` a través de un servidor SMTP local o de pruebas como `SubEthaSMTP`.

---

## 🚀 Características

- Comunicación SMTP básica vía sockets (sin usar `smtplib`)
- Envío de correos con asunto, cuerpo y adjuntos (`.txt`)
- Autenticación LOGIN (base64)
- Soporte para TLS (`STARTTLS`)
- Codificación MIME multipart con adjuntos en Base64
- Registro detallado de la comunicación SMTP

---

## 📂 Estructura del Proyecto

📁 tarea-06/ ├── smtp_telnet_attach.py # Clase TelnetMail que gestiona el envío de correos ├── main.py # Script principal para probar el cliente ├── test.txt # Archivo de prueba para adjuntar ├── correos/ # Carpeta donde se guardan los .eml (si usas un servidor local) └── README.md # Este archivo

yaml
Copiar
Editar

---

## 🛠 Requisitos

- Python 3.10+
- Entorno virtual (opcional pero recomendado)
- Servidor SMTP local como [SubEthaSMTP](https://github.com/davidmoten/subethasmtp) o Docker con Mailhog/Postfix

Instalación de dependencias (si fuera necesario):
```bash
pip install -r requirements.txt
⚙️ Cómo Usar
Ejecuta tu servidor SMTP local (por ejemplo con SubEthaSMTP en Java).

Asegúrate de que esté escuchando en localhost:25 o el puerto que definas.

Modifica main.py con tus valores reales:

python
Copiar
Editar
from smtp_telnet_attach import TelnetMail

client = TelnetMail(
    smtp_server="localhost",
    port=25,
    from_="tucorreo@fake.com",
    to=["destinatario@fake.com"],
    message="Hola, aquí tienes el archivo adjunto!",
    ssl=False,  # Usa True si tu servidor soporta STARTTLS correctamente
    username="usuario",
    password="contraseña"
)

client.attach_file("test.txt")
client.send_mail()
Ejecuta el script:

bash
Copiar
Editar
python main.py
📥 ¿Dónde se guarda el correo?
Si usas un servidor como SubEthaSMTP con salida a archivos .eml, los correos se guardarán en la carpeta configurada, por ejemplo:

bash
Copiar
Editar
C:/Users/tuusuario/Documents/emails/
Los archivos .eml pueden abrirse con:

Outlook o Thunderbird

Editores como VS Code

Sitios online como Encryptomatic Viewer

🧪 ¿Cómo leer el archivo adjunto?
Los archivos .eml contienen el adjunto en Base64. Puedes copiar esa sección y decodificarla online en:
👉 https://www.base64decode.org/

📌 Notas
Este proyecto es solo para fines educativos.

No lo uses para enviar spam ni en producción sin un servidor SMTP bien configurado.

Para pruebas reales con Gmail, activa contraseñas de aplicación y cambia el puerto a 587 con ssl=True.

✨ Créditos
Desarrollado por [Tu Nombre]
Curso: Sistemas Distribuidos - Tarea 06

📬 Licencia
MIT License – Puedes usar, modificar y compartir libremente.

yaml
Copiar
Editar

---

¿Quieres que te lo guarde como archivo `README.md`?







