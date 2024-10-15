class FormsBase:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def show_infos_name(self):
        return self.name

    def show_infos_email(self):
        return self.email

    def show_infos_password(self):
        return self.password

class FormsContact:
    def __init__(self, contact):
        self.contact = contact

    def show_infos_contact(self):
        return self.contact

class FormsLogin:
    def __init__(self, login):
        self.login = login

    def show_infos_login(self):
        return self.login

class FormsComplete(FormsBase, FormsContact, FormsLogin):
    def __init__(self, name, email, password, contact, login):
        FormsBase.__init__(self, name, email, password)
        FormsContact.__init__(self, contact)
        FormsLogin.__init__(self, login)

    def infos_complete(self):
        self.show_infos_name()
        self.show_infos_email()
        self.show_infos_password()
        self.show_infos_contact()
        self.show_infos_login()
