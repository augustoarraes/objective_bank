import binascii, datetime, json, os, jwt
from flask import Response, jsonify, make_response
from sqlalchemy import and_, or_
from model import (ContaModel, ExtratoModel, UserModel, HashModel, db)
import constants


"""
Principais Métodos, Regras de Negócio
"""

def set_contaBN(data):
    nova_conta = ContaModel(data["conta_id"], data["valor"])
    db.session.add(nova_conta)
    db.session.commit()
    return data, 201


def get_contaBN(id):
    conta = ContaModel.query.filter(ContaModel.conta_id==id).first()
    if conta:
        return conta.to_dict(), 200
    else:
        return {}, 404
    

def transacaoBN(data):
    conta = ContaModel.query.filter(ContaModel.conta_id==data["conta_id"]).first()
    if conta.saldo > 0 and data["valor"] < conta.saldo:
        conta.saldo = conta.saldo - operacao(data)
        db.session.commit()
        return conta.to_dict(), 200
    else:
        return {}, 404
    

def operacao(data):
    return data["valor"] * (1+constants.taxas.get(data["forma_pagamento"])/100)


#def extratoBN(id): .... implementação futura