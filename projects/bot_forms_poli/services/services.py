from abc import ABC, abstractmethod

class BotBase(ABC):
    def __init__(self, name: str, login: str, email: str, password: str) -> None:
        self.name = name
        self.login = login
        self.email = email
        self.password = password

    @classmethod
    @abstractmethod
    def preencher_formulario(self) -> str:
        pass

    def preencher_formulario(self) -> str:
        return "Formulario Base preenchido!"

    def get_name(self) -> str:
        return self.name
    
    def get_login(self) -> str:
        return self.login
    
    def get_email(self) -> str:
        return self.email
    
    def get_password(self) -> str:
        return self.password

class BotCadastro(BotBase):
    def __init__(self, login, password) -> None:
        self.name = None
        self.login = login
        self.email = None
        self.password = password

    def preencher_formulario(self) -> str:
        return "Formulario Cadastro preenchido"
    
class BotAtualizacao(BotBase):
    def __init__(self, name, login) -> None:
        self.name = name
        self.login = login
        self.email = None
        self.password = None

    def preencher_formulario(self) -> str:
        return "Formulario Atualizacao preenchido"