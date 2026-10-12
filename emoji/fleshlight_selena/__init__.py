from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def fleshlight_selena(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}の❤️最愛"
    #{name}挚爱❤️👩‍❤️‍💋‍👨{name}愛のカップ。
    try:
        frame.draw_text(
            (0, 1037, 339, 1106),
            text,
            max_fontsize=100,
            min_fontsize=20,
            valign="bottom",
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((920, 920))
        return frame.copy().paste(img, (140, 195), alpha=True, below=True)

    return make_png_or_gif(images, make)


add_meme(
    "fleshlight_selena",
    fleshlight_selena,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["魔女之森"],
    date_created=datetime(2025, 3, 13),
    date_modified=datetime(2026, 10, 12),
)
