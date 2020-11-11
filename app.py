from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores=[
    {"nome":"Adriano","habilidades":['Python','C++','VBA']},        # 1º posição
    {"nome":"Samuel","habilidades":['html',"CSS","Java"]}            # 1º posição
                ]
#Consulta, altera e deleta um desenvolvedor pela ID
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor de ID {} não existe".format(id)
            response = {"status":"erro","mensagem":mensagem}
        except Exception:
            mensagem = "Erro não esperado, procure o administrador da API"
            response = {"status": "erro", "mensagem": mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"status":"Sucesso","mensagem":"Registro excluido."})

#Lista de todos os desenvolvedores
#Registra um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def programadores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({"status":"Sucesso", "mensagem":"Registrado com sucesso"})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)






if __name__ == '__main__':
    app.run(debug=True)