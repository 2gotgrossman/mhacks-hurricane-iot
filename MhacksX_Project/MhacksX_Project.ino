// - Adafruit Unified Sensor Library: https://github.com/adafruit/Adafruit_Sensor
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library

#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN            2         // Pin which is connected to the DHT sensor.
#define Sound_Sensor A2
  int sound = 0;

// Uncomment the type of sensor in use:
#define DHTTYPE           DHT11     // DHT 11 

//DHT sensor connection to signal VCC and GND

//define DHT sensor object
DHT_Unified dht(DHTPIN, DHTTYPE);

//set delay to avoid port saturation
uint32_t delayMS;

void setup() {
  //Bluetooth Mate silver likes to talk fast
  Serial.begin(115200); 
  // Initialize device.
  dht.begin();
  //debug code
  //Serial.println("DHTxx Unified Sensor Example");
  //Print temperature sensor details.
  sensor_t sensor;
  dht.temperature().getSensor(&sensor);
  /*
  Serial.println("------------------------------------");
  Serial.println("Temperature");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" *C");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" *C");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" *C");  
  Serial.println("------------------------------------");
  */
  // Print humidity sensor details.
  dht.humidity().getSensor(&sensor);
  /*
  Serial.println("------------------------------------");
  Serial.println("Humidity");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println("%");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println("%");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println("%");  
  Serial.println("------------------------------------");
  */
  // Set delay between sensor readings based on sensor details.
  delayMS = sensor.min_delay / 1000;
  //add input for the sound sensor
  pinMode(Sound_Sensor, INPUT);

}

void loop() {
  // Delay between measurements.
  delay(delayMS);
  // Get temperature event and print its value.
  sensors_event_t event;  
  dht.temperature().getEvent(&event);
  //error handlers if there is a sensor read errror
  if (isnan(event.temperature)) {
    Serial.println("Error reading temperature!");
  }
  else {
    //Serial.print("Temperature: ");
    Serial.print(event.temperature);
    //Serial.print(" *C");
  }
  // Get humidity event and print its value.
  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) {
    Serial.println("Error reading humidity!");
  }
  else {
    //Serial.print("Humidity: ");
    Serial.print(", ");
    Serial.print(event.relative_humidity);
    //Serial.println("%");
  }
  //output for the sound intensity sensor
  Serial.print(", ");
  sound = analogRead(Sound_Sensor);
  Serial.println(sound);
  
}
