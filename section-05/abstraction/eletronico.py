from log import LogPrintMixin, LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogFileMixin):
    def __init__(self, nome):
        super().__init__(nome)


    def ligar(self):
        super().ligar()
        
        if self._ligado:
            self.log_success(f'{self.nome} está ligado')

    def desligar(self):
        super().desligar()
        
        if not self._ligado:
            self.log_error(f'{self.nome} está desligado')


if __name__ == '__main__':

    s = Smartphone('Samsung')
    s.ligar()
    s.desligar()



