from Aula_pratica_POO.models.aluno import Aluno
from Aula_pratica_POO.models.curso import Curso

CURSOS = {}     #simulação de banco de dados
ALUNOS = {}     #simulação de banco de dados

def cadastrar_aluno(nome, nascimento, nome_curso=None):       #não precisa de SELF pois está fora de uma classe
    if not nome or not nascimento:
        return "Parametros inválidos"

    c = None
    aluno_objeto = Aluno(nome, nascimento)

    if nome_curso:
        c = CURSOS.get(nome_curso)
        c.alunos[aluno_objeto.matricula] = aluno_objeto

    ALUNOS[aluno_objeto.matricula] = aluno_objeto

    return {
        "nome_aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.nome or None
    }

def listar_alunos():
    resposta = ""
    for aluno in ALUNOS.values():
        resposta += (f"Nome: {aluno.nome} \n"
                     f"Matricula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso.nome} \n"
                     f"------------------------ \n")

    return resposta

def detalhar_aluno(matricula):
    if not matricula:
        return "Paramentros inválidos"

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Este aluno não está cadastrado."

    return (f"Nome: {aluno.nome} \n"
            f"Matricula: {aluno.matricula} \n"
            f"Data de nascimento: {aluno.nascimento} \n"
            f"Data de ingresso: {aluno.ingresso} \n"
            f"Curso: {aluno.curso.nome or "Sem curso no momento"} \n"
            f"Notas: {aluno.notas}")

def deletar_aluno(matricula):
    if not matricula:
        return "Paramentros inválidos"

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Este aluno não está cadastrado."

    if aluno.curso:

        curso = CURSOS.get(aluno.curso.nome)
        curso.alunos.pop(matricula)

    ALUNOS.pop(matricula)               #.pop para excluir

    return "Aluno excluido com sucesso!"

