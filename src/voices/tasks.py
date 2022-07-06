import os
import torch
import uuid
import shutil
from celery import shared_task
from django.conf import settings
from voices.models import Record, RecordHistory


@shared_task
def generate_voice(user, text):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = settings.BASE_DIR / 'files/media/model.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ua/v3_ua.pt', local_file)

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    rate = 8000
    speaker = 'mykyta'

    generate_key = str(uuid.uuid4())

    audio_file = model.save_wav(text=text, speaker=speaker, sample_rate=rate)

    record = Record.objects.create(
        record_text=text,
        file=audio_file
    )

    shutil.move('test.wav', f'{settings.MEDIA_ROOT}/voices/test.wav')
    os.rename(f'{settings.MEDIA_ROOT}/voices/test.wav', f'{settings.MEDIA_ROOT}/voices/{generate_key}.wav')


    record_history = RecordHistory.objects.create(
        record=record,
        user=user
    )


