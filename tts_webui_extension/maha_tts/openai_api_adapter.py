import os


def _get_maha_tts_voices() -> list[dict]:
    try:
        from .api import get_voices

        return get_voices()
    except ImportError:
        print("Maha TTS extension not available")
        return []


def _make_tts_fn():
    def tts_fn(
        model: str, text: str, voice: str | None, speed: float | None, params: dict
    ) -> dict:
        from .api import tts

        return tts(
            text=text,
            model_name=params.get("model_name", "Smolie-in"),
            text_language=params.get("text_language", "english"),
            speaker_name=voice,
            device=params.get("device", "auto"),
        )

    return tts_fn


def register():
    try:
        if os.environ.get("OPENAI_PROXY_HOST"):
            register_unsafe_outprocess()
        else:
            register_unsafe_inprocess()
    except Exception as e:
        print(f"Error registering Maha TTS API adapter: {e}")
        print("Maha TTS will not be available on the OpenAI API.")


def register_unsafe_inprocess():
    from tts_webui_extension.openai_tts_api.services.tts_adapter_registry import (
        register_tts_adapter,
    )

    register_tts_adapter("maha_tts", _make_tts_fn())


def register_unsafe_outprocess():
    from tts_webui_extension.openai_tts_api.harness import setup_oai_server

    setup_oai_server(
        tts_fn=_make_tts_fn(),
        get_voices_fn=_get_maha_tts_voices,
        model="maha_tts",
    )