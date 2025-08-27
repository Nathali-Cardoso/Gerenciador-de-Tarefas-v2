import json
import sys

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
        try:
            categoria = input('Digite o nome da categoria: ').lower().strip()
            if not categoria.strip():
                print('Erro: categoria não pode estar vazia.')
                continue
            
            elif categoria not in dados_tarefas:
                    dados_tarefas[categoria] = []
                    salvar_dados()
                    print('\nCategoria adicionada com sucesso!')
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
                            continue
            else:
                print('Erro: categoria já existe!')
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
            edi_categoria = input('Qual categoria deseja editar: ').strip().lower()
            if not edi_categoria.strip():
                print('Erro: dados inválidos - campo vazio.')
                continue
            elif edi_categoria not in dados_tarefas:
                print('Erro: categoria não localizada.')
                continue
            else:
                while True:
                    try:
                        separador()
                        print(f'Categoria selecionada: {edi_categoria} \n')
                        novo_nome_cat = input('Novo nome: ').strip().lower()
                        if not novo_nome_cat.strip():
                            print('Erro: nome da categoria não pode estar em branco.')
                            continue    
                        else:
                            dados_tarefas[novo_nome_cat] = dados_tarefas.pop(edi_categoria)
                            salvar_dados()
                            separador()
                            print(f'Categoria atualizada com sucesso!')
                            separador()
                            retornar_menu()
                    except ValueError:
                        print('Erro: dados inválidos.')
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
            esc_cat = input('Nome da categoria que deseja excluir: ').strip().lower()
            if not esc_cat.split():
                print('Erro: dados inválidos - campo vazio.')
                continue
            elif esc_cat in dados_tarefas:
                separador()
                while True:
                    try:    
                        continuar = int(input(f'Deseja realmente realizar a exclusão da categoria {esc_cat}? \n'
                                              '1 - sim \n'
                                              '2 - não \n'
                                              'Opção: ').strip())
                        if continuar == 1:
                            del dados_tarefas[esc_cat]
                            salvar_dados()
                            separador()
                            print('Categoria excluída com sucesso!')
                            separador()
                            retornar_menu()
                        elif continuar == 2:
                            print('\nProcedimento cancelado.')
                            separador()
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


# FUNÇÕES DE EDIÇÃO / TAREFAS        
def criar_tarefa():
    formatacao_menu('criar tarefa')
    print('Categorias:')
    for c in dados_tarefas:
        print(f'- {c}')
    while True:
        try:
            separador()
            esc_cat = input('Digite o nome da categoria onde será adicionada \na nova tarefa: ').strip().lower()            
            if not esc_cat.strip():
                print('Erro: dados inválidos - campo vazio.')
                continue
            elif esc_cat not in dados_tarefas:
                print('Erro: dados inválidos - categoria não existe.')
                continue
            else:
                separador()
                print(f'Categoria > {esc_cat} < selecionada com sucesso. \n'
                    'Insira os dados da nova tarefa abaixo.')
                while True:
                    try:
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
                                                             '2 - Retornar ao Menu Principal \n'
                                                             '3 - Sair \n'
                                                             'Opção: ').strip())
                                    if outra_tarefa == 1:
                                        criar_tarefa()
                                    elif outra_tarefa == 2:
                                        menu_principal()
                                    elif outra_tarefa == 3:
                                        encerrar()
                                    else:
                                        print('Erro: opção inválida')
                                        continue
                                except ValueError:
                                    print('Erro: digite apenas números.')
                                    continue  
                    except ValueError:
                        print('Erro: dados inválidos.')
                        continue
        except ValueError:
            print('Erro: dados inválidos.')
            continue
  
def excluir_tarefa(): 
    formatacao_menu('excluir tarefa')
    print('Categorias:')   
    for categoria in dados_tarefas:
        print(f'- {categoria}') 
    while True:
        try: 
            loc_categoria = input('\nEm qual categoria esta tarefa está localizada: ').strip().lower()
            if not loc_categoria.strip():
                print('Erro: dados inválidos - campo vazio.')
                continue
            elif loc_categoria in dados_tarefas:
                print('\nCategoria localizada!')
                separador()
                print(f'Categoria: {loc_categoria}\n'
                      'Tarefas: ')
                for indice, tarefa in enumerate(dados_tarefas[loc_categoria], start=1):
                    print(f'Tarefa {indice}: {tarefa["descrição"]} - conclusão: {tarefa["conclusão"]}')
                separador()   
                while True:
                    try:
                        exc_tarefa = input('Insira o nome da tarefa que deseja excluir: ').strip().lower()
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

