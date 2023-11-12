import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog
from io import BytesIO
from biglietto.model.Biglietto import *


class ControlloreBiglietto:
    def __init__(self):
        super(ControlloreBiglietto, self).__init__()
        #self.model = Biglietto()

    def genera_biglietto(self, data, attivita, email, nome, cognome):

        # Richiedi all'utente di inserire i parametri
        title = "Biglietto d'ingresso"
        author = "Museo delle scienze naturali di Camerino"
        content = [data, attivita, email, nome, cognome]

        # Specifica il percorso del file PDF da generare
        file_path = "output.pdf"

        # Crea un documento PDF
        c = canvas.Canvas(file_path, pagesize=letter)

        # Aggiungi il titolo al PDF
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(300, 750, title)

        # Aggiungi l'autore al PDF
        c.setFont("Helvetica-Oblique", 12)
        c.drawCentredString(300, 730, f"Autore: {author}")

        # Aggiungi il contenuto al PDF
        c.setFont("Helvetica", 10)
        y_position = 700  # Altezza iniziale del testo
        for line in content:
            c.drawString(12, y_position, line)
            y_position -= 12  # Spaziatura tra le linee
        c.save()
        return c

    def scarica_biglietto(self, data, attivita, email, nome, cognome):
        biglietto_pdf = self.genera_biglietto(data, attivita, email, nome, cognome)

        # Utilizza la finestra di dialogo per selezionare il percorso di salvataggio
        root = tk.Tk()
        root.withdraw()  # Nasconde la finestra principale di Tkinter
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile="Biglietto d'ingresso")

        # Verifica se l'utente ha scelto un percorso
        if file_path:
            # Salva il file PDF nel percorso scelto
            biglietto_pdf.save()
            print(f"Biglietto salvato con successo in: {file_path}")
        else:
            print("Operazione di salvataggio annullata dall'utente")

    def invia_biglietto_per_email(self, destinatario, data, attivita, nome, cognome):
        biglietto_pdf = self.genera_biglietto(data, attivita, destinatario, nome, cognome)

        # Configura le informazioni dell'account email
        email_mittente = "museo.noreply@gmail.com"
        password_mittente = "mnjo lkvo wrbb upru"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Crea un oggetto messaggio
        msg = MIMEMultipart()
        msg['From'] = email_mittente
        msg['To'] = destinatario
        msg['Subject'] = "Biglietto d'ingresso"

        # Aggiungi il corpo del messaggio
        msg.attach(MIMEText("Testo email", 'plain'))

        # Aggiungi l'allegato PDF
        with open("output.pdf", "rb") as pdf_file:
            part = MIMEApplication(pdf_file.read(), Name="Biglietto d'ingresso.pdf")
            part['Content-Disposition'] = f'attachment; filename="Biglietto ingresso.pdf"'
            msg.attach(part)

        # Connessione al server SMTP e invio dell'email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_mittente, password_mittente)
                server.sendmail(email_mittente, destinatario, msg.as_string())
            print("Email inviata con successo.")
        except Exception as e:
            print(f"Errore durante l'invio dell'email: {e}")


