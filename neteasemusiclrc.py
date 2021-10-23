
import os
import sys
import json
from pprint import pprint


if __name__ == "__main__":
    cwd = os.getcwd()
    print(sys.argv[1:])

    for cf in sys.argv[1:]:

        # (cf1, cf2) = os.path.splitext(cf)
        # outputfilename = cf1+".lrc"

        dirname, filefullname = os.path.split(cf)
        filename, extendname = os.path.splitext(filefullname)
        outputfilename = os.path.join(cwd, filename+".lrc")
        print("Output File:", outputfilename)

        with open(cf, 'r', encoding="utf-8") as fp:
            jsonobj = json.load(fp)

        try:
            lrcstr = jsonobj["lrc"]["lyric"]
        except KeyError:
            lrcstr = None

        try:
            str_tlyric = jsonobj["tlyric"]["lyric"]
        except KeyError:
            str_tlyric = None

        try:
            str_romalrc = jsonobj["romalrc"]["lyric"]
        except KeyError:
            str_romalrc = None

        with open(outputfilename, 'w', encoding="utf-8") as fp:
            if lrcstr is not None:
                fp.write(lrcstr)
                fp.write("\n")
            if str_tlyric is not None:
                fp.write(str_tlyric)
                fp.write("\n")
            if str_romalrc is not None:
                fp.write(str_romalrc)
                fp.write("\n")

    os.system('pause')
