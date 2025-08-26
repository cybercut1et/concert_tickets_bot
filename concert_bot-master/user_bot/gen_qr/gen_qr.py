import qrcode
from PIL import Image, ImageDraw, ImageFont
#todo pip install pillow

def qr_code_gen(text:str,ticket_number):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='purple', back_color='white')

    # Конвертируем изображение в режим RGBA для работы с текстом
    img = img.convert("RGBA")
    draw = ImageDraw.Draw(img)

    # Загружаем шрифт (можно заменить на путь к TTF-файлу, если нужно)
    font_path = "D:\\concert_bot\\user_bot\\gen_qr\\font\\EpilepsySans.ttf"
    font_size = 50
    font = ImageFont.truetype(font_path,font_size)


    # Добавляем номер билета (снизу слева)
    width, height = img.size
    draw.text((width/2-80, height - 65), f"№ {ticket_number}", fill="black", font=font)

    img.save("qr_ticket.png")


# Пример использования
qr_code_gen("hello", 1234)