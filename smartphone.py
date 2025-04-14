class Smartphone:
    def __init__(self, nome, memoria):
        self.nome = nome
        self.memoria = memoria
        self.apps_instaladas = []
        self.status = 'OFF'

    def Install(self, app, tam):
        if self.status == 'ON':
            if self.memoria >= tam:
                self.apps_instaladas.append(app)
                self.memoria -= tam
                print(f"App {app} instalado com sucesso!")
            else:
                print("Memória insuficiente para instalar o app.")
        else:
            print("O smartphone está desligado. Ligue-o para instalar apps.")

    def Power(self, onOff):
        if onOff in ['ON', 'OFF']:
            self.status = onOff
            print(f"Smartphone {self.status}.")
        else:
            print("Comando inválido. Use 'ON' ou 'OFF'.")

    def Lista(self):
        if self.apps_instaladas:
            print("Apps instaladas:", ", ".join(self.apps_instaladas))
        else:
            print("Nenhum app instalado.")

# Testando a classe
smartphone = Smartphone("MeuSmartphone", 1000)
smartphone.Power("ON")
smartphone.Install("WhatsApp", 200)
smartphone.Install("Instagram", 300)
smartphone.Lista()
smartphone.Power("OFF")
