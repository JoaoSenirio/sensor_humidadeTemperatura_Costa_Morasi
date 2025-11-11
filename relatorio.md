# Relatório Técnico da Dupla

## 1. Escopo e Objetivos

Implementar a leitura do sensor AHT20 via interface I²C e exibir em tempo real a temperatura e a umidade relativa no display OLED da BitDogLab, garantindo estabilidade de leitura e compatibilidade com a biblioteca MicroPython oficial.

---

## 2. Metodologia e Implementação

O sistema foi desenvolvido em MicroPython, utilizando o ambiente VSCode, compatível com a placa BitDogLab, baseada no microcontrolador RP2040. O projeto tem como finalidade realizar a leitura de temperatura e umidade do sensor AHT20 via interface I²C e exibir os valores em tempo real no display OLED da placa.

O esquemático segue:

 ---------------------------
|        BitDogLab          |
|   (RP2040 + Periféricos)  |
 ------------ --------------
             |
        Interface I²C
             |
      ------- ---------
     |      AHT20      |
     | Temp / Umidade  |
      ------- --------
             |
        Dados Processados
             |
      ------- --------
     |    OLED 0.96"  |
      -----------------


---

## 3. Resultados e Análise

| Temperatura (°C) | Umidade Relativa (%) |
|------------------|----------------------|
| 23,45 | 57,07 |
| 23,48 | 57,08 |
| 23,50 | 57,05 |
| 23,49 | 57,10 |
| 23,51 | 57,08 |
| 23,48 | 57,01 |
| 23,48 | 57,03 |
| 23,49 | 56,98 |
| 23,50 | 56,99 |
| 23,51 | 56,95 |
| 23,50 | 56,96 |
| 23,52 | 56,96 |
| 23,49 | 56,95 |
| 23,50 | 56,92 |
| 23,51 | 56,93 |
| 23,49 | 56,83 |
| 23,51 | 56,80 |
| 23,50 | 56,83 |
| 23,51 | 56,90 |

---

## 4. Dificuldades e Soluções
Relate os principais desafios técnicos enfrentados e as soluções implementadas.  
Explique como eventuais limitações foram contornadas ou mitigadas, de modo a registrar aprendizados úteis para reproduções futuras.

**Exemplos:**
- Ajuste de timing no barramento I²C;  
- Necessidade de adaptação da biblioteca para MicroPython;  
- Filtragem de ruído em leitura analógica.

---

## 5. Conclusões e Trabalhos Futuros

O sistema desenvolvido mostrou-se funcional, estável e responsivo, sendo capaz de monitorar em tempo real a temperatura e a umidade relativa com precisão adequada ao sensor AHT20. A integração com o display OLED facilitou a visualização e validação dos resultados obtidos

Para melhorar o desempenho do sistema como um todo, principalmente ao conectarmos vários sensores juntos na mesma bitboard, ou exigir uma carga de trabalho mais responsiva, a migração para a linguagem C seria altamente considerada, devido ao seu alto desempenho de processamento e memória.

---

## 6. Referências
https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf

