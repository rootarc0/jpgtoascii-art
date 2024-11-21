from PIL import Image

# Символы для представления яркости
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  # Корректируем соотношение
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")  # Преобразуем в градации серого

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]  # Разбиваем на 10 уровней яркости
    return ascii_str

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Не удалось открыть изображение: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    # Форматируем строку ASCII
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join(ascii_str[i:i + img_width] for i in range(0, ascii_str_len, img_width))

    # Сохраняем результат в файл
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_img)

    print(ascii_img)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Использование: python ascii_art.py <путь_к_изображению>")
