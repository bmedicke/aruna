# Aruna
LED strip control (with individual LEDs)


## Power Circuit Diagramm

<img src="media/circuit_diagram_LEDs_power.jpg"></img>

## terminology

* **entity**
	* sensors, automations, switches, scenes
* **device**
	* physical objects (that might have multiple entities)

## useful links

* [Device Registry](https://developers.home-assistant.io/docs/device_registry_index/)
* [MA Light Schemas](https://www.home-assistant.io/integrations/light.mqtt/)
	* template: the one tasmota uses
	* default: no flashing, transitions
	* **json**: all features

## useful repos

* https://github.com/bokub/rgb-light-card (Lovelace custom card for RGB lights)
