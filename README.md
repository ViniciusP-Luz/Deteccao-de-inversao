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
```text
DetecçãoDeInversao/
├─ Main.py              # Main do projeto
├─ funcoes/             # Funções auxiliares para detecção
│ ├─ init.py
│ ├─ bodyParts.py
│ ├─ FindFlyer.py
│ ├─ Inversao.py
│ ├─ MediaPipeInversao.py
│ ├─ PontoDeInteresse.py
│ └─ CriarEixo.py
├─ 131.mp4             # Vídeo de teste para detecção
└─ requirements.txt    # Dependências do projeto
```


## Resutados
```text
- Teste.png        # Frame atual que está sendo processado
- Teste2.png       # Frame focado na flyer, que será utilizado pelo Mediapipe
- Teste3.png       # Resultado da detecção de inversão
```
