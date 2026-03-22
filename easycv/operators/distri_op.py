
import numpy as np
import math

# region usual used distribution on pixels
class Distribution:
    @staticmethod
    def Uniform(shape: np.shape, dtype: np.dtype = np.float32):
        return np.ones(shape=shape, dtype=dtype)
    
    def Gaussian(loc, scale, shape: np.shape, dtype: np.dtype = np.float32):
        return np.random.normal(loc, scale, size=shape).astype(dtype)
# endregion

def PDF2CDF(pdf: np.array):
    assert pdf.ndim == 1, f'only support one-dim pdf'
    mask = np.tri(pdf.shape[0], pdf.shape[0], dtype=np.float32).transpose()
    return pdf @ mask

def PDF2LUT(src: np.array, dst: np.array):
    assert src.ndim == 1 and \
           dst.ndim == 1, f'only support one-dim histogram distribution'
    # normalization
    src = src / np.sum(src)
    dst = dst / np.sum(dst)

    def nearest(prob: float, cdf: np.array):
        return np.sum(cdf <= prob) - 1
    
    src_cdf = PDF2CDF(src)
    dst_cdf = PDF2CDF(dst)

    return np.array([
        nearest(src_cdf[i], dst_cdf)
        for i in range(src.shape[0])
    ])
