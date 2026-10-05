import serial
import openpyxl
from datetime import datetime

porta = 'COM4'
baudrate = 9600  

nome_arquivo = "dados_bpm_spo2.xlsx" 

try:
    arduino = serial.Serial(porta, baudrate)
    print("Conexão com o Arduino estabelecida!")
except serial.SerialException as e:
    print(f"Erro ao conectar ao Arduino: {e}") 
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
    sheet.append(["Timestamp", "BPM", "SpO2"])
    wb.save(nome_arquivo)
    print("Novo arquivo Excel criado.")

def salvar_no_excel(timestamp, bpm, spo2): 
    sheet.append([timestamp, bpm, spo2])
    wb.save(nome_arquivo)

print("Salvando dados do Arduino... (Pressione Ctrl+C para interromper)")

try:
    while True:
        linha = arduino.readline().decode('utf-8').strip() 
        print(f"Dado recebido: {linha}")

        if "BPM:" in linha and "SpO2:" in linha:  
            try:
                bpm_part = linha.split(",")[0].split(":")[1].strip() 
                spo2_part = linha.split(",")[1].split(":")[1].strip() 
                bpm = float(bpm_part)
                spo2 = float(spo2_part)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
                salvar_no_excel(timestamp, bpm, spo2) 
                print(f"Salvo: {timestamp}, BPM: {bpm}, SpO2: {spo2}")
            except ValueError:
                print("Erro ao processar os valores numéricos.")  
        else:
            print("Erro ao processar os dados. Formato esperado: BPM, SpO2")  

except KeyboardInterrupt:
    print("\nExecução interrompida pelo usuário.")
finally:
    arduino.close()
    print("Conexão com o Arduino encerrada.")
