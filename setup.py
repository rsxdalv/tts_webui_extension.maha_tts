import setuptools

setuptools.setup(
    name="tts_webui_extension.maha_tts",
    packages=setuptools.find_namespace_packages(),
    version="0.1.0",
    author="rsxdalv",
    description="Maha TTS allows generating speech from text using the MahaTTS model.",
    url="https://github.com/rsxdalv/tts_webui_extension.maha_tts",
    project_urls={},
    scripts=[],
    install_requires=[
        "maha-tts @ https://github.com/rsxdalv/MahaTTS/releases/download/v1.0.0/maha_tts-1.0.0-py3-none-any.whl",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

