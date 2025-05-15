import re #biblioteca de somente letras ou numeros

def validar_nome(nome):
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome.strip())) #Verdadeiro ou Falso se for apenas Letras

# função a seguir para evitar erros de digitação do cpf
def organizar_cpf(cpf):
    return re.sub(r"\D", "", cpf) #pega qualquer coisa que não seja numero e remove

def validar_cpf(cpf):
    cpf = organizar_cpf(cpf) #chama função de remover não números
    if len(cpf) != 11 or cpf == cpf[0] * 11: #verifica se tem exatamente 11 digitos e se não é repetido "1"
        return False



