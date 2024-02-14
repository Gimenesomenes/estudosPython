import sqlite3

# Conectar ao banco
conexao = sqlite3.connect('banco')

cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT')

#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(01, "Carolina Gimenes Oliveira", "Ribeirão Preto", "carol@gmail.com", 97863920)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(02, "Lucas Bento", "Ribeirão Preto", "lucas@gmail.com", 90190983)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(03, "Isabela Tiezzi", "Ribeirão Preto", "isabela@gmail.com", 977643829)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(04, "Jéssica Lizar", "São Vicente", "jessica@gmail.com", 78693920)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(05, "Marcio França", "São Paulo", "marcio@gmail.com", 632997654)')

#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(8, "Cynthia", "Inglaterra", "cy@gmail.com")')

#cursor.execute('DELETE FROM gerentes where id=8')
#

# ORDER BY e DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY id DESC')

# LIMIT e DISTINCT

#dados = cursor.execute('SELECT DISTINCT * FROM usuario ')

#GROUP BY e HAVING

#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')

#JOIN's
#JOIN - INNER JOIN
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# LEFT JOIN
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

# RIGHT JOIN

#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')

# FULL JOIN

dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')
for usuario in dados:
    print(usuario)
#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" where nome="Marcio França"')

#cursor.execute('DROP TABLE produtos')
# As informações vão ser enviadas 
conexao.commit()

# A conexão será encerrada 
conexao.close