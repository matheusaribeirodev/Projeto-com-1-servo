# 🤖 Controle de Servo e Tela OLED com ESP32

Este projeto usa uma placa ESP32 rodando **MicroPython** para controlar um servomotor e mostrar mensagens em uma tela OLED de forma simples usando dois botões.

imagem

---

## 🔌 Conexões (Pinos)

* **Tela OLED I2C:** `SDA` -> GPIO 21 | `SCL` -> GPIO 22
* **Servomotor (PWM):** Pino de sinal -> GPIO 18
* **Botão Azul:** GPIO 12 (Move o servo para 0° e mostra "Luz acesa")
* **Botão Verde:** GPIO 14 (Move o servo para 90° e mostra "luz apagada")
* **LED Verde:** GPIO 26 (Pisca ao apertar o botão azul)
* **LED Vermelho:** GPIO 25 (Pisca ao apertar o botão verde)

---

## 🕹️ Como Funciona

1. **Aperte o Botão Azul:** * O servo gira para **0°**.
   * O LED Verde pisca.
   * A tela OLED mostra: `"Luz acesa"`.

2. **Aperte o Botão Verde:** * O servo gira para **90°**.
   * O LED Vermelho pisca.
   * A tela OLED mostra: `"luz apagada"`.

---

## 🚀 Como Testar

1. Abra o projeto pronto no simulador através do link do [Wokwi](https://wokwi.com/projects/463823619639486465).
2. Clique no botão de **Play** (Iniciar Simulação).
3. Clique nos botões colorido na tela para ver o motor mexer e o texto mudar.

---
🔬 *Projeto desenvolvido por Matheus Augusto Ribeiro.
