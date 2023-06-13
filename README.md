# ProfanityGuard
<p>
  ปัจจุบันอาชีพ youtuber หรือ streamer ที่กำลังเป็นที่นิยมนั้นได้สร้างสรรค์ผลงานของพวกเขาผ่านแพลตฟอร์ม youtube แต่พวกเขาบางท่านก็ต้องประสบปัญหา คลิปวีดีโอติดเหลือง หรือ ติดแดง (ติดเหลือง: ผู้ลงโฆษณาทุกรายแสดงโฆษณาในเนื้อหาของคุณได้ในจำนวนจำกัดหรือไม่ได้เลย ติดแดง: คุณเปิดการสร้างรายได้แล้ว แต่วิดีโอไม่มีสิทธิ์สร้างรายได้เนื่องจากมีการร้องเรียนการละเมิดลิขสิทธิ์ อ้างอิงจาก <a herf = "https://support.google.com/youtube/answer/7561938?hl=th">support.google</a>) ทำให้ขาดรายได้เพียงเพราะการสร้างความบันเทิงให้กับผู้ชมของเขานั้นมีคำหยาบเพียงไม่กี่คำในคลิปวีดีโอ
<p/>
<br/>
<p align="center">
  <img src=https://github.com/webbalaka/ProfanityGuard/assets/108358070/e8fb5f8a-9e56-4652-a441-302f3b12499d)/>
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
<p>
  โดย ProfanityGuard เป็น Machine learning เป็นโมเดลที่ต่อยอดมาจาก pretrain model อีกทีนึงนั่นก็คือ airesearch/wav2vec2-large-xlsr-53-th โดยอาศัยการถอดความจากเสียงภาษาไทย (Automatic Speech Recognition; ASR) ที่ถูกเทรนบนข้อมูล Common Voice 7.0 ประมาณ 133 ชั่วโมง แต่ปัญหาคือข้อมูลนั้นมีคำหยาบอยู่น้อย ผมได้เล็งเห็นปัญหานี้ผมจึงแก้ปัญหาด้วยการเพิ่ม Data คำหยาบเข้าไปและได้ทำการทดลอง
<p/>
