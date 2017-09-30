# from keras import backend as K
# print(K.learning_phase())


# import pydot
#
# print(pydot.find_graphviz())


try:
    import pydot_ng as pydot

    pydot.Dot()
except ImportError:
    import pydot # if someone running with old installation