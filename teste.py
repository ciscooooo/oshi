import os

if __name__ == '__main__':

    dir = "/home/cisco/Desktop/Oshi no Ko"

    for dir, subdirs, files in os.walk(dir):
        count = 0
        for f in sorted(files):
            chapter = os.path.basename(dir).split(" ")[1]
            os.rename(os.path.join(dir, f), os.path.join(dir, chapter + "_" + str(count) + ".png"))
            count += 1

#if os.stat(os.path.join(dir, f)).st_size == 28627 or os.stat(os.path.join(dir, f)).st_size == 26627:
                #os.remove(os.path.join(dir, f))

        