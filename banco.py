import oracledb

def get_conexao():
    return oracledb.connect(user="RM559999", password="Fiap#2025", dsn="oracle.fiap.com.br/orcl")

def recupera_perguntas_enquete(enquete_id: int) -> list:
    sql = "select p.id, p.numero, p.questao, p.tipo, i.nome from tb_pergunta p  left join tb_item i on p.id = i.pergunta_id where p.enquete_id = :enquete order by p.numero"


    with get_conexao() as conn:
        with conn.cursor() as cur:
            param = {"enquete": enquete_id}
            cur.execute(sql, param) 
            dados = cur.fetchall()
            
        return dados
    
if __name__ == "__main__":
    perguntas = recupera_perguntas_enquete(1)
    for quest in perguntas:
        print(quest)