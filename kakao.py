import os

with open("m4s.txt", "w", encoding="utf8") as ing_file:
    b = int(input("마지막 번호를 입력하세요 : "))
    c = input("m4s 주소를 입력하세요 : ")
    quality = input("화질 선택(예:1080) : ")
    adr = c.split("?")
    adr1 = adr[0].rsplit("/", 2)
    lastNum = '{:0>6}'.format(b)

# audio
    audio_init = 'curl "' + adr1[0] + '/a_t0_96-44100/init.m4s?' + adr[1] + '\" -o "init.m4s"\n'
    audio_allFile = 'curl "' + adr1[0] + '/a_t0_96-44100/[000000-' + lastNum + '].m4s?' + adr[1] + '\" -o "#1.m4s"\n'

    # 메모장에 명령어 출력
    ing_file.write(audio_init)
    ing_file.write(audio_allFile)

    # 파일 다운로드 및 병합
    os.system(audio_init)
    os.system(audio_allFile)
    os.system("copy /b init.m4s + 0*.m4s audio.m4s")

# video
    if quality == '1080' :
        video_init = 'curl "' + adr1[0] + '/v_t0_HIGH4/init.m4s?' + adr[1] + '\" -o "init.m4s"\n'
        video_allFile = 'curl "' + adr1[0] + '/v_t0_HIGH4/[000000-' + lastNum + '].m4s?' + adr[1] + '\" -o "#1.m4s"\n' 
    elif quality == '720' :
        video_init = 'curl "' + adr1[0] + '/v_t0_HIGH/init.m4s?' + adr[1] + '\" -o "init.m4s"\n'
        video_allFile = 'curl "' + adr1[0] + '/v_t0_HIGH/[000000-' + lastNum + '].m4s?' + adr[1] + '\" -o "#1.m4s"\n' 
    elif quality == '480' :
        video_init = 'curl "' + adr1[0] + '/v_t0_MAIN/init.m4s?' + adr[1] + '\" -o "init.m4s"\n'
        video_allFile = 'curl "' + adr1[0] + '/v_t0_MAIN/[000000-' + lastNum + '].m4s?' + adr[1] + '\" -o "#1.m4s"\n' 
    elif quality == '360' :
        video_init = 'curl "' + adr1[0] + '/v_t0_BASE/init.m4s?' + adr[1] + '\" -o "init.m4s"\n'
        video_allFile = 'curl "' + adr1[0] + '/v_t0_BASE/[000000-' + lastNum + '].m4s?' + adr[1] + '\" -o "#1.m4s"\n'
    elif quality == '240' :
        video_init = 'curl "' + adr1[0] + '/v_t0_LOW/init.m4s?' + adr[1] + '\" -o "init.m4s"\n'
        video_allFile = 'curl "' + adr1[0] + '/v_t0_LOW/[000000-' + lastNum + '].m4s?' + adr[1] + '\" -o "#1.m4s"\n'
        
    ing_file.write(video_init)
    ing_file.write(video_allFile)
    
    os.system(video_init)
    os.system(video_allFile)
    os.system("copy /b init.m4s + 0*.m4s video.m4s")

# m4s를 mp4로 변환
    os.system(".\\ffmpeg -i video.m4s -c copy video.mp4")

# audio와 video 파일 합치기
    os.system(".\\ffmpeg -i video.mp4 -i audio.m4s -vcodec copy -acodec copy merge.mp4")


# 다운로드 한 파일 삭제
    init_file = "init.m4s"
    audio_file = "audio.m4s"
    video_file = "video.m4s"
    video_mp4 = "video.mp4"

    if os.path.isfile(init_file):
        os.remove(init_file)

    if os.path.isfile(audio_file):
        os.remove(audio_file)

    if os.path.isfile(video_file):
        os.remove(video_file)
    
    if os.path.isfile(video_mp4):
        os.remove(video_mp4)    

    for i in range(b+1):
        i = '{:0>6}'.format(i)
        m4s_file = i + ".m4s"
        if os.path.isfile(m4s_file):
            os.remove(m4s_file)

print("다운로드 완료")
os.system("pause>nul")