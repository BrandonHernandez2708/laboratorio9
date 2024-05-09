int relayPin = 8;  // Pin para controlar el relé
int ledPin = 13;    // Pin para el LED adicional

void setup() {
  pinMode(relayPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Inicia la comunicación serial a 9600 baudios
}

void loop() {
  if (Serial.available() > 0) { // Verifica si hay datos disponibles para leer desde el puerto serie
    char command = Serial.read(); // Lee el dato del puerto serie

    if (command == '1') {
      digitalWrite(relayPin, HIGH);
      digitalWrite(ledPin, HIGH);
    } else if (command == '0') {
      digitalWrite(relayPin, LOW);
      digitalWrite(ledPin, LOW);
    }
  }
}