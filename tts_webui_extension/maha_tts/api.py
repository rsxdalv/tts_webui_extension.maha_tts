import glob
import os
import torch
from tts_webui.utils.manage_model_state import manage_model_state


VOICES_DIR = "voices/maha-tts"


def get_ref_clips(speaker_name):
    return glob.glob(os.path.join("./", VOICES_DIR, speaker_name, "*.wav"))


def get_voices():
    """Get available voices (speakers) for Maha TTS"""
    try:
        voices_dir = os.path.join("./", VOICES_DIR)
        if os.path.exists(voices_dir):
            files = os.listdir(voices_dir)
            dirs = [f for f in files if os.path.isdir(os.path.join(voices_dir, f))]
            return [{"value": d, "label": d} for d in dirs]
        return []
    except Exception:
        return []


@manage_model_state("maha_tts")
def preload_models_if_needed(model_name, device):
    from maha_tts.inference import load_models

    return load_models(name=model_name, device=device)


def tts(
    text,
    model_name,
    text_language,
    speaker_name,
    device="auto",
    **kwargs,
):
    from maha_tts.inference import infer_tts, config

    device = torch.device(
        device == "auto" and "cuda" if torch.cuda.is_available() else "cpu" or device
    )
    diff_model, ts_model, vocoder, diffuser = preload_models_if_needed(
        model_name=model_name, device=device
    )

    ref_clips = get_ref_clips(speaker_name)
    text_language = (
        torch.tensor(config.lang_index[text_language]).to(device).unsqueeze(0)
    )
    audio, sr = infer_tts(
        text, ref_clips, diffuser, diff_model, ts_model, vocoder, text_language
    )
    return {"audio_out": (sr, audio)}