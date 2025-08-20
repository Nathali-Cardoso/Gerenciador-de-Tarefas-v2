# Projeto Gerenciador de Tarefas - versão 2.0
# Desenvolvido por Nathali Cardoso | GitHub: github.com/Nathali-Cardoso
# Nesta versão foi adicionado o uso do JSON, listas e dicionários ao projeto.

import json

try: 
    with open("dados_tarefas.json", "r", encoding="utf-8") as arquivo:
        dados_tarefas = json.load(arquivo)

except (FileNotFoundError,  json.JSONDecodeError):
    dados_tarefas = {}

def criar_categoria():
    categoria = input('Digite o nome da categoria: ')
    
    if categoria not in dados_tarefas:
        dados_tarefas[categoria] = []
        
        with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)
        
    else:
        print('Erro: categoria já existe!')
        
def criar_tarefa():
    for c in dados_tarefas:
        print(c)
    
    esc_cat = input('Primeiro escolha uma categoria acima: ')
    print('Categoria selecionada com sucesso!')    
    
    novo_id = max(t["id"] for t in dados_tarefas[esc_cat]) + 1 if dados_tarefas[esc_cat] else 1
    
    nova_tarefa = {
        "id" : novo_id,
        "descrição" : input('Descrição da tarefa:'),
        "conclusão" : "pendente"
    }
    
    dados_tarefas[esc_cat].append(nova_tarefa)
    
    with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)
    
    print('Tarefa adicionada com sucesso!')
    
def excluir_tarefa():    
    for categoria in dados_tarefas:
        print(categoria)
        
    loc_categoria = input('Em qual categoria esta tarefa está localizada: ')
    if loc_categoria in dados_tarefas:
        print('Categoria localizada!')
        
        for indice, tarefa in enumerate(dados_tarefas[loc_categoria], start=1):
            print(f'Tarefa {indice}: {tarefa["descrição"]} - conclusão: {tarefa["conclusão"]}')
                            
        exc_tarefa = input('Insira o nome da tarefa que deseja excluir: ')
        
        for tarefa in dados_tarefas[loc_categoria]:
            if tarefa["descrição"] == exc_tarefa:
                dados_tarefas[loc_categoria].remove(tarefa) 
                
                with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
                    json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)
                
                print(f'Tarefa: {exc_tarefa}, excluída com sucesso!')

            else:
                print('Erro: tarefa não localizada!')
    else:
        print('Erro: Categoria não localizada!')

def excluir_categoria():
    print('Atenção: este procedimento é permanente.\n'
          'Fará a exclusão da categoria e de todas das tarefas nela contidas!!')
    
    print('Categoria(s):')
    for categoria in dados_tarefas:
        print(categoria)
    esc_cat = input('Insira o nome da categoria que deseja excluir permanentemente: ')
    if esc_cat in dados_tarefas:
        del dados_tarefas[esc_cat]
        
        with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)
        
        print('Categoria excluída com sucesso!')

    else:
        print('Erro: categoria não localizada.')

def editar_tarefa():
    for categoria in dados_tarefas:
        print(categoria)
    
    loc_cat = input('Em qual categoria a tarefa está localizada?: ')
    
    if loc_cat in dados_tarefas:
        print('Categoria localizada!')
        
        print(f'Categoria:{loc_cat} - Tarefas:')
        for tarefa in dados_tarefas[loc_cat]:
            print(tarefa["descrição"])
        editar_tar = input('Qual tarefa deseja editar?: ')
        for tarefa in dados_tarefas[loc_cat]:
            if tarefa["descrição"] == editar_tar:
                print('Alteração de dados:')
                tarefa["descrição"] = input('Nova descrição da tarefa: ')
                tarefa["concluido"] = input('Conclusão: ')
                print('Alterações realizadas com sucesso!')
                
                with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
                    json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)
                
                break               
            else:
                print('Erro: tarefa não localizada.')        
     
    else:
        print('Erro: categoria não localizada.')
        
        
def editar_categoria():
    print('Categorias:')
    for categoria in dados_tarefas:
        print(categoria)
        
    edi_cat = input('Qual categoria deseja editar: ')
    for categoria in dados_tarefas:
        if categoria == edi_cat:
            novo_nome_cat = input('Novo nome da categoria: ')
            dados_tarefas[novo_nome_cat] = dados_tarefas.pop(edi_cat)
            
            with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)
            
            break
        else:
            print('Erro: categoria não encontrada.,')
            
        
