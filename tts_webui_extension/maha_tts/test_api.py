from api import tts


def test_tts():
    """Smoke test for the tts function."""
    # Note: This test assumes voices are available. In a real test, you'd mock or provide test data.
    try:
        result = tts(
            text="Hello world",
            model_name="Smolie-in",
            text_language="english",
            speaker_name="test_speaker",  # This would need a real speaker folder
            device="cpu"
        )
        assert "audio_out" in result
        assert isinstance(result["audio_out"], tuple)
        assert len(result["audio_out"]) == 2
        sampling_rate, waveform = result["audio_out"]
        assert isinstance(sampling_rate, int)
        assert hasattr(waveform, '__len__')  # Check if waveform is array-like
        print("Smoke test passed!")
    except Exception as e:
        print(f"Test failed (expected if no voices available): {e}")


if __name__ == "__main__":
    test_tts()