Requirement:
1.ESP8266 NodeMCU
2.SSD1306 OLED display (I2C version)
3. Jumper wires

Wiring:
Connect the OLED display to the ESP8266 as follows:
- VCC to Vin
- GND to GND
- SDA to D2 (GPIO 4)
- SCL to D1 (GPIO 5)

Software setup:
1. Install MicroPython on your ESP8266.
2. Upload the ssd1306.py library to your ESP8266 if it's not already included in your firmware.
