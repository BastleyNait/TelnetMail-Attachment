import telnetlib
import ssl
from base64 import b64encode
from os.path import basename
import mimetypes

class TelnetMail:
    def __init__(
        self,
        smtp_server: str,
        from_: str,
        to: list,
        message: str = "Hola!",
        port: int = 587,
        ssl: bool = True,
        username: str = "",
        password: str = "",
    ):
        self.smtp_server = smtp_server
        self.port = port
        self.from_ = from_
        self.to = to
        self.message = message
        self.ssl = ssl
        self.username = username
        self.password = password
        self._server = None

    def attach_file(self, filepath):
        boundary = "===BOUNDARY==="
        file_name = basename(filepath)
        content_type, _ = mimetypes.guess_type(filepath)
        if content_type is None:
            content_type = "application/octet-stream"

        with open(filepath, "rb") as f:
            file_content = f.read()
        encoded_file = b64encode(file_content).decode()

        headers = f"""MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{boundary}"
"""

        body = f"""--{boundary}
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

{self.message}
"""

        attachment = f"""--{boundary}
Content-Type: {content_type}; name="{file_name}"
Content-Disposition: attachment; filename="{file_name}"
Content-Transfer-Encoding: base64

{encoded_file}
--{boundary}--
"""

        self.message = headers + "\n" + body + "\n" + attachment

    def _read(self):
        data = self._server.read_until(b"\n", timeout=3).decode("utf-8")
        print("[←]", data.strip())
        return data

    def _write(self, command: str, display: str = None):
        if display:
            print("[→]", display)
        else:
            print("[→]", command.strip())
        self._server.write((command + "\r\n").encode("utf-8"))

    def send_mail(self):
        self._server = telnetlib.Telnet(self.smtp_server, self.port, timeout=10)
        self._read()
        self._write("EHLO smtp.local")
        self._read()

        if self.ssl:
            self._write("STARTTLS")
            self._read()
            self._server.sock = ssl.wrap_socket(self._server.sock)

            self._write("EHLO smtp.local")
            self._read()

        self._write("AUTH LOGIN")
        self._read()
        self._write(b64encode(self.username.encode()).decode(), display="USERNAME")
        self._read()
        self._write(b64encode(self.password.encode()).decode(), display="PASSWORD")
        self._read()

        self._write(f"MAIL FROM:<{self.from_}>")
        self._read()
        for t in self.to:
            self._write(f"RCPT TO:<{t}>")
            self._read()

        self._write("DATA")
        self._read()
        self._write(f"Subject: Prueba con Adjunto\r\nFrom: {self.from_}\r\nTo: {', '.join(self.to)}\r\n\r\n{self.message}\r\n.")
        self._read()

        self._write("QUIT")
        self._read()
        self._server.close()
