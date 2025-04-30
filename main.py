from smtp_telnet_attach import TelnetMail

client = TelnetMail(
    smtp_server="localhost",
    port=25,  # Cambia esto si usas otro proveedor
    from_="tucorreo@fake.com",
    to=["destinatario@fake.com"],
    message="Hola, aquí tienes el archivo adjunto!",
    ssl=False,
    username="tucorreo@gmail.com",
    password="tu_contraseña_de_aplicacion"  # Usa una contraseña de app si es Gmail
)

client.attach_file("./test.txt")  # Pon aquí la ruta real del archivo
client.send_mail()

