#include "WifiCam.hpp"
#include <StreamString.h>
#include <uri/UriBraces.h>

static const char FRONTPAGE[] = R"EOT(
<!doctype html>
<title>e</title>
<body>hello</body>
)EOT";

static void
serveStill(bool dbug)
{
  auto frame = esp32cam::capture();
  if (frame == nullptr) {
    Serial.println("capture() failure");
    server.send(500, "text/plain", "still capture error\n");
    return;
  }
  if (dbug) Serial.printf("capture() success: %dx%d %zub\n", frame->getWidth(), frame->getHeight(),
                frame->size());

  server.setContentLength(frame->size());
  server.send(200,  "image/jpeg");
  WiFiClient client = server.client();
  frame->writeTo(client);
}

static void
serveMjpeg(bool dbug)
{
  if (dbug) Serial.println("MJPEG streaming begin");
  WiFiClient client = server.client();
  auto startTime = millis();
  int nFrames = esp32cam::Camera.streamMjpeg(client);
  auto duration = millis() - startTime;
  if (dbug) Serial.printf("MJPEG streaming end: %dfrm %0.2ffps\n", nFrames, 1000.0 * nFrames / duration);
}

void
addRequestHandlers(bool dbug)
{
  server.on("/", HTTP_GET, [] {
    server.setContentLength(sizeof(FRONTPAGE));
    server.send(200, "text/html");
    server.sendContent(FRONTPAGE, sizeof(FRONTPAGE));
  });

//  server.on("/robots.txt", HTTP_GET,
//            [] { server.send(200, "text/html", "User-Agent: *\nDisallow: /\n"); });

//  server.on("/resolutions.csv", HTTP_GET, [] {
//    StreamString b;
//    for (const auto& r : esp32cam::Camera.listResolutions()) {
//      b.println(r);
//    }
//    server.send(200, "text/csv", b);
//  });

  server.on(UriBraces("/{}x{}.{}"), HTTP_GET, [dbug] {
    long width = server.pathArg(0).toInt();
    long height = server.pathArg(1).toInt();
    String format = server.pathArg(2);
    if (width == 0 || height == 0 || !(format == "jpg" || format == "mjpeg")) {
      server.send(404);
      return;
    }

    auto r = esp32cam::Camera.listResolutions().find(width, height);
    if (!r.isValid()) {
      server.send(404, "text/plain", "non-existent resolution\n");
      return;
    }
    if (r.getWidth() != width || r.getHeight() != height) {
      server.sendHeader("Location",
                        String("/") + r.getWidth() + "x" + r.getHeight() + "." + format);
      server.send(302);
      return;
    }

    if (!esp32cam::Camera.changeResolution(r)) {
      Serial.printf("changeResolution(%ld,%ld) failure\n", width, height);
      server.send(500, "text/plain", "changeResolution error\n");
    }
    if (dbug) Serial.printf("changeResolution(%ld,%ld) success\n", width, height);

    if (format == "jpg") {
      serveStill(dbug);
    } else if (format == "mjpeg") {
      serveMjpeg(dbug);
    }
  });
}
