// based on https://github.com/yoursunny/esp32cam/example/
// using the esp32cam library by yoursunny https://github.com/yoursunny/esp32cam
// require: esp32 v2.02 https://github.com/espressif/arduino-esp32/releases/tag/2.0.2
// require: ESP32Servo library
#include "WifiCam.hpp"
#include <WiFi.h>

#include <ESP32Servo.h>
#include "CameraMovement.h"

static const char *WIFI_SSID = "FLYNN-LAPTOP";
static const char *WIFI_PASS = "87654321";

const int bigPin = 14;   // TBD
const int smallPin = 15; // TBD
const int DUMMYPIN1 = 12;
const int DUMMYPIN2 = 13;
const int servoMoveGap = 100; // TBD
unsigned long timer = 0;

esp32cam::Resolution initialResolution;

WebServer server(80);

int servoArr[2] = {0, 0};
CameraMovement camMo;
Servo dummy1;
Servo dummy2;
Servo big;
Servo small;

void setup()
{

  // servo
  dummy1.attach(DUMMYPIN1);
  dummy2.attach(DUMMYPIN2);
  big.attach(bigPin);
  small.attach(smallPin);

  //cam
  Serial.begin(115200);
  Serial.println();

  {
    using namespace esp32cam;

    initialResolution = Resolution::find(1024, 768);

    Config cfg;
    cfg.setPins(pins::AiThinker);
    cfg.setResolution(initialResolution);
    cfg.setJpeg(80);

    bool ok = Camera.begin(cfg);
    if (!ok)
    {
      Serial.println("camera initialize failure");
      delay(5000);
      ESP.restart();
    }
    Serial.println("camera initialize success");
  }

  // stabilize camera before starting WiFi to reduce "Brownout detector was triggered"
  delay(2000);

  WiFi.persistent(false);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  if (WiFi.waitForConnectResult() != WL_CONNECTED)
  {
    Serial.println("WiFi failure");
    delay(5000);
    ESP.restart();
  }

  Serial.println("WiFi connected");
  Serial.print("http://");
  Serial.println(WiFi.localIP());

  addRequestHandlers();
  server.begin();
}

void loop()
{
  server.handleClient();
  if (millis() - timer > servoMoveGap) {
    cameraMove();
    timer = millis();
  }
}

void cameraMove()
{
  //camMo.getNext(servoArr);
  big.write(servoArr[0]);
  small.write(servoArr[1]);
}
