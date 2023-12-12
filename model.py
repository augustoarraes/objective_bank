from init import db
from sqlalchemy_serializer import SerializerMixin
import datetime, pytz


class ContaModel(db.Model, SerializerMixin):
    __tablename__ = 'OBJ_CONTA'

    id = db.Column(db.Integer(), primary_key=True)
    conta_id = db.Column(db.Integer())
    saldo = db.Column(db.Double())
    user_fk = db.Column(db.Integer()) # ... implementação futura
    is_active = db.Column(db.Boolean())
    created = db.Column(db.Date())

    def __init__(self, conta_id, saldo=0):
        self.conta_id = conta_id
        self.saldo = saldo
        self.created = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S.%f")
        self.is_active = True

    def __repr__(self):
        return f"<Conta {self.conta_id} - saldo: {self.saldo}>"


class ExtratoModel(db.Model):
    __tablename__ = 'OBJ_EXTRATO'

    id = db.Column(db.Integer(), primary_key=True)
    conta_fk = db.Column(db.Integer())
    forma_pgto = db.Column(db.String())
    saldo_anterior = db.Column(db.Double())
    saldo_pos_transacao = db.Column(db.Double())
    updated = db.Column(db.Date())

    def __init__(self, conta_fk, forma_pgto, saldo_anterior, saldo_pos_transacao):
        self.conta_fk = conta_fk
        self.forma_pgto = forma_pgto
        self.saldo_anterior = saldo_anterior
        self.updated = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S.%f")
        self.saldo_pos_transacao = saldo_pos_transacao


class UserModel(db.Model): # ... implementação futura
    __tablename__ = 'OBJ_USER'

    id = db.Column(db.Integer(), primary_key=True)
    senha = db.Column(db.String())
    ultimo_login = db.Column(db.DateTime())
    username = db.Column(db.String())
    nome = db.Column(db.String())
    sobrenome = db.Column(db.String())
    email = db.Column(db.String())
    is_active = db.Column(db.Boolean())
    created = db.Column(db.DateTime())
    log_user = db.Column(db.String())

    def __init__(self, senha, username, nome, sobrenome, email, log_user):
        self.senha = senha
        self.username = username
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.created = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S.%f")
        self.log_user = log_user
        self.is_active = True


class HashModel(db.Model):
    __tablename__ = 'OBJ_HASH'

    id = db.Column(db.Integer(), primary_key=True)
    hash = db.Column(db.String())
    date = db.Column(db.DateTime)

    def __init__(self, hash):
        self.date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S.%f")
        self.hash = hash

    def __repr__(self):
        return f"<Data {self.date}>"