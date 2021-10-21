from gtts import gTTS

if __name__ == '__main__':
    sText = "강의 시작 1분 전입니다. 출석 해주세요."
    tts = gTTS(text=sText, lang='ko',slow=False)
    sSaveFile = "time_1.mp3"
    tts.save(sSaveFile)
    print(sSaveFile+"file saved!")

    