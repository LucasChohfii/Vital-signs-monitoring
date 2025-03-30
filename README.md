# Português 🇧🇷

# Sistema de Monitoramento de Sinais Vitais

## Visão Geral

O **Sistema de Monitoramento de Sinais Vitais** foi projetado para o monitoramento contínuo dos batimentos cardíacos (BPM) e dos níveis de saturação de oxigênio no sangue (SpO2). Ele utiliza o sensor MAX30102 para medições precisas, um Arduino para processamento, um LCD para exibição dos dados em tempo real e comunicação Bluetooth para transmissão dos dados.

## Funcionalidades

- **Monitoramento de Batimentos Cardíacos (BPM):** Detecção da frequência cardíaca utilizando luz infravermelha refletida pelo sensor MAX30102.
- **Saturação de Oxigênio no Sangue (SpO2):** Medição e exibição dos níveis de saturação de oxigênio no sangue.
- **Exibição em Tempo Real:** Tela LCD 16x2 para exibição dos valores de BPM e SpO2.
- **Comunicação Bluetooth:** Os dados são enviados para um PC ou aplicativo móvel via módulo Bluetooth HC-05.
- **Registro no Excel:** Os dados são registrados em uma planilha do Excel com timestamps para fácil rastreamento e análise.

## Componentes Utilizados

- **MAX30102:** Sensor de oximetria de pulso e batimentos cardíacos.
- **Arduino UNO R3:** Microcontrolador utilizado para processar os dados do sensor.
- **LCD 16x2:** Utilizado para exibir os valores de BPM e SpO2.
- **Módulo Bluetooth HC-05:** Para transmissão sem fio dos dados.
- **Fios jumper, resistores e protoboard.**

## Como Usar

1. Conecte o sensor MAX30102, Arduino, display LCD e módulo Bluetooth conforme o esquema fornecido.
2. Carregue o código do Arduino na placa.
3. Emparelhe o módulo Bluetooth com seu dispositivo móvel ou PC.
4. Abra o script em Python para receber os dados e registrá-los em um arquivo Excel.

## Montagem no tinkercad

![Image](https://github.com/user-attachments/assets/ee258ffd-e552-4397-bbe3-9d1ffd809c01)
No esquema para a montagem no tinkercad, foram utilizados um Arduino UNO R3, um resistor de 10kΩ, um LCD 16X2, potenciômetro (simular o sensor de batimentos cardíacos e nível de oxigênio).
**Link para o tinkercad:** https://www.tinkercad.com/things/ghEfPm2XXAq-terrific-jarv

# English 🇺🇸

# Vital Signs Monitoring System

## Overview

The **Vital Signs Monitoring System** is designed for continuous monitoring of heart rate (BPM) and blood oxygen saturation (SpO2) levels. It features a MAX30102 sensor for accurate measurement, an Arduino for processing, an LCD for displaying real-time readings, and Bluetooth communication for data transmission.

## Features

- **Heart Rate Monitoring (BPM):** Heart rate detection using infrared light reflection from the MAX30102 sensor.
- **Blood Oxygen Saturation (SpO2):** Measure and display blood oxygen saturation levels.
- **Real-time Display:** 16x2 LCD screen for displaying heart rate and SpO2 values.
- **Bluetooth Communication:** Data is sent to a PC or mobile app via Bluetooth HC-05 module.
- **Excel Logging:** Data is saved in an Excel spreadsheet with timestamps for easy tracking and analysis.

## Components Used

- **MAX30102:** Pulse oximeter and heart rate sensor.
- **Arduino UNO R3:** Microcontroller used for processing the sensor data.
- **LCD 16x2 Display:** Used to display heart rate and SpO2 values.
- **HC-05 Bluetooth Module:** For wireless data transmission.
- **Jumper wires, resistors, and breadboard.**

## How to Use

1. Connect the MAX30102 sensor, Arduino, LCD display, and Bluetooth module as per the provided schematics.
2. Upload the Arduino code to your Arduino board.
3. Pair the Bluetooth module with your mobile or PC.
4. Open the Python script to receive the data and log it in an Excel file.
