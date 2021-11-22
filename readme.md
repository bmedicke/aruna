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
pip install psycopg[pool] # [binary] version not yet supported for ARM.
pip install black
```

### running it

```sh
# start db and adminer:
docker-compose up -d

# start backend:
./backend.py
```

## notifications

<details><summary>how to notify on changes</summary>

**create new demo table**

```sql
DROP TABLE "demo";
CREATE TABLE "demo" (
  "number" integer NOT NULL
);
```

**define trigger function**

```sql
CREATE OR REPLACE FUNCTION notify() RETURNS TRIGGER AS
$$
BEGIN
PERFORM pg_notify('table_changed', 'payload');
RETURN new;
END
$$
LANGUAGE plpgsql
```

**attach trigger to table**

```sql
DROP TRIGGER "notify_update_insert" ON "demo";
CREATE TRIGGER "notify_update_insert"
BEFORE
INSERT OR UPDATE OR DELETE
ON "demo"
FOR EACH ROW
EXECUTE FUNCTION notify();
```

**listen to changes**

```sh
./notifications.py
```

**change the table**

```sql
INSERT INTO "demo" ("number")
VALUES ('1');
```

* [more info](https://www.postgresql.org/docs/12/plpgsql-overview.html)

**or send on the channel directly**

```sh
psql 'dbname=postgres hostaddr=192.168.8.212 user=postgres password=postgres' -c "notify table_changed, 'payload'"
```

</details>

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
	* [empty queries and performance impact](https://stackoverflow.com/questions/21117431/how-to-receive-automatic-notifications-about-changes-in-tables)

## useful repos

* https://github.com/bokub/rgb-light-card (Lovelace custom card for RGB lights)
