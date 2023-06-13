import gradio as gr
import numpy as np
import librosa
import soundfile as sf
import requests
import torch
import torchaudio

# from PIL import Image

# pipeline = pipeline(task="automatic-speech-recognition", model="BALAKA/wav2vec2-large-xlsr-53-th-main")

API_URL = "https://api-inference.huggingface.co/models/BALAKA/wav2vec2-large-xlsr-53-th-swear-words"
headers = {"Authorization": "Bearer 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"}
# processor = Wav2Vec2Processor.from_pretrained("airesearch/wav2vec2-large-xlsr-53-th")
# model = Wav2Vec2ForCTC.from_pretrained("BALAKA/wav2vec2-large-xlsr-53-thai")
demo = gr.Blocks()


def check(sentence):
    found = []
    negative = ["กระดอ", "กระทิง", "กระสัน", "กระหรี่", "กรีด", "กวนส้นตีน", "กะหรี่", "กินขี้ปี้เยี่ยว", "ขายตัว", "ขี้", "ขโมย", "ข่มขืน", "ควย", "ควาย", "คอขาด", "ฆ่า", "จังไร", "จัญไร", "ฉิบหาย", "ฉี่", "ชั่ว", "ชาติหมา", "ชิงหมาเกิด", "ชิบหาย", "ช้างเย็ด", "ดาก", "ตอแหล", "ตัดหัว", "ตัดหำ", "ตาย", "ตีกัน", "ทรมาน", "ทาส", "ทุเรศ", "นรก", "บีบคอ", "ปากหมา", "ปี้กัน", "พ่อง", "พ่อมึง", "ฟักยู", "ฟาย", "ยัดแม่", "ยิงกัน", "ระยำ", "ดอกทอง", "โสเภณี", "ล่อกัน", "ศพ", "สถุล", "สทุน", "สัด", "สันดาน", "สัส", "สาด", "ส้นตีน", "หน้าตัวเมืย", "ส้นตีน", "หมอย", "หรรม", "หัวแตก", "หำ", "หี", "อนาจาร", "อัปปรี", "อีช้าง", "อีปลาวาฬ", "อีสัด", "อีหน้าหี", "อีหมา", "ห่า", "อับปรี", "เฆี่ยน", "เงี่ยน", "เจี๊ยว", "เชี่ย", "เด้า", "เผด็จการ", "เยี่ยว", "เย็ด", "เลือด", "เสือก", "เหล้า", "เหี้ย", "เอากัน", "แดก", "แตด", "แทง", "แม่ง", "แม่มึง", "แรด", "โคตร", "โง่", "โป๊", "โรคจิต", "ใจหมา", "ไอเข้", "ไอ้ขึ้หมา", "ไอ้บ้า", "ไอ้หมา", "เวร", "เวน"]
    negative = list(dict.fromkeys(negative))
    for i in negative:
        if sentence.find(i) != -1:
            found.append(i)
    return found


def tran_script(speech):
    if speech is not None:
        inputs = processor(speech, sampling_rate=16_000,
                           return_tensors="pt", padding=True)
        logits = model(inputs.input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        predicted_sentence = processor.batch_decode(predicted_ids)
        return predicted_sentence
    else:
        path = glob('/content/split_*.mp3')
        sentence = []
        for i in range(len(path)):
            now_path = f'/content/split_{i+1}.mp3'
            speech, sample_rate = librosa.load(now_path)
            inputs = processor(speech, sampling_rate=16_000,
                            return_tensors="pt", padding=True)
            logits = model(inputs.input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)
            predicted_sentence = processor.batch_decode(predicted_ids)
            sentences.append(predicted_sentence)
        return sentences
            
            


def split_file(speech, sample_rate):
    buffer = 5 * sample_rate
    samples_total = len(speech)
    samples_wrote = 0
    counter = 1

    while samples_wrote < samples_total:

        if buffer > (samples_total - samples_wrote):
            buffer = samples_total - samples_wrote

        block = speech[samples_wrote: (samples_wrote + buffer)]
        out_filename = "split_" + str(counter) + ".mp3"

        sf.write(out_filename, block, sample_rate)
        counter += 1
        samples_wrote += buffer


def resample(speech, sample_rate):
    if sample_rate != 16000:
        #speech = librosa.resample(speech, orig_sr=sample_rate, target_sr=16000)
        resampler=torchaudio.transforms.Resample(sample_rate, 16000)
    return resampler(speech)[0].numpy()


def process(file_path):
    file_path = '/content/ben10.mp3'
    speech, sample_rate = torchaudio.load(file_path)
    speech = resample(speech, sample_rate)
    if librosa.get_duration(filename=file_path) <= 5:
        sentence = tran_script(speech)
        sentence = str(sentence).replace(' ', '').strip("[]grt")
        return '[0.00-0.05] found : ' + check(sentence)
    split_file(speech, sample_rate)
    # sentence = tran_script(None)
    return 'hi'
    


def flip_text(x):
    return x[::-1]


with demo:
    gr.Markdown("Select your input type.")
    with gr.Tabs():
        with gr.TabItem("From your voice."):
            with gr.Row():
                voice = gr.Audio(source="microphone", type="filepath",
                                 optional=True, label="Démarrer l'enregistrement")
                voice_output = gr.Textbox()
            text_button1 = gr.Button("Flip")
        with gr.TabItem("From youtube"):
            with gr.Row():
                text_input2 = gr.Textbox()
                text_output2 = gr.Textbox()
            text_button2 = gr.Button("Flip")
        with gr.TabItem("From twitch"):
            with gr.Row():
                text_input3 = gr.Textbox()
                text_output3 = gr.Textbox()
            text_button3 = gr.Button("Flip")

    text_button1.click(process, inputs=voice, outputs=voice_output)
    text_button2.click(flip_text, inputs=text_input2, outputs=text_output2)
    text_button3.click(flip_text, inputs=text_input3, outputs=text_output3)

demo.launch(share=True)
