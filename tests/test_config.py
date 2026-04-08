import numpy as np

# with the shape of CHW.
test_rgb_pixels = np.array([
        [[0,100,200,255],
         [0,100,200,255],
         [0,100,200,255],
         [0,100,200,255]],

        [[0,100,200,255],
         [0,100,200,255],
         [0,100,200,255],
         [0,100,200,255]],

        [[0,100,200,255],
         [0,100,200,255],
         [0,100,200,255],
         [0,100,200,255]]
    ]
)

# with the shape of [1,1,256]. To generate grayscale pictures.
test_oneline_pixels = np.arange(0,255, dtype=np.uint8)
test_oneline_pixels = np.array([test_oneline_pixels, test_oneline_pixels]).transpose()
def get_current_file_dir():
    '''
    Get the parent directory of the current file.
    '''
    from pathlib import Path
    filepath = Path(__file__).resolve()
    return filepath.parent

BASE_DIR = get_current_file_dir()
test_picture_path = f'{BASE_DIR}/images/stranthen.jpg'
test_grayscale_picture_path = f'{BASE_DIR}/images/grayscale.jpg'
another_test_picture_path = f'{BASE_DIR}/images/building.jpg'

test_style_picture_paths = [
    f'{BASE_DIR}/images/test1.jpg',
    f'{BASE_DIR}/images/test2.jpg',
    f'{BASE_DIR}/images/test3.jpg'
]
