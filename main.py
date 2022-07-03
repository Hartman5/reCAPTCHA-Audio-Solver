#No driver config added so you can configure to your liking works with selenium, seleniun-wire, undetected_chromedriver, thats all thats tested.
#Optimize this to however but only call function solve() when the captcha is present
def solve():
  try:
    frames = driver.find_elements_by_tag_name("iframe")
    recaptcha_control_frame = None
    recaptcha_challenge_frame = None
    frames = driver.find_elements_by_tag_name("iframe")
    recaptcha_control_frame = None
    recaptcha_challenge_frame = None
    for index, frame in enumerate(frames):
            if re.search('reCAPTCHA', frame.get_attribute("title")):
                recaptcha_control_frame = frame
            if re.search('recaptcha challenge', frame.get_attribute("title")):
                recaptcha_challenge_frame = frame
    if not (recaptcha_control_frame and recaptcha_challenge_frame):
            pass
    while True:
        try:
            frames = driver.find_elements_by_tag_name("iframe")
            driver.switch_to.frame(recaptcha_control_frame)
            driver.find_element_by_class_name("recaptcha-checkbox-border").click()
            break
        except:
            pass
    while True:
        try:
            driver.switch_to.default_content()
            frames = driver.find_elements_by_tag_name("iframe")
            driver.switch_to.frame(recaptcha_challenge_frame)
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_id("recaptcha-audio-button").click()
            driver.switch_to.default_content()
            frames = driver.find_elements_by_tag_name("iframe")
            driver.switch_to.frame(recaptcha_challenge_frame)
            break
        except:
            pass
    while True:
        try:
            src = driver.find_element_by_id("audio-source").get_attribute("src")
            path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
            path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))
            urllib.request.urlretrieve(src, path_to_mp3)
            sound = pydub.AudioSegment.from_mp3(path_to_mp3)
            sound.export(path_to_wav, format="wav")
            sample_audio = sr.AudioFile(path_to_wav)
            break
        except:
            pass
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)
    driver.find_element_by_id("audio-response").send_keys(key.lower())
    driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
    os.system('del /f sample.mp3')
    os.system('del /f sample.wav')
    return True
  except:
    return False
