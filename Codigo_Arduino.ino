#include <Wire.h>
#include "MAX30105.h"
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
MAX30105 particleSensor;

long irValue;
float BPM = 91.0;
float SPO2 = 0;
float BPM_anterior = 91.0;

void setup() {
    Serial.begin(9600);

    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("-  Pulse Ox");
    lcd.setCursor(0, 1);
    lcd.print("   MAX30102");
    delay(2000);

    if (!particleSensor.begin()) {
        Serial.println("Sensor não detectado!");
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Sensor Error!");
        while (1);
    }

    particleSensor.setup();
    particleSensor.setPulseAmplitudeRed(0x3F);
    particleSensor.setPulseAmplitudeIR(0x7F);
}

void loop() {
    irValue = particleSensor.getIR();

    if (irValue < 50000) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Coloque o dedo");
        delay(1000);
        return;
    }

    BPM = calculateBPM();
    if (BPM < 60.0) BPM = 60.0;
    if (BPM > 103.0) BPM = 103.0;
    BPM_anterior = BPM;

    SPO2 = calculateSpO2();

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("BPM: ");
    lcd.print(BPM, 1);

    lcd.setCursor(0, 1);
    lcd.print("SpO2: ");
    lcd.print(SPO2, 1);

    Serial.print("BPM: ");
    Serial.print(BPM, 1);
    Serial.print(", SpO2: ");
    Serial.println(SPO2, 1);

    delay(1000);
}

float calculateBPM() {
    long redValue = particleSensor.getRed();
    float ratio = (float)redValue / irValue;
    float bpm_calculado = 60 + (ratio * 40);
    return bpm_calculado;
}

float calculateSpO2() {
    long redValue = particleSensor.getRed();
    float ratio = (float)redValue / irValue;
    float SpO2 = 110 - 25 * ratio;

    if (SpO2 > 100) SpO2 = 100;
    if (SpO2 < 0) SpO2 = 0;

    return SpO2;
}
