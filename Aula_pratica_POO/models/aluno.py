import datetime
from uuid import uuid4



class Aluno:


# ATRIBUTOS

    def __init__(self, nome, nascimento):   #função para inicializar e os paramentros
        self.nome = nome            #self.nome do atributo = valor que queremos
        self.nascimento = nascimento
        self.matricula = str(uuid4())
        self.ingresso = datetime.timezone
        self.curso = None
        self.notas = None

# COMPORTAMENTOS
    def marcar_prova(self, data_prova, nome_prova ):            #Função de marcar prova
        provas = {}
        prova = provas.get(nome_prova)

        if not prova:
            raise Exception             #raise funciona dentro das funções

        prova["data"] = data_prova
        prova["aluno"] = self.matricula

        return f"Sua prova foi marcada para o dia {data_prova} com sucesso!"

    def fazer_media(self):
        if not self.notas:
            return "Nenhuma nota foi encontrada"

        media = sum(self.notas)/len(self.notas)

        return f"Sua média é de {media}!"

    def repor_aula(self, nome_aula, data_reposicao):
        aulas_perdidas = {}
        aula = aulas_perdidas.get(nome_aula)

        if not aula:
            return "Você já fez está aula"

        aula["data_reposicao"] = data_reposicao
        aula["Aluno"] = self.matricula

        return f"Sua aula foi marcada para dia {data_reposicao}!"


