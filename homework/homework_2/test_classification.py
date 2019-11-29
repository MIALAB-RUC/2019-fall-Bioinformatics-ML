#encoding:utf-8

#from network import Network
from BPNN import BPNNClassification
import StudentdataLoader


def test():
    train_data, test_data = StudentdataLoader.load_data()
    # bp = Network([4, 15, 3])
    # bp.SGD(train_data, 10000, 10, 0.5, test_data=test_data)

    bp = BPNNClassification([3,5, 2])
    bp.MSGD(train_data, 500, 2, 0.5, test_data=test_data)

test()
