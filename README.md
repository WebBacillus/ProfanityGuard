# ProfanityGuard

  ปัจจุบันอาชีพ youtuber หรือ streamer ที่กำลังเป็นที่นิยมนั้นได้สร้างสรรค์ผลงานของพวกเขาผ่านแพลตฟอร์ม youtube แต่พวกเขาบางท่านก็ต้องประสบปัญหา คลิปวีดีโอติดเหลือง หรือ ติดแดง (ติดเหลือง: ผู้ลงโฆษณาทุกรายแสดงโฆษณาในเนื้อหาของคุณได้ในจำนวนจำกัดหรือไม่ได้เลย ติดแดง: คุณเปิดการสร้างรายได้แล้ว แต่วิดีโอไม่มีสิทธิ์สร้างรายได้เนื่องจากมีการร้องเรียนการละเมิดลิขสิทธิ์ อ้างอิงจาก [support.google](https://support.google.com/youtube/answer/7561938?hl=th). ทำให้ขาดรายได้เพียงเพราะการสร้างความบันเทิงให้กับผู้ชมของเขานั้นมีคำหยาบเพียงไม่กี่คำในคลิปวีดีโอ
<br/>
<p align="center" style="flex-direction:column;">
  <img src=https://github.com/webbalaka/ProfanityGuard/assets/108358070/829e97e0-9b19-4975-9655-cdf6af866607)/>
</p>
<br/>
<p align="center">
  <img src=https://github.com/webbalaka/ProfanityGuard/assets/108358070/fde8bb83-4c2c-456c-9556-60562a30462a)/>
</p>
<br/>
<p align="center">
  <img src=https://github.com/webbalaka/ProfanityGuard/assets/108358070/5a301ca5-df09-4b15-bcc7-d6ad406de854)/>
</p>
<br/>
<p align="center">
  <img src=https://github.com/webbalaka/ProfanityGuard/assets/108358070/edb3818b-cede-4cfa-81b8-257da996c5d2)/>
</p>
<br/>
<p>
 จากตัวอย่างที่กล่าวมาข้างต้นแสดงให้เห็นว่ามี youtuber หลายท่านกำลังประสบปัญหานี้ ผมจึงสนใจการแก้ปัญหานี้โดยใช้ Machine learning ตรวจสอบคำหยาบทั้งหมดในวีดีโอก่อน เพื่อแก้ไขคำที่สุ่มเสี่ยงที่จะก่อให้เกิดปัญหานี้และช่วยย่นระยะเวลาสำหรับคนตัดต่อให้แก้ไขคำหยาบได้อย่างรวดเร็ว  
<p/>

โดย ProfanityGuard เป็น Machine learning ที่ต่อยอดมาจาก pretrain model อีกทีนึงนั่นก็คือ [airesearch/wav2vec2-large-xlsr-53-th](https://huggingface.co/airesearch/wav2vec2-large-xlsr-53-th) โดยมีจุดมุ่งหมายหลักเพื่อแก้ปัญหาปัญหา youtuber หรือ streamer ที่ประสบปัญหา คลิปวีดีโอติดเหลือง หรือ ติดแดง โดยอาศัยการถอดความจากเสียงภาษาไทย (Automatic Speech Recognition; ASR) ที่ถูกเทรนบนข้อมูล [Common Voice 7.0](https://commonvoice.mozilla.org/en/datasets) แล้วมา brute force เพื่อตรวจสอบคำหยาบอีกที โดยให้ผลลัพธ์ที่ดีกว่า pretrain model ประมาณ 2 เท่า เมื่อเทียบกับ WER CER และ F1-Score

สามารถอ่านเพิ่มเติมได้ที่ [ProfanityGuard ตรวจจับคำหยาบด้วย AI ก่อนนำไปลง Youtube](https://medium.com/@webbalaka/profanityguard-%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%84%E0%B8%B3%E0%B8%AB%E0%B8%A2%E0%B8%B2%E0%B8%9A%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-ai-%E0%B8%81%E0%B9%88%E0%B8%AD%E0%B8%99%E0%B8%99%E0%B8%B3%E0%B9%84%E0%B8%9B%E0%B8%A5%E0%B8%87-youtube-792c09c027ff)  
หรือสามารถทดลองใช้โมเดลได้ที่ [Huggingface space](https://huggingface.co/spaces/BALAKA/ProfanityGuard) หรือ [Google Colaboratory](https://colab.research.google.com/drive/1pzTpSPe_rHqBecO_knrF1eD8YKQoZBbC?authuser=1#scrollTo=WEFsRrPF0Fbp)
