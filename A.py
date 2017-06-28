def data_filter(x):
    return x>"2"

class A():
    def __init__(self, input_file):
        self.input_file = input_file

    def test(self,sc):
        rdd = sc.textFile(self.input_file).map(lambda x: x.split(",")).filter(lambda x: data_filter(x[0]))
        print rdd.take(5)
