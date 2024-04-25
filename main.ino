#include <Adafruit_NeoPixel.h>
#define LED_COUNT 300
#define Pin 9
Adafruit_NeoPixel leds = Adafruit_NeoPixel(LED_COUNT, Pin, NEO_GRB + NEO_KHZ800);
// C++ code
//
int R = 0;
int G = 255;
int B = 0;
int brightness = 64;
void setup()
{
  leds.begin();
  //pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  for(int i = 0; i < LED_COUNT; i++){
    leds.setPixelColor(i, R, G, B);
    leds.setBrightness(brightness);
    leds.show();
  }
}