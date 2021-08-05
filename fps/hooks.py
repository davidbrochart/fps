from enum import Enum

import pluggy
from fastapi import APIRouter

from .config import PluginModel


class HookType(Enum):
    ROUTER = "fps_router"
    CONFIG = "fps_config"


@pluggy.HookspecMarker(HookType.ROUTER.value)
def router() -> APIRouter:
    pass


def register_router(r: APIRouter):
    def router_callback() -> APIRouter:
        return r

    return pluggy.HookimplMarker(HookType.ROUTER.value)(
        function=router_callback, specname="router"
    )


@pluggy.HookspecMarker(HookType.CONFIG.value)
def config() -> PluginModel:
    pass


def register_config(config_model: PluginModel):
    def config_callback() -> PluginModel:
        return config_model

    return pluggy.HookimplMarker(HookType.CONFIG.value)(
        function=config_callback, specname="config"
    )


@pluggy.HookspecMarker(HookType.CONFIG.value)
def plugin_name() -> str:
    pass


def register_plugin_name(plugin_name: str):
    def plugin_name_callback() -> str:
        return plugin_name

    return pluggy.HookimplMarker(HookType.CONFIG.value)(
        function=plugin_name_callback, specname="plugin_name"
    )
