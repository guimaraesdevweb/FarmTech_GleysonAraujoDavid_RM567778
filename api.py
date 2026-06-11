# ====================================================================
# API DE RECEPÇÃO DE DADOS (O "Guichê")
# Instale o Flask antes usando no terminal: pip install flask
# ====================================================================

from flask import Flask, request, jsonify
from datetime import datetime

# Inicia o aplicativo Flask
app = Flask(__name__)

# Criamos uma "rota" (o endereço que o ESP32 vai chamar)
# O método 'POST' significa que esta rota serve para RECEBER dados
@app.route('/api/dados-feijao', methods=['POST'])
def receber_dados():
    # 1. A API recebe o "pacote" JSON que o ESP32 enviou
    dados = request.get_json()

    # 2. Se o pacote estiver vazio, retorna um erro
    if not dados:
        return jsonify({"erro": "Nenhum dado recebido"}), 400

    # 3. Extraímos os dados do JSON para variáveis no Python
    n = dados.get('nitrogenio')
    p = dados.get('fosforo')
    k = dados.get('potassio')
    ph = dados.get('ph')
    umidade = dados.get('umidade')
    bomba = dados.get('bomba_ativa')
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 4. Imprime no terminal do VSCode para você ver chegando em tempo real!
    print(f"\n[{agora}] 🟢 NOVOS DADOS RECEBIDOS DO CAMPO:")
    print(f"NPK: {n}-{p}-{k} | pH: {ph} | Umidade: {umidade}% | Bomba: {'LIGADA' if bomba else 'DESLIGADA'}")

    # ==============================================================
    # AQUI ENTRARÁ O CÓDIGO DO BANCO DE DADOS ORACLE NO FUTURO
    # Exemplo do que faremos depois:
    # cursor.execute("INSERT INTO tb_leitura (data, n, p, k, ph, umidade) VALUES (...)", (agora, n, p, k, ph, umidade))
    # db.commit()
    # ==============================================================

    # 5. A API responde ao ESP32 que deu tudo certo (Código 200)
    return jsonify({"status": "sucesso", "mensagem": "Dados salvos na nuvem!"}), 200

# Executa o servidor na porta 5000
if __name__ == '__main__':
    # O host='0.0.0.0' permite que a API receba acessos externos
    app.run(host='0.0.0.0', port=5000, debug=True)