def concluir_tarefa():
    formatacao_menu('concluir tarefa')
    print('Categorias:')
    for categoria in dados_tarefas:
        print(f'- {categoria}')   
    separador()
    while True:
        try:        
            loc_cat = input('Em qual categoria a tarefa está localizada?: ').strip().lower()
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
                        ed_tarefa = input('Qual tarefa deseja concluir?: ').strip().lower()
                        if not ed_tarefa.strip():
                            print('Erro: dados inválidos - campo vazio.')
                            continue
                        else:
                            for tarefa in dados_tarefas[loc_cat]:
                                if tarefa["descrição"] == ed_tarefa:
                                    tarefa["descrição"] = 'concluído'  
                                    salvar_dados()                                      
                                    print('\nTarefa concluída com sucesso!')
                                    
                                    while True:
                                        try:
                                            separador()
                                            outra_tarefa = int(input('Deseja concluir outra tarefa?[1-sim/2-não]: ').strip())
                                            if outra_tarefa == 1:
                                                concluir_tarefa()
                                            elif outra_tarefa == 2:
                                                retornar_menu()            
                                            else:
                                                print('Erro: opção inválida.')
                                                continue
                                        except ValueError:
                                            print('Erro: digite apenas números.')    
                                            continue
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

         
#FUNÇÃO DE ENCERRAMENTO DO PROGRAMA
def encerrar():
    separador()
    print('Encerrando o programa...\n'
          'Até breve!')
    sys.exit(0)


# FUNÇÕES DE CONTROLE DE MENU
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
        
def menu_principal():
    if not dados_tarefas:
        formatacao_menu('menu principal')
        if not dados_tarefas:
            print('1 - Criar Categoria \n'
                '2 - Sair')
            while True:
                try:
                    separador()
                    opcao = int(input('Opção: ').strip())
                    if opcao == 1:
                        criar_categoria()
                    elif opcao == 2:
                        encerrar()
                    else:
                        print('Erro: opção inválida.')
                        continue
                except ValueError:
                    print('Erro: digite apenas números.')
                    continue
    else:
        formatacao_menu('menu principal')
        print('1 - Categorias \n'
            '2 - Tarefas \n'
            '3 - Sair')
    while True:
        try:
            separador()
            opcao = int(input('Opção: ').strip())
            if opcao == 1:
                menu_categoria()
            elif opcao == 2:
                menu_tarefa()
            elif opcao == 3:
                encerrar()
            else:
                print('Erro: opção inválida.')
                continue    
        except ValueError:
            print('Erro: digite apenas números.')
            continue  

def menu_categoria():
    formatacao_menu('categoria')
    print('1 - Criar \n'
          '2 - Editar \n'
          '3 - Excluir \n'
          '0 - Retornar ao Menu Principal')
    while True:
        try:
            separador()
            opcao = int(input('Opção: ').strip())
            if opcao == 1:
                criar_categoria()
            elif opcao == 2:
                editar_categoria()
            elif opcao == 3:
                excluir_categoria()
            elif opcao == 0:
                menu_principal()
            else:
                print('Erro: opção inválida.')
                continue    
        except ValueError:
            print('Erro: digite apenas números.')
            continue

def menu_tarefa():
    formatacao_menu('tarefas')
    print('1 - Criar \n'
          '2 - Concluir \n'
          '3 - Excluir \n'
          '0 - Retornar ao Menu Principal')
    while True:
        try:
            separador()
            opcao = int(input('Opção: ').strip())
            if opcao == 1:
                criar_tarefa()
            elif opcao == 2: 
                concluir_tarefa()
            elif opcao == 3:
                excluir_tarefa()
            elif opcao == 0:
                retornar_menu()
            else:
                print('Erro: opção inválida.')
                continue
        except ValueError:
            print('Erro: digite apenas números.')
            continue


# FUNÇÕES ÚTEIS / FORMATAÇÃO
def formatacao_menu(texto):
    largura = 70
    print('=' * largura )
    print(texto.upper().center(largura))
    print('=' * largura)

def separador():
    largura = 70
    print('-' * largura)
