# Projeto Gerenciador de Tarefas - versão 2.0
# Desenvolvido por Nathali Cardoso | GitHub: github.com/Nathali-Cardoso
# Nesta versão foi adicionado o uso do JSON, listas e dicionários ao projeto.

import json
import sys

try: 
    with open("dados_tarefas.json", "r", encoding="utf-8") as arquivo:
        dados_tarefas = json.load(arquivo)

except (FileNotFoundError,  json.JSONDecodeError):
    dados_tarefas = {}
    
def menu_principal():
    formatacao_menu('menu principal')
    if not dados_tarefas:
        print('1 - Criar Categoria\n'
              '2 - Encerrar \n')
        while True: 
            try:
                separador()
                opcao = int(input('Opção: ').strip())
                if opcao == 1:
                    criar_categoria()
                elif opcao == 2:
                    encerrar()
                else:
                    print('Erro: dados inválidos.')
                    continue
            except ValueError:
                print('Erro: digite apenas números.')
                continue
    else:
        print('1 - Criar Categoria \n'
              '2 - Criar Tarefa \n'
              '3 - Concluir Tarefa \n'
              '4 - Editar Categoria \n'
              '5 - Excluir Tarefa \n'
              '6 - Excluir Categoria \n'
              '0 - Encerrar')
        while True:
            try:
                separador()
                opcao = int(input('Opção: ').strip())
                if opcao == 1:
                    criar_categoria()
                elif opcao == 2:
                    criar_tarefa()
                elif opcao == 3:
                    concluir_tarefa()
                elif opcao == 4:
                    editar_categoria()
                elif opcao == 5:
                    excluir_tarefa()
                elif opcao == 6:
                    excluir_categoria()
                elif opcao == 0:
                    encerrar()
                else:
                    print('Erro: dados inválidos')
                
            except ValueError:
                print('Erro: digite apenas números.')
                continue    

def retornar_menu():
    while True:
        print('Você deseja: \n'
              '1 - Retornar ao Menu Principal \n'
              '2 - Encerrar')
        try:
            opcao = int(input('Opção: ').strip())
            if opcao == 1:
                menu_principal()
            elif opcao == 2:
                encerrar()
            else:
                print('Erro: opção inválida.')
                continue
        except ValueError:
            print('Erro: dados inválidos.')
            continue  

def formatacao_menu(texto):
    largura = 70
    print('=' * largura )
    print(texto.upper().center(largura))
    print('=' * largura)

def encerrar():
    separador()
    print('Encerrando o programa...\n'
          'Até breve!')
    sys.exit(0)

def separador():
    largura = 70
    print('-' * largura)

def salvar_dados():
    with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)

def criar_categoria():
    formatacao_menu('criar categoria')
    while True:
        try:
            categoria = input('Digite o nome da categoria: ').lower()
            if not categoria.strip():
                print('Erro: categoria não pode estar vazia.')
                continue
            
            elif categoria not in dados_tarefas:
                    dados_tarefas[categoria] = []
                
                    with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
                        json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)
                    
                    separador()
                    print('Categoria adicionada com sucesso!')
                     
                    while True:    
                        try:
                            separador()
                            option = int(input('1 - Voltar ao menu\n'
                                            '2 - Encerrar\n'
                                            'Insira uma opção: ').strip())
                            if option == 1:
                                menu_principal()
                            
                            elif option == 2:
                                encerrar()
                                
                            else:
                                separador()
                                print('Erro: opção inválida.')
                                continue

                        except ValueError:
                            separador()
                            print('Erro: digite apenas números.')
            
            else:
                print('Erro: categoria já existe!')
                continue
        
        except ValueError:
            print('Erro: dados inválidos.')
            continue
        
def criar_tarefa():
    formatacao_menu('criar tarefa')
    print('Categorias:')
    for c in dados_tarefas:
        print(f'- {c}')
    
    while True:
        try:
            esc_cat = input('Escolha a categoria para adicionar a tarefa: ').lower()            
            if not esc_cat.strip():
                print('Erro: dados inválidos - campo vazio.')
                continue
            elif esc_cat not in dados_tarefas:
                print('Erro: dados inválidos - categoria não existe.')
                continue
            else:
                print('Dados da nova tarefa:')
                while True:
                    try:
                        descricao = input('Descrição da tarefa: ').lower()
                        if not descricao.strip():
                            print('Erro: descrição não pode estar em branco.')
                            continue
                        else:
                            nova_tarefa = {
                                "descrição" : descricao,
                                "conclusão" : "pendente"
                            }
                            dados_tarefas[esc_cat].append(nova_tarefa)
                            salvar_dados()
                            print('\nTarefa adicionada com sucesso!')
                            separador()
                            retornar_menu()
                    except ValueError:
                        print('Erro: dados inválidos.')
                        continue
        except ValueError:
            print('Erro: dados inválidos.')
  
