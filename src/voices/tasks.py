import os
import torch
from celery import shared_task
from django.conf import settings


@shared_task
def generate_voice():
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = settings.BASE_DIR / 'files/voices/model.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ua/v3_ua.pt',
                                       local_file)

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    text = "Привіт! Як справи?"
    rate = 48000
    speaker = 'mykyta'

    file_name = settings.BASE_DIR / 'files' / 'test' + ".wav"
    with open(file_name, 'wb') as f:
        model.save_wav(text=text, speaker=speaker, sample_rate=rate)

    return True