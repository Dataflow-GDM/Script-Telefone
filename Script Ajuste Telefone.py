import pandas as pd

# Função para ajustar números de telefone
def adjust_phone_number(phone):
    if len(phone) == 15:
        # Remove o primeiro 55
        return phone[2:]
    elif len(phone) == 14:
        # Remove o primeiro 55 e adiciona o 9 após o DDD
        return phone[2:4] + '9' + phone[4:]
    elif len(phone) == 13:
        # Número está correto
        return phone
    elif len(phone) == 12:
        # Adiciona o 9 após o DDD
        return phone[:4] + '9' + phone[4:]
    elif len(phone) == 11:
        # Adiciona o DDI 55 no início
        return '55' + phone
    else:
        # Não altera o número se tiver 10 caracteres ou menos
        return phone

# Função para validar e limpar os dados inicialmente
def clean_phone(value):
    try:
        # Converter para string removendo notação científica, caso exista
        return str(int(float(value)))
    except (ValueError, TypeError):
        # Retorna vazio para valores inválidos
        return ''

# Caminho do arquivo original
input_file_path = r"C:\Users\Mauro\Growth Digital Marketing\Joabe Onorato da Silva - Analise de Dados\Bases\Base Telefone\base_segmento_smartico_2811.csv"

# Carregar os dados
data = pd.read_csv(input_file_path)

# Limpar a coluna user_phone
data['user_phone'] = data['user_phone'].apply(clean_phone)

# Aplicar a lógica de ajuste
data['adjusted_phone'] = data['user_phone'].apply(adjust_phone_number)

# Caminho para salvar o arquivo ajustado
output_file_path = r"C:\Users\Mauro\Growth Digital Marketing\Joabe Onorato da Silva - Analise de Dados\Bases\segmentado_ajustado.csv"

# Salvar o arquivo ajustado
data.to_csv(output_file_path, index=False)

print(f"Arquivo ajustado salvo em: {output_file_path}")
