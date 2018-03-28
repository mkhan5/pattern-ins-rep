import os
import fnmatch
class LinesMod:
    def __init__(self):
        pass

    def replaceData(self, filename, start_lineno, end_lineno, text_from_file):
        self.filename = filename
        self.start_lineno = start_lineno
        self.end_lineno = end_lineno
        self.text_from_file = text_from_file

        input_data = [line.strip() for line in open(self.filename,'r')]
        replace_data = [line.strip() for line in open(self.text_from_file,'r')]
        input_data[start_lineno-1:end_lineno] = replace_data
        fp = open(filename, 'w')
        fp.writelines( "%s\n" % item for item in input_data )
        fp.close()

    def insertDataTop(self, filename,text_from_file):
        self.filename = filename
        self.text_from_file = text_from_file

        input_data = [line.strip() for line in open(self.filename,'r')]
        append_data = [line.strip() for line in open(self.text_from_file,'r')]
        input_data[:0] = append_data
        fp = open(filename, 'w')
        fp.writelines( "%s\n" % item for item in input_data )
        fp.close()

if __name__ == "__main__":
    main_file = os.getcwd()+'/gemv/gemv.c'
    data_file = os.getcwd()+'/temp/temp.c'
    linesmod = LinesMod()

    fileCount = 0
    rootdir = os.getcwd()
    fileList = []
    for root, dirnames, filenames in os.walk(rootdir):
        for filename in fnmatch.filter(filenames, '*.c'):
            if not (filename == "polybench.c"):
                fileList.append(os.path.join(root, filename))
                fileCount = fileCount + 1
    print fileCount

    for one_file in fileList:
       linesmod.insertDataTop(one_file,data_file)
        #linesmod.replaceData(main_file,1,4,data_file)
