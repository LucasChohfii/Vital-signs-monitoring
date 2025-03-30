import serial
import openpyxl
from datetime import datetime

porta = 'COM4'
baudrate = 9600  # Corrigido: "%600" → "9600" (valor comum para Baud Rate)

nome_arquivo = "dados_bpm_spo2.xlsx"  # Corrigido: "none_arguivo" e "nome_arguivo" → "nome_arquivo"

try:
    arduino = serial.Serial(porta, baudrate)
    print("Conexão com o Arduino estabelecida!")
except serial.SerialException as e:
    print(f"Erro ao conectar ao Arduino: {e}")  # Corrigido: "{Errp ao consetar" → "Erro ao conectar"
    exit()

try:
    wb = openpyxl.load_workbook(nome_arquivo)
    sheet = wb.active
    print("Arquivo Excel existente carregado.")
except FileNotFoundError:
    # Cria um novo arquivo Excel
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Dados BPM e SpO2"
    # Cabeçalhos
    sheet.append(["Timestamp", "BPM", "SpO2"])  # Corrigido: "SpO2)" → "SpO2"]"
    wb.save(nome_arquivo)
    print("Novo arquivo Excel criado.")

# Função para salvar os dados no Excel
def salvar_no_excel(timestamp, bpm, spo2):  # Corrigido: removido "!usage" (comentário inválido)
    sheet.append([timestamp, bpm, spo2])
    wb.save(nome_arquivo)

# Loop principal
print("Salvando dados do Arduino... (Pressione Ctrl+C para interromper)")

try:
    while True:
        # Lê o que é recebido do Arduino
        linha = arduino.readline().decode('utf-8').strip()  # Corrigido: "resabido" → "recebido"
        print(f"Dado recebido: {linha}")  # Corrigido: "(linha)" → "{linha}"

        # Verifica e processa os dados no formato "BPM: 91.2, SpO2: 87.8"
        if "BPM:" in linha and "SpO2:" in linha:  # Corrigido: "BPH" e "Sp02" → "BPM" e "SpO2"
            try:
                # Extraindo os valores de BPM e SpO2
                bpm_part = linha.split(",")[0].split(":")[1].strip()  # Pega o valor após "BPM:"
                spo2_part = linha.split(",")[1].split(":")[1].strip()  # Pega o valor após "SpO2:"
                bpm = float(bpm_part)
                spo2 = float(spo2_part)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Corrigido: 'YY'-Xm-Xd XM-XM-XS' → formato correto
                # Salva os dados no Excel
                salvar_no_excel(timestamp, bpm, spo2)  # Corrigido: removido colchetes extras
                print(f"Salvo: {timestamp}, BPM: {bpm}, SpO2: {spo2}")
            except ValueError:
                print("Erro ao processar os valores numéricos.")  # Corrigido: "Error no processar" → "Erro ao processar"
        else:
            print("Erro ao processar os dados. Formato esperado: BPM, SpO2")  # Corrigido mensagem

except KeyboardInterrupt:
    print("\nExecução interrompida pelo usuário.")
finally:
    arduino.close()
    print("Conexão com o Arduino encerrada.")