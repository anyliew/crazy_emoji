from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage
from pydantic import Field

from meme_generator import (
    MemeArgsModel,
    MemeArgsType,
    ParserArg,
    ParserOption,
    add_meme,
)
from meme_generator.exception import TextOverLength, MemeFeedback
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"

# 图片编号（1~25）对应的杯子名称
variant_names = [
    "天使心",        # 1.png
    "清洗液",        # 2.png
    "纪念版圣修女",  # 3.png
    "啦啦队偶像",    # 4.png
    "偶像心跳",      # 5.png
    "杰士邦",        # 6.png
    "白丝壁女",      # 7.png
    "限定版圣修女",  # 8.png
    "琉璃子",        # 9.png
    "机械龙女",      # 10.png
    "萌新礼包",      # 11.png
    "神宫美优子",    # 12.png
    "水城不知火",    # 13.png
    "乳入娘",        # 14.png
    "纯洁臀",        # 15.png
    "紫域精灵",      # 16.png
    "桥本友希",      # 17.png
    "圣修女",        # 18.png
    "春奈纱希",      # 19.png
    "魔女之森",      # 20.png
    "新手礼包",      # 21.png
    "夏日琉璃子",    # 22.png
    "对魔忍",        # 23.png
    "杏奈",          # 24.png
    "空气玩法",      # 25.png
]

help_text = (
    "图片编号，0 为随机；1~25 对应："
    + "、".join(f"{i}={name}" for i, name in enumerate(variant_names, 1))
)


class Model(MemeArgsModel):
    number: int = Field(0, description=help_text)


args_type = MemeArgsType(
    args_model=Model,
    parser_options=[
        ParserOption(
            names=["-n", "--number"],
            args=[ParserArg(name="number", value="int")],
            help_text=help_text,
        ),
    ],
)


