import regex as re

class ValidadorSenhaAutomato:
    def __init__(self, comprimento_minimo):
        self.comprimento_minimo = comprimento_minimo
        self.transicoes = {
            0: {'num': 1, 'minus': 2, 'mai': 3, '@': 4, '!': 5, '#': 5, '$': 5, '%': 5, '&': 5},
            1: {'num': 1},
            2: {'minus': 2},
            3: {'mai': 3},
            4: {'num': 1, 'minus': 2, 'mai': 3},
            5: {'num': 1, 'minus': 2, 'mai': 3}
        }
        self.estados_finais = {1, 2, 3, 4, 5}

    def validar_senha(self, senha):
        estado_atual = 0
        tem_especial = False
        caractere_especial = None  
        for indice, caractere in enumerate(senha, 1):
            print(f"Iteração {indice}:")
            print("Caractere:", caractere)
            print("Estado atual:", estado_atual)
            
            if re.match(r'\d', caractere):
                prox_estado = self.transicoes[estado_atual].get('num', None)
            elif re.match(r'[a-z]', caractere):
                prox_estado = self.transicoes[estado_atual].get('minus', None)
            elif re.match(r'[A-Z]', caractere):
                prox_estado = self.transicoes[estado_atual].get('mai', None)
            elif re.match(r'[@]', caractere):
                prox_estado = self.transicoes[estado_atual].get('@', None)
            elif re.match(r'[!#$%&]', caractere):
                prox_estado = self.transicoes[estado_atual].get(caractere, None)
                tem_especial = True
                if not caractere_especial:  
                    caractere_especial = caractere
            else:
                return True 

            if prox_estado is None:
                return True
            estado_atual = prox_estado
            print("Próximo estado:", prox_estado)
            print("Estado atual após transição:", estado_atual)

        senha_valida = estado_atual in self.estados_finais and len(senha) >= self.comprimento_minimo and tem_especial
        print("Tamanho da senha:", len(senha))
        print("Caractere especial contido na senha:", caractere_especial)
        print("Senha válida:", senha_valida)
        return senha_valida

if __name__ == "__main__":
    comprimento_minimo = 8
    automato = ValidadorSenhaAutomato(comprimento_minimo)
    senha_teste = "linoguerrerodopovobrasileiro@"
    print("A senha '{}' é válida? {}".format(senha_teste, automato.validar_senha(senha_teste)))