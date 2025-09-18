# Detecção de Inversões em Cheerleading com Visão Computacional

## Descrição
Este projeto tem como objetivo identificar momentos de inversão durante lançamentos no esporte cheerleading utilizando técnicas de visão computacional. O estudo utiliza diferentes algoritmos de detecção de poses, incluindo **Viola & Jones**, **MediaPipe** e **YOLO**, e os mescla para obter resultados precisos qaunto a posições invertidas de atletas.

## Tecnologias Utilizadas
- Python 3.x  
- OpenCV  
- MediaPipe  
- YOLO (Ultralytics)  
- Haar Cascade (Viola & Jones)  

## Estrutura do Projeto
Detecção de Inversão/
├─ Main.py/ # Main do projeto
├─ funcoes/ # Todas as funcoes criadas para realizar a detecção
│ ├─ __init__.py
│ ├─ bodyParts.py
│ ├─ FindFLyer.py
│ ├─ Inversao.py
│ ├─ MediaPipeiInversao.py
│ ├─ PontoDeInteresse.py
│ └─ CriarEixo.py
├─ 131.mp4 # Video de teste para a detecção 
└─ requirements.txt # Dependências do projeto

## Resutados
Teste.png # Frame atual que está sendo processado
Teste2.png # Frame focado na flyer, que será utilizado pelo Mediapipe
Teste3.png # Resultado da detecção de inversão
