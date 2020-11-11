from flask import Flask, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

desenvolvedores=[
    {"id":0,"nome":"Adriano","habilidades":['Python','C++','VBA']},        # 1º posição
    {"id":1,"nome":"Samuel","habilidades":['html',"CSS","Java"]}  ]          # 2º posição

#Consulta, altera e deleta um desenvolvedor pela ID
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor de ID {} não existe".format(id)
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro não esperado, procure o administrador da API"
            response = {"status": "erro", "mensagem": mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status": "Sucesso", "mensagem": "Registro excluido."}

#Lista de todos os desenvolvedores
#Registra um novo desenvolvedor
class Programadores(Resource):
        def post(self):
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]
        def get(self):
            return desenvolvedores

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(Programadores, '/dev/')

if __name__ == '__main__':
    app.run()