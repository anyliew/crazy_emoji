from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def fleshlight_machinery(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}の挚❤️爱"
    #{name}挚爱❤️👩‍❤️‍💋‍👨{name}愛のカップ。
    try:
        frame.draw_text(
            (9, 708, 577, 790),
            text,
            fill=(255,255,255),
            max_fontsize=100,
            min_fontsize=20,
            valign="bottom",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((680, 680))
        return frame.copy().paste(img, (60, 110), alpha=True, below=True)

    return make_png_or_gif(images, make)


add_meme(
    "fleshlight_machinery",
    fleshlight_machinery,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["机械龙女","机械龙女EVA","机械龙女eva"],
    date_created=datetime(2024, 12, 21),
    date_modified=datetime(2026, 10, 12),
)
