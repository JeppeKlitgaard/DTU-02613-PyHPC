import sys
from pathlib import Path
import numpy as np
from PIL import Image
CELEBA_DIR = Path("/dtu/projects/02613_2024/data/celeba/images/")
EXERCISE_DIR = Path(__file__).resolve().parent

def huehist(image):
    bins = np.linspace(0, 255, 64 + 1)
    hsv_image = np.asarray(Image.fromarray(image).convert('HSV'))
    hue_values = hsv_image[:, :, 0].reshape(-1)
    hue_hist = np.histogram(hue_values, bins)[0]
    return hue_hist

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <filename>")
        sys.exit(1)

    i = int(sys.argv[1]) - 1
    i_str = str(i * 1000).zfill(6)

    job_dir = CELEBA_DIR / f"{i_str}"
    assert job_dir.exists(), f"Directory {job_dir} does not exist"
    assert job_dir.is_dir(), f"{job_dir} is not a directory"

    image_paths = list(job_dir.glob("*.jpg"))

    hist_arr = np.zeros((len(image_paths), 64), dtype=np.int32)
    for j, path in enumerate(image_paths):
        image = Image.open(path)
        image_arr = np.array(image)
        hue_hist = huehist(image_arr)

        hist_arr[j] = hue_hist

    summed_hist = np.sum(hist_arr, axis=0)

    np.save(EXERCISE_DIR / f"subhist_{i_str}.npy", summed_hist)