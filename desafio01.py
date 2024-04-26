class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Favorito: {'Sim' if self.favorito else 'Não'}"


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        for i, contato in enumerate(self.contatos):
            print(f"{i+1}: {contato}")

    def editar_contato(self, indice, novo_contato):
        self.contatos[indice] = novo_contato

    def marcar_favorito(self, indice):
        self.contatos[indice].favorito = True

    def desmarcar_favorito(self, indice):
        self.contatos[indice].favorito = False

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if favoritos:
            for i, contato in enumerate(favoritos):
                print(f"{i+1}: {contato}")
        else:
            print("Nenhum contato favorito encontrado.")

    def apagar_contato(self, indice):
        del self.contatos[indice]


def main():
    agenda = Agenda()

    while True:
        print("\n========== Agenda de Contatos ==========")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/Desmarcar Favorito")
        print("5. Listar Favoritos")
        print("6. Apagar Contato")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            favorito = input("Marcar como favorito? (s/n): ").lower() == "s"
            novo_contato = Contato(nome, telefone, email, favorito)
            agenda.adicionar_contato(novo_contato)
            print("Contato adicionado com sucesso!")
        elif opcao == "2":
            print("\n========== Lista de Contatos ==========")
            agenda.listar_contatos()
        elif opcao == "3":
            indice = int(input("Digite o índice do contato a ser editado: ")) - 1
            novo_nome = input("Digite o novo nome do contato: ")
            novo_telefone = input("Digite o novo telefone do contato: ")
            novo_email = input("Digite o novo email do contato: ")
            novo_contato = Contato(novo_nome, novo_telefone, novo_email)
            agenda.editar_contato(indice, novo_contato)
            print("Contato editado com sucesso!")
        elif opcao == "4":
            indice = int(input("Digite o índice do contato: ")) - 1
            favoritar = input("Marcar como favorito? (s/n): ").lower() == "s"
            if favoritar:
                agenda.marcar_favorito(indice)
                print("Contato marcado como favorito!")
            else:
                agenda.desmarcar_favorito(indice)
                print("Contato desmarcado como favorito!")
        elif opcao == "5":
            print("\n========== Lista de Favoritos ==========")
            agenda.listar_favoritos()
        elif opcao == "6":
            indice = int(input("Digite o índice do contato a ser apagado: ")) - 1
            agenda.apagar_contato(indice)
            print("Contato apagado com sucesso!")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
