from Aula_pratica_POO.models.aluno import Aluno

CURSOS = {}     #simulação de banco de dados
ALUNOS = []     #simulação de banco de dados

def cadastrar_aluno(nome, nascimento, curso=None):
    if not nome or not nascimento:
        return "Parametros inválidos"

    c = {}
    aluno_objeto = Aluno(nome, nascimento)

    if curso:
        c = CURSOS.get("curso")
        c["alunos"].append(aluno_objeto)

    ALUNOS.append(aluno_objeto)

    return {
        "nome_aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.get("nome_curso")
    }

def listar_alunos():
    resposta = ""
    for aluno in ALUNOS:
        resposta += (f"Nome: {aluno.nome} \n"
                     f"Matricula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso} \n"
                     f"------------------------ \n")

    return resposta

