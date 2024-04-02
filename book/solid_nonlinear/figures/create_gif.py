import imageio
from PIL import Image

def create_gif(image_paths, gif_path, duration=0.5, loop=0, resize=None, transparent=False, frame_rate=None):
    """
    Create a GIF from a list of image paths.

    Args:
        image_paths (list): A list of file paths to the input images.
        gif_path (str): The file path to save the generated GIF.
        duration (float, optional): The duration (in seconds) to display each frame. Defaults to 0.5.
        loop (int, optional): The number of times the GIF should loop. Use 0 for infinite looping, 1 for no looping.
        resize (tuple, optional): Tuple containing the desired width and height for resizing images.
        transparent (bool, optional): If True, GIF will have a transparent background. Defaults to False.
        frame_rate (int, optional): The frame rate (in frames per second) of the GIF.

    Returns:
        None
    
    Example:
        >>> image_paths = ["image1.jpg", "image2.png", "image3.svg"]
        >>> gif_path = "output.gif"
        >>> duration = 0.5
        >>> loop = 0
        >>> resize = (200, 200)
        >>> transparent = True
        >>> frame_rate = 10
        >>> create_gif(image_paths, gif_path, duration=duration, loop=loop, resize=resize, transparent=transparent, frame_rate=frame_rate)
    """
    images = []
    for path in image_paths:
        with Image.open(path) as img:
            if resize:
                img = img.resize(resize)
            if transparent:
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")
            images.append(img)
    
    if frame_rate:
        kwargs = {'duration': duration, 'loop': loop, 'fps': frame_rate}
    else:
        kwargs = {'duration': duration, 'loop': loop}
    
    imageio.mimsave(gif_path, images, **kwargs)
    print(f"GIF saved at {gif_path}")


