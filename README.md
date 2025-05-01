
markdown
# SimpleTelnetMail - Envío de Correos por Telnet

Este proyecto permite enviar correos electrónicos a través del protocolo SMTP utilizando Telnet de manera sencilla.

## Requisitos previos

Antes de ejecutar el programa, asegúrate de tener instalado:

- Python 3.6 o superior
- `FakeSMTP` (para pruebas locales)
- Acceso a línea de comandos o terminal

## Pasos para la ejecución

### 1. Iniciar FakeSMTP

Primero, abre `FakeSMTP` para simular un servidor SMTP local y recibir los correos de prueba. Puedes descargarlo desde [https://nilhcem.com/FakeSMTP/](https://nilhcem.com/FakeSMTP/).

Una vez descargado, ejecútalo y asegúrate de que esté escuchando en el puerto **25** (o el que tengas configurado).

### 2. Crear y activar un entorno virtual

Abre una terminal y navega hasta el directorio del proyecto. Luego, crea un entorno virtual con:

```bash
python -m venv venv
```

Actívalo:

- En Windows:

  ```bash
  venv\Scripts\activate
  ```

- En macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar dependencias

Con el entorno activado, instala el paquete necesario:

```bash
pip install SimpleTelnetMail
```

### 4. Ejecutar el programa

Finalmente, ejecuta el archivo principal:

```bash
python main.py
```

Esto abrirá una sesión Telnet para enviar un correo utilizando los datos proporcionados en el script.

---

## Notas

- Asegúrate de que el puerto de `FakeSMTP` coincida con el configurado en `main.py`.
- Este proyecto está diseñado para fines educativos y de prueba. No se recomienda para entornos de producción sin cifrado ni autenticación.

