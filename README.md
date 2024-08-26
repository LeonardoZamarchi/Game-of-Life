# Jogo da Vida - Simulação Interativa

Este repositório contém uma implementação interativa do Jogo da Vida de John Conway. A simulação permite ajustar a probabilidade de células vivas na configuração inicial e controlar a velocidade da simulação em tempo real, além de pausar, retomar e resetar a simulação.

## Descrição do Jogo da Vida

O Jogo da Vida é um autômato celular criado pelo matemático John Conway. Ele consiste em um grid de células que podem estar vivas ou mortas. A evolução do grid ocorre em passos discretos, com o estado de cada célula dependendo do estado de suas vizinhas. As regras básicas que governam a transição entre os estados das células são:

### Regras do Jogo

1. **Sobrevivência**:
   - Uma célula viva com 2 ou 3 vizinhos vivos continua viva na próxima geração.

2. **Morte**:
   - Uma célula viva com menos de 2 vizinhos vivos morre por isolamento.
   - Uma célula viva com mais de 3 vizinhos vivos morre por superpopulação.

3. **Nascimento**:
   - Uma célula morta com exatamente 3 vizinhos vivos torna-se viva na próxima geração.

## Funcionalidades do Script

Este script implementa o Jogo da Vida com funcionalidades interativas, permitindo ao usuário:

- **Controlar a Probabilidade Inicial**: Use um slider para ajustar a probabilidade de células vivas na configuração inicial.
- **Controlar a Velocidade da Simulação**: Use um slider para ajustar a velocidade da simulação (intervalo de tempo entre as iterações).
- **Pausar e Retomar a Simulação**: Use os botões "Play" e "Pause" para controlar a execução da simulação.
- **Resetar a Simulação**: Use o botão "Reset" para reiniciar o grid com a configuração inicial.

## Bibliotecas Utilizadas

O script depende das seguintes bibliotecas Python:

- `numpy`: Utilizada para manipulação e cálculo de arrays de forma eficiente.
- `matplotlib`: Utilizada para visualização gráfica e animação da simulação.
- `matplotlib.widgets`: Utilizada para criar sliders e botões interativos.

## Como Funciona

### Estrutura Básica

1. **Grid Inicial**:
   - O grid é inicializado com base na probabilidade de células vivas, controlada pelo slider "Prob Vivos".

2. **Atualização do Grid**:
   - A cada iteração, o grid é atualizado de acordo com as regras do Jogo da Vida. As células são avaliadas e atualizadas simultaneamente para a próxima geração.

3. **Animação**:
   - A animação visualiza a evolução do grid ao longo do tempo. A velocidade pode ser ajustada em tempo real.

4. **Controle de Simulação**:
   - O usuário pode pausar, retomar ou resetar a simulação a qualquer momento.

### Como Executar

1. **Instale as Dependências**:
   Certifique-se de que `numpy` e `matplotlib` estão instalados em seu ambiente Python. Você pode instalá-los via pip:

   ```bash
   pip install numpy matplotlib