def fleshlight_random(images: list[BuildImage], texts: list[str], args: Model):
    total_num = 25
    if args.number == 0:
        frame_num = random.randint(1, total_num)  # 0 表示随机
    elif 1 <= args.number <= total_num:
        frame_num = args.number  # 编号即图片文件名（1~25）
    else:
        raise MemeFeedback(f"图片编号错误，请选择 1~{total_num}（0 为随机）")

    frame = BuildImage.open(img_dir / f"{frame_num}.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}の❤️最爱"

    # 为不同的背景图片设置不同的文本位置（bbox: x1, y1, x2, y2）
    text_positions = [
        (533, 39, 779, 140),    # 图片1.png的文本位置
        (13, 1039, 430, 1189),   # 图片2.png的文本位置
        (40, 110, 374, 207),    # 图片3.png的文本位置
        (686, 1100, 1200, 1200),   # 图片4.png的文本位置
        (55, 135, 812, 282),    # 图片5.png的文本位置
        (261, 31, 758, 91),     # 图片6.png的文本位置
        (566, 606, 764, 644),   # 图片7.png的文本位置
        (40, 110, 374, 207),    # 图片8.png的文本位置
        (26, 74, 380, 141),     # 图片9.png的文本位置
        (9, 708, 577, 790),     # 图片10.png的文本位置
        (43, 403, 328, 485),    # 图片11.png的文本位置
        (13, 1039, 428, 1191),  # 图片12.png的文本位置
        (331, 40, 797, 136),    # 图片13.png的文本位置
        (465, 5, 792, 87),      # 图片14.png的文本位置
        (840, 393, 1200, 464),  # 图片15.png的文本位置
        (799, 59, 1168, 211),   # 图片16.png的文本位置
        (52, 692, 334, 755),    # 图片17.png的文本位置
        (40, 110, 374, 207),    # 图片18.png的文本位置
        (252, 648, 649, 692),   # 图片19.png的文本位置
        (0, 1037, 339, 1106),   # 图片20.png的文本位置
        (93, 688, 493, 769),    # 图片21.png的文本位置
        (35, 111, 428, 210),    # 图片22.png的文本位置
        (35, 111, 428, 210),    # 图片23.png的文本位置
        (22, 638, 739, 737),    # 图片24.png的文本位置
        (305, 1, 800, 133),     # 图片25.png的文本位置（原 0.png）
    ]

    # 为不同的背景图片设置不同的字体颜色
    text_colors = [
        "white",        # 1. fleshlight_angel(天使心)
        "white",        # 2. fleshlight_cleaning_liquid(清洗液)
        "black",        # 3. fleshlight_commemorative_edition_saint_sister(纪念版圣修女)
        "white",        # 4. fleshlight_hoshino_alice(啦啦队偶像/拉拉队偶像)
        "black",        # 5. fleshlight_idol_heartbeat(偶像心跳)
        "black",        # 6. fleshlight_jissbon(杰士邦)
        "black",        # 7. fleshlight_kuileishushi(白丝壁女)
        "black",        # 8. fleshlight_limited_edition_saint_sister(限定版圣修女)
        "black",        # 9. fleshlight_liuli_zi(琉璃子)
        "white",        # 10. fleshlight_machinery(机械龙女/机械龙女EVA/机械龙女eva)
        "white",        # 11. fleshlight_mengxin_packs(萌新礼包)
        "white",        # 12. fleshlight_miyuko_kamimiya(神宫美优子)
        "white",        # 13. fleshlight_mizuki_shiranui(水城不知火)
        "black",        # 14. fleshlight_nrn(乳入娘)
        "white",        # 15. fleshlight_pure_buttocks(纯洁臀)
        "black",        # 16. fleshlight_purple_spirit(紫域精灵)
        "white",        # 17. fleshlight_qiaobenyouxi(桥本友希)
        "black",        # 18. fleshlight_saint_sister(圣修女)
        "white",        # 19. fleshlight_saki_haruna(春奈纱希)
        "black",        # 20. fleshlight_selena(魔女之森)
        "white",        # 21. fleshlight_starter_pack(新手礼包)
        "black",        # 22. fleshlight_summer_liuli_zi(夏日琉璃子)
        "black",        # 23. fleshlight_taimanin_asgi(对魔忍)
        "black",        # 24. fleshlight_xingnai(杏奈)
        "white",        # 25. fleshlight_air_play(空气玩法)（原 0.png）
    ]

    # 为不同的背景图片设置不同的头像位置和大小
    avatar_configs = [
        {"position": (65, 105), "size": (675, 675)},    # 图片1.png的头像配置
        {"position": (290, 20), "size": (920, 920)},    # 图片2.png的头像配置
        {"position": (202, 252), "size": (770, 770)},   # 图片3.png的头像配置
        {"position": (130, 180), "size": (920, 920)},   # 图片4.png的头像配置
        {"position": (340, 340), "size": (920, 920)},   # 图片5.png的头像配置
        {"position": (475, 180), "size": (180, 180)},   # 图片6.png的头像配置
        {"position": (499, 611), "size": (65, 65)},     # 图片7.png的头像配置
        {"position": (202, 252), "size": (770, 770)},   # 图片8.png的头像配置
        {"position": (145, 180), "size": (500, 500)},   # 图片9.png的头像配置
        {"position": (60, 110), "size": (680, 680)},    # 图片10.png的头像配置
        {"position": (15, 115), "size": (350, 350)},    # 图片11.png的头像配置
        {"position": (275, -10), "size": (950, 950)},   # 图片12.png的头像配置
        {"position": (320, 144), "size": (512, 512)},   # 图片13.png的头像配置
        {"position": (544, 326), "size": (230, 230)},   # 图片14.png的头像配置
        {"position": (-64, 81), "size": (860, 860)},    # 图片15.png的头像配置
        {"position": (107, 180), "size": (1000, 1000)}, # 图片16.png的头像配置
        {"position": (105, 75), "size": (630, 630)},    # 图片17.png的头像配置
        {"position": (202, 252), "size": (770, 770)},   # 图片18.png的头像配置
        {"position": (663, 575), "size": (125, 125)},   # 图片19.png的头像配置
        {"position": (140, 195), "size": (920, 920)},   # 图片20.png的头像配置
        {"position": (15, 185), "size": (580, 580)},    # 图片21.png的头像配置
        {"position": (210, 265), "size": (770, 770)},   # 图片22.png的头像配置
        {"position": (215, 222), "size": (780, 780)},   # 图片23.png的头像配置
        {"position": (130, 150), "size": (475, 475)},   # 图片24.png的头像配置
        {"position": (252, 133), "size": (300, 300)},   # 图片25.png的头像配置（原 0.png）
    ]

    # 根据选择的背景图片获取对应的文本位置、颜色和头像配置
    idx = frame_num - 1  # 转为 0-based 数组索引
    text_bbox = text_positions[idx]
    text_color = text_colors[idx]
    avatar_config = avatar_configs[idx]

    try:
        frame.draw_text(
            text_bbox,
            text,
            max_fontsize=100,
            min_fontsize=5,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
            fill=text_color,
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize(avatar_config["size"])
        # 6.png 需要把用户图片放在最上层（其余图片保持在下层）
        return frame.copy().paste(
            img,
            avatar_config["position"],
            alpha=True,
            below=frame_num != 6,
        )

    return make_jpg_or_gif(images, make)


add_meme(
    "fleshlight_random",
    fleshlight_random,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    args_type=args_type,
    keywords=["随机杯子"],
    date_created=datetime(2025, 9, 2),
    date_modified=datetime(2026, 10, 12),
)
