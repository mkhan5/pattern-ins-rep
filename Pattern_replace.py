class LineReplace:
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

lr = LineReplace()
lr.replaceData("test.txt",1,3,"substring.txt")
#replaces data from start_lineno to end_lineno (start_lineno, end_lineno inclusive)
