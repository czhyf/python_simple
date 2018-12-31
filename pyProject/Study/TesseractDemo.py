#识别图片中的文字，拿到验证码
import tesserocr
from PIL import Image
image=Image.open('image——path')
print(tesserocr.image_to_text(image))