def excluir_tarefa(): 
    formatacao_menu('excluir tarefa')
    print('Categorias:')   
    for categoria in dados_tarefas:
        print(f'- {categoria}') 
    while True:
        try: 
            loc_categoria = input('\nEm qual categoria esta tarefa está localizada: ').lower()
            if not loc_categoria.strip():
                print('Erro: dados inválidos - campo vazio.')
                continue
            
            elif loc_categoria in dados_tarefas:
                print('Categoria localizada!')
                separador()
                
                print(f'Categoria: {loc_categoria}\n'
                      'Tarefas: ')
                for indice, tarefa in enumerate(dados_tarefas[loc_categoria], start=1):
                    print(f'Tarefa {indice}: {tarefa["descrição"]} - conclusão: {tarefa["conclusão"]}')
                
                separador()   
                while True:
                    try:
                        exc_tarefa = input('Insira o nome da tarefa que deseja excluir: ').lower()
                        if not exc_tarefa.strip():
                            print('Erro: dados inválidos - campo vazio.')
                            continue
                        
                        else:
                            for tarefa in dados_tarefas[loc_categoria]:
                                if tarefa["descrição"] == exc_tarefa:
                                    dados_tarefas[loc_categoria].remove(tarefa) 
                                    salvar_dados()        
                                    print(f'Tarefa: {exc_tarefa}, excluída com sucesso!')
                                    retornar_menu()
                                else:
                                    print('Erro: tarefa não existe.')
                                    continue
                                
                    except ValueError:
                        print('Erro: dados inválidos.')
                        continue 
            else:
                print('Erro: categoria não existe.')
                continue

        except ValueError:
            print('Erro: dados inválidos.')
            continue

def excluir_categoria():
    formatacao_menu('excluir categoria')
    
    print('Atenção: este procedimento é irreversível.\n'
          'Executá-lo fará a exclusão permanente da categoria e de todas as \ntarefas nela contidas.')
    
    separador()
    print('Categoria(s):')
    for categoria in dados_tarefas:
        print(f'- {categoria}')
        
    while True:     
        try:
            separador()
            esc_cat = input('Nome da categoria que deseja excluir: ').lower()
            if not esc_cat.split():
                print('Erro: dados inválidos - campo vazio.')
                continue
            
            elif esc_cat in dados_tarefas:
                separador()
                
                while True:
                    try:    
                        continuar = int(input(f'Deseja realmente realizar a exclusão da categoria {esc_cat}? [1-sim|2-não]: ').strip())
                        if continuar == 1:
                            del dados_tarefas[esc_cat]
                            salvar_dados()
                            print('Categoria excluída com sucesso.')
                            retornar_menu()
                        elif continuar == 2:
                            retornar_menu()
                        else:
                            print('Erro: opção inválida.')
                            continue
                        
                    except ValueError:
                        print('Erro: dados inválidos - insira apenas números.')
                        continue
            else:
                print('Erro: categoria não localizada.')
                continue
            
        except ValueError:
            print('Erro: dados inválidos.')

def concluir_tarefa():
    formatacao_menu('concluir tarefa')
    print('Categorias:')
    for categoria in dados_tarefas:
        print(f'- {categoria}')
    
    separador()
    while True:
        try:        
            loc_cat = input('Em qual categoria a tarefa está localizada?: ').lower()
            if not loc_cat.strip():
                print('Erro: dados inválidos - campo vazio.')
                continue
            
            elif loc_cat in dados_tarefas:
                separador()
                print(f'Categoria:{loc_cat}\n'
                      'Tarefas:')
                for tarefa in dados_tarefas[loc_cat]:
                    print(f'- {tarefa["descrição"]}')
                    
                separador()  
                while True:
                    try:
                        ed_tarefa = input('Qual tarefa deseja concluir?: ').lower()
                        if not ed_tarefa.strip():
                            print('Erro: dados inválidos - campo vazio.')
                            continue
                        
                        else:
                            for tarefa in dados_tarefas[loc_cat]:
                                if tarefa["descrição"] == ed_tarefa:
                                    tarefa["descrição"] = 'concluído'  
                                    salvar_dados()                                      
                                    print('\nTarefa atualizada.')
                                    
                                    ##adicionar opção para concluir mais de 1 tarefa
                                    retornar_menu()     
                                else:
                                    print('Erro: tarefa não localizada.')        
                                    continue
            
                    except ValueError:
                        print('Erro: dados inválidos.')
                        continue
            else:
                print('Erro: categoria não localizada.') 
                continue
        except ValueError:
            print('Erro: dados inválidos.')
            continue
         
def editar_categoria():
    formatacao_menu('editar categoria')
    print('Categorias:')
    for categoria in dados_tarefas:
        print(f'- {categoria}')
    
    while True:
        try:    
            edi_categoria = input('Qual categoria deseja editar: ').lower()
            if not edi_categoria.strip():
                print('Erro: dados inválidos - campo vazio.')
                continue
            else:     
                for categoria in dados_tarefas:
                    if categoria == edi_categoria:
                        while True:
                            try:
                                novo_nome_cat = input('Novo nome da categoria: ').lower()
                                if not novo_nome_cat.strip():
                                    print('Erro: nome da categoria não pode estar em branco.')
                                    continue    
                                else:
                                    dados_tarefas[novo_nome_cat] = dados_tarefas.pop(edi_categoria)
                                    salvar_dados()
                                    print('Nome da categoria atualizado com sucesso.')
                                    separador()
                                    retornar_menu()
                            except ValueError:
                                print('erro: dados inválidos.')
                                continue
                    else:
                        print('Erro: categoria não encontrada.')
                        continue
        except ValueError:
            print('Erro: dados inválidos.')
            continue           

menu_principal()