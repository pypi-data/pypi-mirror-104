# ImitateTTS


An open-source deep learning TTS Engine for people with speech disoders
<br>
<br>
Based on [mozilla/TTS](https://github.com/mozilla/TTS)
<br>
## Installation
<br>
<br>
If you want to use the engine locally then the easiest way would be to use pip to install it:


```bash
pip install imitate
```


If you want to code then:


```bash
git clone https://github.com/AdityaCyberSafe/ImitateTTS.git
cd ImitateTTS
pip install -r requirements.txt
```

## Usage
<br>
<br>
Frontend: Refer to this <a href="https://github.com/AdityaCyberSafe/ImitateTTS/tree/main/imitatetts/server/README.md">link</a>.

CLI: 


```bash
imitate --text "Text for ImitateTTS" \
        --model_name "<type>/<language>/<dataset>/<model_name>" \
        --vocoder_name "<type>/<language>/<dataset>/<model_name>" \
        --out_path folder/to/save/output/
```
