import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog
from biglietto.model.Biglietto import *


class ControlloreBiglietto:
    def __init__(self):
        super(ControlloreBiglietto, self).__init__()

    def genera_biglietto(self, file_path, data, attivita, email, nome, cognome):
        self.biglietto = Biglietto(attivita, data, email, nome, cognome)

        # Richiedi all'utente di inserire i parametri
        title = "Biglietto d'ingresso"
        author = "Museo delle scienze naturali di Camerino"
        content = [self.biglietto.data, self.biglietto.attivita, self.biglietto.email, self.biglietto.nome, self.biglietto.cognome]
        heading = ["Data: ", "Attivita: ", "Email: ", "Nome: ", "Cognome: "]

        # Crea un documento PDF
        c = canvas.Canvas(file_path, pagesize=letter)
        c.setTitle("Biglietto d'ingresso")

        # Aggiungi il titolo al PDF
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(300, 750, title)

        # Aggiungi l'autore al PDF
        c.setFont("Helvetica-Oblique", 12)
        c.drawCentredString(300, 730, author)

        # Aggiungi il contenuto al PDF
        #c.setFont("Helvetica", 10)
        y_position = 700  # Altezza iniziale del testo
        for i in range(5):
            print(len(heading[i]))
            c.setFont("Helvetica-Bold", 12)
            c.drawString(12, y_position, heading[i])
            c.setFont("Helvetica", 10)
            c.drawString(100, y_position, content[i])
            y_position -= 12  # Spaziatura tra le linee
        return c

    def scarica_biglietto(self, data, attivita, email, nome, cognome):

        # Utilizza la finestra di dialogo per selezionare il percorso di salvataggio
        root = tk.Tk()
        root.withdraw()  # Nasconde la finestra principale di Tkinter
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile="Biglietto d'ingresso")
        print(file_path)
        biglietto_pdf = self.genera_biglietto(file_path, data, attivita, email, nome, cognome)
        # Verifica se l'utente ha scelto un percorso
        if file_path:
            # Salva il file PDF nel percorso scelto
            biglietto_pdf.save()
            print(f"Biglietto salvato con successo in: {file_path}")
        else:
            print("Operazione di salvataggio annullata dall'utente")

    def invia_biglietto_per_email(self, destinatario, data, attivita, nome, cognome):
        biglietto_pdf = self.genera_biglietto("output.pdf", data, attivita, destinatario, nome, cognome)
        biglietto_pdf.save()

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
        msg.attach(MIMEText(f"Gentile {nome} {cognome}, in allegato trova il Suo biglietto.\n "
                            f"Il biglietto é nominativo e va presentato al bancone di ingresso del museo "
                            f"per accedere ai servizi da Lei prenotati.\n"
                            f"Cordiali saluti", 'plain'))

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
