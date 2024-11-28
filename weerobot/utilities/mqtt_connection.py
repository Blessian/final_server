from typing import Any, List, Set, Dict, Tuple, Sequence, Union, Optional, Callable, Iterable, AsyncGenerator, cast
from contextlib import asynccontextmanager
import uuid
import time

from fastapi import FastAPI
from gmqtt import Client as MQTTClient
from fastapi_mqtt import FastMQTT, MQTTConfig


def get_fast_mqtt() -> FastMQTT:
    mqtt_config = MQTTConfig(
        host="broker.mqtt-dashboard.com",
        port=1883,
        keepalive=60,
        password="dnwnwjdqhr13",
        reconnect_retries=-1,
        reconnect_delay=10,
    )
    return FastMQTT(config=mqtt_config)

@asynccontextmanager
async def _lifespan(_app: FastAPI, fast_mqtt: FastMQTT) -> AsyncGenerator[None, Any]:
    while True:
        fast_mqtt.config.username = f"blessian_{uuid.uuid4()}"
        try:
            await fast_mqtt.mqtt_startup()
        except Exception as e:
            print(f"MQTT connection fail\nError: {e}\n\nTry again...")
            time.sleep(10)
        print("MQTT connection success!")
        yield
        break
    await fast_mqtt.mqtt_shutdown()