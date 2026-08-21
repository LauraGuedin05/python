from . import db
from .base import ModeloBase


class Cadastro(ModeloBase):
    __tablename__ = "cadastros"

    nome = db.Column(db.String(120), nullable=False)
    profissao = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    logradouro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    complemento = db.Column(db.String(100), default="")
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)

    CAMPOS_OBRIGATORIOS = (
        "nome", "profissao", "cep", "logradouro",
        "numero", "bairro", "cidade", "estado",
    )

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.nome).all()

    @classmethod
    def a_partir_de_dict(cls, informacoes):
        """Monta um Cadastro a partir de um dict (form HTML ou JSON da API)."""
        try:
            return cls(
                nome=str(informacoes["nome"]).strip(),
                profissao=str(informacoes["profissao"]).strip(),
                cep=str(informacoes["cep"]).strip(),
                logradouro=str(informacoes["logradouro"]).strip(),
                numero=str(informacoes["numero"]).strip(),
                complemento=str(informacoes.get("complemento", "")).strip(),
                bairro=str(informacoes["bairro"]).strip(),
                cidade=str(informacoes["cidade"]).strip(),
                estado=str(informacoes["estado"]).strip().upper(),
            )
        except (KeyError, ValueError, TypeError) as exc:
            nomes_campos = ", ".join(cls.CAMPOS_OBRIGATORIOS)
            raise ValueError(f"Campos obrigatórios: {nomes_campos}") from exc

    def atualizar_de_dict(self, informacoes):
        """Atualiza só os campos que vierem no dict."""
        for chave in self.CAMPOS_OBRIGATORIOS + ("complemento",):
            if chave in informacoes:
                conteudo = str(informacoes[chave]).strip()
                if chave == "estado":
                    conteudo = conteudo.upper()
                setattr(self, chave, conteudo)

    def endereco_completo(self):
        partes = [
            f"{self.logradouro}, {self.numero}",
            self.complemento,
            self.bairro,
            f"{self.cidade}/{self.estado}",
            f"CEP {self.cep}",
        ]
        return " — ".join(parte for parte in partes if parte)

    def para_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "profissao": self.profissao,
            "cep": self.cep,
            "logradouro": self.logradouro,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "endereco_completo": self.endereco_completo(),
            "data_criacao": str(self.data_criacao),
        }
