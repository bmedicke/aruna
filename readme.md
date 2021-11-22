# Aruna
LED strip control (with individual LEDs)

## backend

### setup

```sh
cd backend

# install docker:
curl -fsSL https://get.docker.com -o get-docker.sh
sh ./get-docker.sh
rm get-docker.sh

# install docker-compose and postgres:
apt install docker-compose postgresql -y

# create and activate virtual environment:
python3 -m venv env
source env/bin/activate

# on rpi4 you might get an error about multiple
# definitions while installing rpi.gpio,
# to avoid them use the flag:
export CFLAGS=-fcommon

# install libs:
pip install adafruit-blinka
pip install adafruit-circuitpython-neopixel
pip install psycopg2
```
### running it

```sh
# start db and adminer:
docker-compose up -d

# start backend:
./backend.py
```

## Power Circuit Diagramm

<img src="media/circuit_diagram_LEDs_power.jpg"></img>

## terminology

* **entity**
	* sensors, automations, switches, scenes
* **device**
	* physical objects (that might have multiple entities)

## useful links

* [Device Registry](https://developers.home-assistant.io/docs/device_registry_index/)
* [HA MQTT Light Schemas](https://www.home-assistant.io/integrations/light.mqtt/)
	* template: the one tasmota uses
	* default: no flashing, transitions
	* **[json](https://www.home-assistant.io/integrations/light.mqtt/#json-schema)**: all features
		* [demo usage](https://community.home-assistant.io/t/mqtt-add-on-works-but-no-discovery/241680)
	* [async-notifications with psycopg](https://www.psycopg.org/docs/advanced.html#asynchronous-notifications)
		* get notified of db-updates

## useful repos

* https://github.com/bokub/rgb-light-card (Lovelace custom card for RGB lights)
