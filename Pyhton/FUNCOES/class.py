class curso():
    def __init__(self, id_curso, nome_curso, carga_hor_curso):
        self.id_curso = id_curso
        self.nome_curso = nome_curso
        self.carga_hor_curso = carga_hor_curso

    def setId(self, id_curso):
        self.id_curso = id_curso
    def setNome(self, nome_curso):
        self.nome_curso = nome_curso
    def setCgHoraria(self, carga_hor_curso):
        self.carga_hor_curso = carga_hor_curso
    
    def imprimeInfos(self):
        print("<<<<<DADOS DO CURSO>>>>>")
        print("ID do curso", self.id_curso)
        print("Nome do curso: ", self.nome_curso)
        print("Carga Horaria: ", self.carga_hor_curso, "hs")
       

curso = curso(20212050, "Orientação a objetos", 160)

curso.imprimeInfos()