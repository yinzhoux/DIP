from .image import Image, from_array
import numpy as np

class ImageWarper:
    @staticmethod
    def standard_warp(image: Image, transform_matrix: np.ndarray, size: tuple[int,int]):
        '''
        Standard image warping.
        Parameters:
            @image: source image to warp.
            @transform_matrix: transfrom matrix from <image> to result image. Inversed inside this function.
            @size: the result image size.
        '''
        inversed_transform_matrix = ImageWarper.assert_transform_matrix_valid(transform_matrix)

        height, width = size
        x = np.arange(0, height)
        y = np.arange(0, width)
        xx, yy = np.meshgrid(x, y, indexing='ij')
        cod = np.array([xx, yy, np.ones((height, width))])
        cod = cod.transpose(1,2,0)

        assert cod.shape[-1] == 3 and inversed_transform_matrix.shape == (3,3), f'cod and matrix shape mismatch: {cod.shape} vs. {transform_matrix.shape}'
        remapped_cod = cod @ inversed_transform_matrix
        
        valid_height, valid_width = image.size
        valid_mask = (remapped_cod[...,0] >= 0) & (remapped_cod[..., 0] < valid_height) & \
                     (remapped_cod[...,1] >= 0) & (remapped_cod[..., 1] < valid_width)
        
        remapped_cod = remapped_cod.astype(np.uint)[:, :, :2] # (x, y, pos)

        safe_rows = np.clip(remapped_cod[..., 0], 0, height - 1)
        safe_cols = np.clip(remapped_cod[..., 1], 0, width - 1)


        new_pixels = [
            pixels[safe_rows, safe_cols]
            for pixels in image.pixels
        ]

        for i in range(image.bands_cnt):
            new_pixels[i][~valid_mask] = 0

        return from_array(pixels=np.array(new_pixels).transpose(1,2,0), image_type=image.type, image_name=f'warped_{image.image_name}')

    @staticmethod
    def assert_transform_matrix_valid(transform_matrix: np.ndarray):
        assert transform_matrix.shape == (3,3), f'invalid transformation matrix size {transform_matrix}.'

        inversed_transform_matrix = np.linalg.pinv(transform_matrix)

        return inversed_transform_matrix