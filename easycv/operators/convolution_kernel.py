import numpy as np

class Kernel:
    @staticmethod
    def BlurKernel(size: tuple[int,int]):
        Kernel.assert_kernel_size(size)
        kernel = np.ones(shape=size)
        return kernel / np.sum(kernel)
    
    @staticmethod
    def GaussianBlurKernel(size: int, sigma: float = 1.0):
        Kernel.assert_kernel_size(size)
        meshgrid = np.linspace(-size//2, size//2, size)
        gaussian1d = np.exp(-(meshgrid**2)/(2*sigma**2))
        gaussian2d = np.outer(gaussian1d, gaussian1d)
        return gaussian2d / np.sum(gaussian2d)
    
    @staticmethod
    def ImpulseKernel(size: tuple[int, int], poss: list[tuple[int,int]]):
        Kernel.assert_kernel_size(size)
        kernel = np.zeros(shape=size)
        
        for pos in poss:
            assert pos[0] >= 0 and pos[0] < size[0] and \
                   pos[1] >= 0 and pos[1] < size[1], f'invalid position tuple {pos} of impulse kernel.'

            kernel[pos[0]][pos[1]] = 1

        return kernel / np.sum(kernel)
    
    @staticmethod
    def VerticalDifferenceKernel():
        return np.array([
            [0,-1,0],
            [0,2,0],
            [0,-1,0]
        ])
    
    @staticmethod
    def HorizontalDifferenceKernel():
        return np.array([
            [0,0,0],
            [-1,2,-1],
            [0,0,0]
        ])
    
    @staticmethod
    def DiagonalDifferenceKernel():
        return np.array([
            [-1,0,0],
            [0,2,0],
            [0,0,-1]
        ])
    
    @staticmethod
    def InverseDiagonalDifferenceKernel():
        return np.array([
            [0,0,-1],
            [0,2,0],
            [-1,0,0]
        ]) 

    @staticmethod
    def iskernel(kernel: np.array):
        return True
    
    @staticmethod
    def assert_kernel_size(size: tuple[int, int]|int):
        if isinstance(size, tuple):
            assert size[0] > 0 and size[0] % 2 == 1 and \
                   size[1] > 0 and size[1] % 2 == 1, f'invalid kernel size {size}'
        elif isinstance(size, int):
            assert size > 0 and size % 2 == 1, f'invalid kernel size {size}'
        