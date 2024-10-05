# PLN_pipeline

Aplique técnicas de tokenização e correção de erros de ortografia a dados de revisão de
produtos que tenham sido raspados de uma página de revisão da Internet. Ilustre o
comportamento e o desempenho do seu trecho de pipeline de PLN identificando os principais
gargalos e sugira uma melhoria possível. Esclareça o porquê da ordem dos elementos em sua
pipeline.

Na sua resposta ilustre, através de uma aplicação web, desenvolvida em Python, com front end
e back end, os seguintes pontos:

a) O tempo necessário para se efetuar a raspagem de dados.
b) O tempo necessário à remoção de ruído
c) O tempo necessário à quebra em tokens de frases e tokens de palavras.
d) Substituição de abreviaturas
d) O tempo necessário para se processar e corrigir palavras digitadas incorretamente.

A entrada para seu programa deve ser uma URL.

As saídas devem ser cada uma das etapas citadas da pipeline de pré-processamento e os tempos
necessários para se executar tais etapas.

**Exemplo**


| Entrada | Saída | Etapa | Tempo  |
| ------- | ----- | ----- | ------ |
| `http://teste.com.br`                                                                     | `"<html>...textos</html>"`                                                                   | Raspagem                       | 5ms    |
| `"<html>...textos</html>"`                                                                | `"Produto interessantee. Gostei bastante. Mt!"`                                               | Remoção de ruído                | 1ms    |
| `"Produto interessantee. Gostei bastante. Mt!"`                                           | `['Produto interessantee.', 'Gostei bastante.', 'Mt!']`                                       | Tokenização por frases          | 2ms    |
| `['Produto interessantee.', 'Gostei bastante.', 'Mt!']`                                   | `[['Produto', 'interessantee'], ['Gostei', 'bastante'], ['Mt']]`                              | Tokenização por palavras        | 2.5ms  |
| `[['Produto', 'interessantee'], ['Gostei', 'bastante'], ['Mt']]`                          | `[['Produto', 'interessantee'], ['Gostei', 'bastante'], ['Muito']]`                           | Expansão de siglas e abreviaturas| 1ms    |
| `[['Produto', 'interessantee'], ['Gostei', 'bastante'], ['Muito']]`                       | `[['produto', 'interessantee'], ['gostei', 'bastante'], ['muito']]`                           | Conversão para minúsculas       | 3ms    |
| `[['produto', 'interessantee'], ['gostei', 'bastante'], ['muito']]`                       | `[['produto', 'interessante'], ['gostei', 'bastante'], ['muito']]`                            | Correção de caracteres incorretos| 2.3ms  |
