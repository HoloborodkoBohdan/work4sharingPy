import threading

from django.core import mail


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, sender):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.sender = sender
        threading.Thread.__init__(self)

    def run(self):
        #print('*> ', self.subject)

        connection = mail.get_connection()
        connection.open()
        email = mail.EmailMessage(self.subject, self.html_content, self.sender,
                                   self.recipient_list, connection=connection)
        email.send()
        connection.close()
        print('> send: ', self.subject)


def send_html_mail(subject, html_content, recipient_list, sender):
    EmailThread(subject, html_content, recipient_list, sender).start()