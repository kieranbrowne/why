# import tensorflow as tf

def why(out,inmap):
    """Returns an explanation of output for input"""
    return out.op.inputs

