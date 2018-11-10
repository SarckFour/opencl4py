def read(filename):
    #todo exept FNFE
    import os.path as show
    f = open(show.realpath("../src/purecl/common/"+filename))
    out = f.read()
    f.close()
    return out