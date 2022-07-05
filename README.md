<p align="center"> 
   <img width="100%" src="https://user-images.githubusercontent.com/78701055/177348554-432bf332-3bfb-40eb-938b-dd0aa8bce460.png" alt="Irrigation Monitor"/> 
</p>


### <img height="30" src="https://irrigation-monitor-app.herokuapp.com/static/images/icon.png" alt=""/> About the project:
It is the IoT Based `Smart Agriculture & Automatic Irrigation System` with `Nodemcu ESP8266`. Agriculture plays a vital role in the development of agricultural countries. Some issues concerning agriculture have been always hindering the development of the country. Consequently, the only solution to this problem is smart agriculture by modernizing the current traditional methods of agriculture.

Hence the method is making agriculture smart using automation and IoT technologies. Internet of Things (IoT) enables various applications of crop growth monitoring and selection, automatic irrigation decision support, etc. We proposed ESP8266 IoT Automatic irrigation system to modernize and improve the productivity of the crop.

This project explains how to make IoT Smart Agriculture with Automatic Irrigation System using some simple sensors that are available in the market. We will use `Soil Moisture Sensor` to measure moisture content present in the soil. Similarly to measure Air Temperature and Humidity, we prefer `DHT11 Humidity Temperature Sensor`. Using a `5V Power relay` we will control the `Water Pump`. Whenever the sensor detects a low quantity of moisture in the soil, the motor turns on automatically. Hence, will automatically irrigate the field. Once the soil becomes wet, the motor turns off. You can monitor all this happening remotely via our website online from any part of the world.

### <img height="30" src="https://irrigation-monitor-app.herokuapp.com/static/images/icon.png" alt=""/> About the website:


![Screenshot from 2022-04-28 14-08-40](https://user-images.githubusercontent.com/78701055/165713255-90e30607-7d61-4c6d-9269-f7cb6b7d00a2.png)

A basic django based application which contacts with nodemcu collects the temperature, moisture and humidity data and plots the graph of it.
User has to register then login and give the id of the device in the website so that they can communicate with each other. <br>
The code for `nodemcu` is also given in this repo under the `IrrigationDevice` folder. <br>
You can give a unique id to your device and pass the same in website.
#### The website is hosted <a href="https://irrigation-monitor-app.herokuapp.com/" target="_blank">here</a>.

### <img height="30" src="https://irrigation-monitor-app.herokuapp.com/static/images/icon.png" alt=""/> Setting up the django project :

1. Creating virtual environment:
```bash
python -m venv venv
```
2. Activate virtual environment

Linux:
```bash
source venv/bin/activate
```
Windows:
```cmd
./venv/Scripts/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Apply migrations: 
```bash
python manage.py migrate
```
5. Collect static files : 
```bash
python manage.py collectstatic
```
6. Start the development server: 
```bash
python manage.py runserver
```


### <img height="30" src="https://irrigation-monitor-app.herokuapp.com/static/images/icon.png" alt=""/> Hardware components used:

|<img src="https://user-images.githubusercontent.com/78701055/165717011-2a3ec22e-2812-4dbf-9073-11a4ed1ea21e.jpg" alt="" width="100"/> | <img src="https://user-images.githubusercontent.com/78701055/165716988-27039939-38cd-4655-b87b-a9fa601956b8.jpg" alt="" width="100"/> |  <img src="https://user-images.githubusercontent.com/78701055/165717001-d27e5014-dbd8-402f-9706-3cf2bffdac07.jpg" alt="" width="100"/> | <img src="https://user-images.githubusercontent.com/78701055/165716965-ab8d125a-3fb3-4e2b-9265-11998659722a.jpg" alt="" width="100"/> | <img src="https://user-images.githubusercontent.com/78701055/165717195-119f7bd5-3436-4be9-974b-831ddf9f1141.jpeg" alt="" width="100"/> | <img src="https://user-images.githubusercontent.com/78701055/165722571-47ea42bf-d9ea-4c80-bcc8-b8947c829673.png" alt="" width="100"/> | <img src="https://user-images.githubusercontent.com/78701055/165722579-5a57fc60-37b1-4fae-9606-eb36b6851a13.jpg" alt="" width="100"/> |
|--|--|--|--|--|--|--|
|NodeMCU | Soil Moisture Sensor | DHT11 Sensor | 	Relay Module | Motor Pump | 12v battery | 12V to 5v converter |

### <img height="30" src="https://irrigation-monitor-app.herokuapp.com/static/images/icon.png" alt=""/> Final Design of circuit:

![WhatsApp Image 2022-04-28 at 2 53 07 PM](https://user-images.githubusercontent.com/78701055/165721822-8ce9857e-6f89-431b-96a5-bb17adb5e330.jpeg)





