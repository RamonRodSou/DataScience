# São operadores uitilizados para comparar se os dois objetos testados ocupam a mesma posição na memmória

curso = "Curso de Python"
nome_curso = curso

print(id(curso))
print(id(nome_curso))

print(curso is nome_curso) # esta na mesma regiao da memoria ( apontando para o mesmo endereco/ referencia)
print(curso is not nome_curso) # se esta apontando para enderecos diferentes