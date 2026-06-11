from flask import Flask, request, jsonify
import oracledb
from datetime import datetime

app = Flask(__name__)

# ====================================================================
# CONFIGURAÇÕES DO BANCO ORACLE CLOUD
# Substitua as informações abaixo pelas suas credenciais reais
# ====================================================================
USUARIO = "RM567778"
SENHA = "180680"

# Suas informações de conexão
HOST = "oracle.fiap.com.br"
PORTA = 1521  # 1521 é a porta padrão do Oracle. 
SID = "ORCL"

# O Python cria o DSN perfeitamente formatado para você!
DSN = oracledb.makedsn(host=HOST, port=PORTA, sid=SID)

def conectar_banco():
    """Cria a conexão com a Oracle Cloud e retorna o objeto de conexão"""
    try:
        conexao = oracledb.connect(user=USUARIO, password=SENHA, dsn=DSN)
        return conexao
    except Exception as e:
        print(f"Erro ao conectar no banco: {e}")
        return None

# ====================================================================
# ROTA DA API (O Guichê de Recepção)
# ====================================================================
@app.route('/api/dados-feijao', methods=['POST'])
def receber_dados():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado recebido"}), 400

    # Extraindo os valores do JSON
    n = dados.get('nitrogenio')
    p = dados.get('fosforo')
    k = dados.get('potassio')
    ph = dados.get('ph')
    umidade = dados.get('umidade')
    bomba = dados.get('bomba_ativa')
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(f"\n[{agora}] 🟢 DADOS RECEBIDOS! Tentando salvar na nuvem...")

    # Abrindo conexão com o banco
    conexao = conectar_banco()
    
    if conexao:
        try:
            # O Cursor é o "carteiro" que leva o comando SQL para o banco
            cursor = conexao.cursor()
            
            # Comando SQL de inserção
            sql = """
                INSERT INTO tb_leitura_sensores (nitrogenio, fosforo, potassio, ph, umidade, bomba_ativa) 
                VALUES (:1, :2, :3, :4, :5, :6)
            """
            
            # Executando o comando passando as variáveis do sensor
            cursor.execute(sql, [n, p, k, ph, umidade, bomba])
            
            # Confirmando a transação (salvando de fato no cofre)
            conexao.commit()
            
            print("🚀 SUCESSO! Dados inseridos na Oracle Cloud.")
            cursor.close()
            conexao.close()
            
            return jsonify({"status": "sucesso", "mensagem": "Salvo no Oracle!"}), 200

        except Exception as e:
            print(f"⚠️ Erro ao inserir dados: {e}")
            return jsonify({"erro": "Falha ao salvar no banco"}), 500
    else:
        return jsonify({"erro": "Banco de dados offline"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)