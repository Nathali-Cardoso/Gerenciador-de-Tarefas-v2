from colorama import Fore, Back, Style, init
import json
import sys
init(autoreset=True)

# FUNÇÕES DE ARMAZENAMENTO
try: 
    with open("dados_tarefas.json", "r", encoding="utf-8") as arquivo:
        dados_tarefas = json.load(arquivo)

except (FileNotFoundError,  json.JSONDecodeError):
    dados_tarefas = {}
    
def salvar_dados():
    with open("dados_tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados_tarefas, arquivo, indent=4, ensure_ascii=False)


# FUNÇÕES DE EDIÇÃO / CATEGORIA
def criar_categoria():
    formatacao_menu('criar categoria')
    while True:
        categoria = input('Digite o nome da nova categoria: ').lower().strip()
        if not categoria.strip():
            print('Erro: este campo não pode estar vazio.')
            separador()
            continue
        elif categoria not in dados_tarefas:
                dados_tarefas[categoria] = []
                salvar_dados()
                print('\nCategoria adicionada com sucesso!')
                retornar_menu()
        else:
            print('Erro: categoria já existe!')
            separador()
            continue

def editar_categoria():
    formatacao_menu('editar categoria')
    print('CATEGORIAS:')
    for categoria in dados_tarefas:
        print(f'- {categoria}')
    while True:
        separador()    
        edi_categoria = input('Categoria: ').strip().lower()
        if not edi_categoria.strip():
            print('Erro: este campo não pode estar vazio.')
            continue
        elif edi_categoria in dados_tarefas:
            print('Categoria selecionada com sucesso.')
            while True:
                separador()
                novo_nome_cat = input('Novo nome: ').strip().lower()
                if not novo_nome_cat.strip():
                    print('Erro: nome da categoria não pode estar em branco.')
                    continue    
                else:
                    dados_tarefas[novo_nome_cat] = dados_tarefas.pop(edi_categoria)
                    salvar_dados()
                    print('Nome atualizado com sucesso!')
                    retornar_menu()
        else:
            print('Erro: categoria não localizada.')
            continue                    

def excluir_categoria():
    formatacao_menu('excluir categoria')
    print('Atenção: este procedimento é irreversível.\n'
          'Executá-lo fará a exclusão permanente da categoria e de todas as \ntarefas nela contidas.')
    separador()
    print('CATEGORIAS:')
    for categoria in dados_tarefas:
        print(f'- {categoria}')
    while True:     
        separador()
        esc_cat = input('Nome da categoria que deseja excluir: ').strip().lower()
        if not esc_cat.split():
            print('Erro: este campo não pode estar vazio')
            continue
        elif esc_cat in dados_tarefas:
            while True:
                try:    
                    separador()
                    continuar = int(input(f'Deseja realmente realizar a exclusão da categoria {esc_cat}? \n'
                                            '1 - sim \n'
                                            '2 - não \n\n'
                                            'Opção: ').strip())
                    if continuar == 1:
                        del dados_tarefas[esc_cat]
                        salvar_dados()
                        print(f'\nCategoria: {esc_cat}, excluída com sucesso!')
                        retornar_menu()
                    elif continuar == 2:
                        print('\nProcedimento cancelado.')
                        retornar_menu()
                    else:
                        print('Erro: opção fora da lista. Escolha um número válido.')
                        continue  
                except ValueError:
                    print('Erro: insira apenas números.')
                    continue
                except Exception:
                    print('Ocorreu um erro inesperado. Tente novamente. ')
                    continue
        else:
            print('Erro: categoria não localizada.')
            continue

def visualizar_categorias():
    formatacao_menu('lista de categorias')
    for quant, categoria in enumerate(dados_tarefas, start=1):
        print(f'{quant} - {categoria}')
    retornar_menu()

# FUNÇÕES DE EDIÇÃO / TAREFAS        
def criar_tarefa():
    formatacao_menu('criar tarefa')
    print('CATEGORIAS:')
    for c in dados_tarefas:
        print(f'- {c}')
    while True:
        separador()
        esc_cat = input('Categoria: ').strip().lower()            
        if not esc_cat.strip():
            print('Erro: este campo não pode estar vazio.')
            continue
        elif esc_cat in dados_tarefas:
            print(f'\nCategoria: {esc_cat}, selecionada com sucesso.')
            while True:
                separador()
                descricao = input('Descrição da tarefa: ').strip().lower()
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
                    while True:
                        try:
                            separador()
                            outra_tarefa = int(input('Você quer: \n'
                                                        '1 - Criar outra Tarefa \n'
                                                        '2 - Visualizar as Tarefas \n'
                                                        '3 - Retornar ao Menu Principal \n'
                                                        '0 - Sair \n\n'
                                                        'Opção: ').strip())
                            if outra_tarefa == 1:
                                criar_tarefa()
                            elif outra_tarefa == 2:
                                visualizar_tarefas()
                            elif outra_tarefa == 3:
                                menu_principal()
                            elif outra_tarefa == 0:
                                encerrar()
                            else:
                                print('Erro: opção fora da lista. Escolha um número válido.')
                                continue
                        except ValueError:
                            print('Erro: digite apenas números.')
                            continue
                        except Exception:
                            print('Ocorreu um erro inesperado. Tente novamente.')  
                            continue
        else:
            print('Erro: categoria não existe.')
            continue

def concluir_tarefa():
    formatacao_menu('concluir tarefa')
    print('CATEGORIAS:')
    for categoria in dados_tarefas:
        print(f'- {categoria}')
    print('Digite o nome da categoria abaixo:')   
    while True:
        separador()
        loc_cat = input('Categoria: ').strip().lower()
        if not loc_cat.strip():
            print('Erro: este campo não pode estar vazio.')
            continue
        elif loc_cat in dados_tarefas:
            pendentes = [t for t in dados_tarefas[loc_cat] if t["conclusão"] == "pendente"]    
            if not pendentes:
                print('\nTodas as tarefas desta categoria foram concluídas.\nParabéns!')
                retornar_menu()
            else:
                print('\nLista de tarefas:')
                for tarefa in dados_tarefas[loc_cat]:
                    print(f'- {tarefa["descrição"]}')
                while True:
                    separador()
                    ed_tarefa = input('Qual tarefa deseja concluir?: ').strip().lower()
                    if not ed_tarefa.strip():
                        print('Erro: este campo não pode estar vazio.')
                        continue
                    for tarefa in dados_tarefas[loc_cat]:
                        if tarefa["descrição"] == ed_tarefa:
                            if tarefa["conclusão"] == "concluído":
                                print('\nEsta tarefa já foi concluída.')
                                retornar_menu()
                            else:
                                tarefa["conclusão"] = "concluído"
                                salvar_dados()                                      
                                print(f'\nTarefa: {ed_tarefa}, concluída com sucesso!')
                                while True:
                                    try:
                                        separador()
                                        outra_tarefa = int(input('Você quer: \n'
                                                                '1 - Concluir outra Tarefa \n'
                                                                '2 - Retornar ao Menu Principal \n'
                                                                '3 - Sair \n'
                                                                'Opção: ').strip())
                                        if outra_tarefa == 1:
                                            concluir_tarefa()
                                        elif outra_tarefa == 2:
                                            menu_principal()
                                        elif outra_tarefa == 3:
                                            encerrar()
                                        else:
                                            print('Erro: opção fora da lista. Escolha um número válido.')
                                            continue
                                    except ValueError:
                                        print('Erro: digite apenas números.')    
                                        continue                      
                            break
                    else:
                        print('Tarefa não lozalizada.')
                        continue      
        else:
            print('Erro: categoria não localizada.') 
            continue

def excluir_tarefa(): 
    formatacao_menu('excluir tarefa')
    print('CATEGORIAS:')   
    for categoria in dados_tarefas:
        print(f'- {categoria}') 
    while True:
        separador()
        loc_categoria = input('Categoria: ').strip().lower()
        if not loc_categoria.strip():
            print('Erro: este campo não pode estar vazio.')
            continue
        elif loc_categoria in dados_tarefas:
            print('\nCategoria localizada!')
            separador()
            print(f'CATEGORIA: {loc_categoria}\n\n'
                    'Tarefas: ')
            for tarefa in dados_tarefas[loc_categoria]:
                print(f'nome: {tarefa["descrição"]} - conclusão: {tarefa["conclusão"]}')
            while True:
                separador()
                exc_tarefa = input('Insira o nome da tarefa que deseja excluir: ').strip().lower()
                if not exc_tarefa.strip():
                    print('Erro: este campo não pode estar vazio.')
                    continue
                else:
                    for tarefa in dados_tarefas[loc_categoria]:
                        if tarefa["descrição"] == exc_tarefa:
                            dados_tarefas[loc_categoria].remove(tarefa) 
                            salvar_dados()        
                            print(f'\nTarefa: {exc_tarefa}, excluída com sucesso!')
                            retornar_menu()
                    else:
                        print('Erro: tarefa não localizada.')
                        continue
        else:
            print('Erro: categoria não existe.')
            continue

def visualizar_tarefas():
    formatacao_menu('tarefas')
    print('Categorias: ')
    for categoria in dados_tarefas:
        print(f'- {categoria}')
    while True:    
        separador()
        sel_categoria = input('Digite o nome da categoria: ').strip()
        if not sel_categoria.strip():
            print('Erro: este campo não pode estar vazio.')
            continue
        elif sel_categoria not in dados_tarefas:
            print('Erro: categoria não localizada.')
            continue
        else:
            while True:
                try:
                    separador()
                    opcao = int(input('Você quer visualizar: \n'
                                        '1 - Tarefas Pendentes \n'
                                        '2 - Tarefas Concluídas \n'
                                        '3 - Todas as Tarefas \n'
                                        '4 - Retornar ao Menu Principal \n'
                                        'Opção: ').strip()) 
                    if opcao == 1:
                        formatacao_menu('tarefas pendentes')
                        for tarefa in dados_tarefas[sel_categoria]:
                            if tarefa["conclusão"] == "pendente":    
                                print(f'nome: {tarefa["descrição"]}\n'
                                      f'conclusão: {tarefa["conclusão"]}')
                                separador()
                        retornar_menu()
                    elif opcao == 2:
                        formatacao_menu('tarefas concluídas')
                        for tarefa in dados_tarefas[sel_categoria]:
                            if tarefa["conclusão"] == "concluído":    
                                print(f'nome: {tarefa["descrição"]}\n'
                                      f'conclusão: {tarefa["conclusão"]}')
                                separador()
                        retornar_menu()
                    elif opcao == 3:
                        formatacao_menu('todas as tarefas')
                        for tarefa in dados_tarefas[sel_categoria]:    
                            print(f'nome: {tarefa["descrição"]}\n'
                                  f'conclusão: {tarefa["conclusão"]}')
                            separador()
                        retornar_menu()
                    elif opcao == 4:
                        menu_principal()
                    else:
                        print('Erro: opção fora da lista. Escolha um número válido.')
                        continue
                except ValueError:
                    print('Erro: digite apenas números.')    
                    continue
                except Exception:
                    print('Ocorreu um erro inesperado. Tente novamente.')
                    continue        
                    

#FUNÇÃO DE ENCERRAMENTO DO PROGRAMA
def encerrar():
    separador()
    print('Encerrando o programa...\n'
          'Até breve!')
    sys.exit(0)


# FUNÇÕES DE CONTROLE DE MENU
def retornar_menu():
    while True:
        try:
            separador()
            opcao = int(input('Você deseja: \n'
                                '1 - Retornar ao Menu Principal \n'
                                '2 - Encerrar \n\n'
                                'Opção: ').strip())
            if opcao == 1:
                menu_principal()
            elif opcao == 2:
                encerrar()
            else:
                print('Erro: opção fora da lista. Escolha um número válido.')
                continue
        except ValueError:
            print('Erro: digite apenas números.')
            continue 
        except Exception:
            print('Ocorreu um erro inesperado. Tente novamente.')
            continue
        
def menu_principal():
    if not dados_tarefas:
        formatacao_menu('menu principal')
        while True:
            try:
                opcao = int(input('1 - Criar Categoria \n'
                                  '2 - Sair \n\n'
                                  'Opção: ').strip())
                if opcao == 1:
                    criar_categoria()
                elif opcao == 2:
                    encerrar()
                else:
                    print('Erro: opção fora da lista. Escolha um número válido.')
                    separador()
                    continue
            except ValueError:
                print('Erro: digite apenas números.')
                separador()
                continue
            except Exception:
                print('Ocorreu um erro inesperado. Tente novamente.')
                separador()
                continue
    else:
        formatacao_menu('menu principal')
        while True:
            try:
                opcao = int(input('1 - Categorias \n'
                                  '2 - Tarefas \n'
                                  '3 - Sair \n\n'
                                  'Opção: ').strip())
                if opcao == 1:
                    menu_categoria()
                elif opcao == 2:
                    menu_tarefa()
                elif opcao == 3:
                    encerrar()
                else:
                    print('Erro: opção fora da lista. Escolha um número válido.')
                    separador()
                    continue    
            except ValueError:
                print('Erro: digite apenas números.')
                separador()
                continue  
            except Exception:
                print('Ocorreu um erro inesperado. Tente novamente.')
                separador()
                continue

def menu_categoria():
    formatacao_menu('categoria')
    while True:
        try:
            opcao = int(input('1 - Criar \n'
                              '2 - Editar \n'
                              '3 - Visualizar Existentes \n'
                              '4 - Excluir \n'
                              '0 - Retornar ao Menu Principal \n\n'
                              'Opção: ').strip())
            if opcao == 1:
                criar_categoria()
            elif opcao == 2:
                editar_categoria()
            elif opcao == 3:
                visualizar_categorias()
            elif opcao == 4:
                excluir_categoria()
            elif opcao == 0:
                menu_principal()
            else:
                print('Erro: opção fora da lista. Escolha um número válido.')
                separador()
                continue    
        except ValueError:
            print('Erro: digite apenas números.')
            separador()
            continue
        except Exception:
            print('Ocorreu um erro inesperado. Tente novamente.')
            separador()
            continue

def menu_tarefa():
    formatacao_menu('tarefas')
    while True:
        try:
            opcao = int(input('1 - Criar \n'
                              '2 - Concluir \n'
                              '3 - Visualizar \n'
                              '4 - Excluir \n'
                              '0 - Retornar ao Menu Principal \n\n'
                              'Opção: ').strip())
            if opcao == 1:
                criar_tarefa()
            elif opcao == 2: 
                concluir_tarefa()
            elif opcao == 3:
                visualizar_tarefas()
            elif opcao == 4:
                excluir_tarefa()
            elif opcao == 0:
                menu_principal()
            else:
                print('Erro: opção fora da lista. Escolha um número válido.')
                separador()
                continue
        except ValueError:
            print('Erro: digite apenas números.')
            separador()
            continue
        except Exception:
            print('Ocorreu um erro inesperado. Tente novamente.')
            separador()
            continue


# FUNÇÕES ÚTEIS / FORMATAÇÃO
def formatacao_menu(texto):
    largura = 70
    print('=' * largura )
    print(texto.upper().center(largura))
    print('=' * largura)  

def separador():
    print('-' * 70)
 