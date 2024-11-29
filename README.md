# Ajuste e Validação de Números de Telefone com Python

Este script processa e ajusta números de telefone em uma base de dados. Ele inclui a limpeza inicial, remoção ou adição de prefixos (como DDI e DDD), e a normalização dos números para um formato padronizado. O script foi projetado para lidar com variações comuns em números de telefone e salvar o resultado em um novo arquivo CSV.

## Funcionalidades

- **Limpeza Inicial dos Dados**:
  - Remove notação científica e converte valores para texto.
  - Trata valores inválidos, atribuindo uma string vazia.

- **Ajuste dos Números de Telefone**:
  - Remove prefixos desnecessários, como `55` repetidos.
  - Adiciona dígito `9` após o DDD, quando ausente.
  - Normaliza números para o formato com ou sem DDI conforme o caso.

- **Exportação dos Dados Ajustados**:
  - Gera um arquivo CSV contendo os números ajustados.

## Como Funciona

1. **Carregamento da Base de Dados**:
   - O script lê um arquivo CSV fornecido pelo usuário contendo os números de telefone.

2. **Processamento**:
   - Cada número é processado por duas funções:
     - **`clean_phone`**: Remove valores inválidos e converte números para texto.
     - **`adjust_phone_number`**: Ajusta os números de acordo com seu comprimento e estrutura.

3. **Exportação**:
   - Os dados ajustados são salvos em um novo arquivo CSV.

## Dependências

Este script utiliza a biblioteca `pandas`. Para instalar, execute:

pip install pandas
Estrutura do Código
Funções Principais:

clean_phone(value): Valida e converte números para texto, tratando entradas inválidas.
adjust_phone_number(phone): Ajusta os números de telefone com base em sua estrutura e comprimento.
Fluxo de Execução:

Carrega o arquivo CSV da base de dados.
Aplica as funções de limpeza e ajuste na coluna user_phone.
Salva os resultados no arquivo especificado.

Como Usar
Substitua os caminhos dos arquivos no código:

Arquivo de entrada (input_file_path): Caminho para o arquivo CSV original.
Arquivo de saída (output_file_path): Caminho para salvar o arquivo ajustado.
Execute o script:


python script_ajustar_telefone.py
O script exibirá o caminho do arquivo ajustado ao final da execução:


Arquivo ajustado salvo em: <caminho_do_arquivo>
Personalização
Coluna de Telefone: O script utiliza a coluna user_phone. Certifique-se de que esta coluna exista no arquivo de entrada.
Formatação Específica: Para ajustar as regras de formatação, edite a lógica na função adjust_phone_number.
Observações
Certifique-se de que o arquivo de entrada está no formato CSV e contém uma coluna chamada user_phone.
Este script é configurado para lidar com números de telefone no Brasil, considerando o DDI 55 e adicionando o dígito 9 para celulares.
