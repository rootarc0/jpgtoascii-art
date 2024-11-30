I made a converter jpg image to ASCII-art on python, i use Pillow
# How to use?
use in terminal (console) - python asciiart.py yourimg.jpg

# NEW VERSION
hey guys, I made a new version of the app, now it uses GTK! I'm using GNOME so it looks cool for me, I'll do it later with Qt

# Bags

1. Traceback (most recent call last):
  File "/home/superuser/asciiart.py", line 1, in <module>
    from PIL import Image
  
install the Pillow
`python3 -m venv myenv`
`source myenv/bin/activate` (On Linux)
`pip install pillow PyGObject`

2. Traceback (most recent call last):
  File "/home/user/asciiart.py", line 49, in <module>
    main(sys.argv[1])
  File "/home/user/asciiart.py", line 33, in main
    ascii_str = pixels_to_ascii(image)
                ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/superuser/asciiart.py", line 20, in pixels_to_ascii
    ascii_str += ASCII_CHARS[pixel // 25]  # Разбиваем на 10 уровней яркости
                 ~~~~~~~~~~~^^^^^^^^^^^^^
IndexError: string index out of range

It seems that the jpg image format is too large (Idk)

# Test

![изображение](https://github.com/user-attachments/assets/616fd31b-194a-45d7-808e-8ea07857ff2a)


