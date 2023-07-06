with open(r"./ST watch training.txt", encoding="UTF-8") as st_utts:
    st_utts = st_utts.readlines()

with open(r"./new training.txt", encoding="UTF-8", mode="w") as new_training:
    for utt in st_utts:
        utt = "[g:DeviceActionResult] " + utt
        new_training.write(utt)