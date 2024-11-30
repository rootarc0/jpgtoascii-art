import gi
from PIL import Image

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class ASCIIArtConverter(Gtk.Window):
    def __init__(self):
        super().__init__(title="Конвертер изображений в ASCII арт")
        self.set_size_request(400, 300)

        # Создаем элементы интерфейса
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.file_chooser = Gtk.FileChooserButton("Выберите изображение", Gtk.FileChooserAction.OPEN)
        self.file_chooser.set_filter(self.create_image_filter())
        self.box.pack_start(self.file_chooser, True, True, 0)

        self.convert_button = Gtk.Button(label="Конвертировать в ASCII")
        self.convert_button.connect("clicked", self.on_convert_clicked)
        self.box.pack_start(self.convert_button, True, True, 0)

        self.save_button = Gtk.Button(label="Сохранить ASCII арт")
        self.save_button.connect("clicked", self.on_save_clicked)
        self.box.pack_start(self.save_button, True, True, 0)

        self.text_view = Gtk.TextView()
        self.text_view.set_editable(False)
        self.box.pack_start(self.text_view, True, True, 0)

        self.ascii_art = ""  # Переменная для хранения ASCII арта

        self.show_all()

    def create_image_filter(self):
        filter = Gtk.FileFilter()
        filter.set_name("Изображения")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpeg")
        return filter

    def on_convert_clicked(self, widget):
        file_path = self.file_chooser.get_filename()
        if file_path:
            self.ascii_art = self.convert_image_to_ascii(file_path)
            self.display_ascii_art(self.ascii_art)

    def convert_image_to_ascii(self, file_path):
        # Открываем изображение
        img = Image.open(file_path)
        
        # Сохраняем соотношение сторон
        aspect_ratio = img.height / img.width
        new_width = 100
        new_height = int(aspect_ratio * new_width * 0.55)  # Уменьшаем высоту для корректного отображения
        img = img.resize((new_width, new_height))
        img = img.convert("L")  # Конвертируем в градации серого

        # Определяем символы для ASCII
        ascii_chars = "@%#*+=-:. " * 2  # Увеличиваем количество символов
        ascii_art = ""

        for y in range(img.height):
            for x in range(img.width):
                pixel = img.getpixel((x, y))
                ascii_art += ascii_chars[pixel // 32]  # Разбиваем на 8 уровней
            ascii_art += "\n"

        return ascii_art

    def display_ascii_art(self, ascii_art):
        buffer = self.text_view.get_buffer()
        buffer.set_text(ascii_art)

    def on_save_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Сохранить ASCII арт", self, Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            file_path = dialog.get_filename()
            with open(file_path, 'w') as f:
                f.write(self.ascii_art)

        dialog.destroy()

# Запуск приложения
win = ASCIIArtConverter()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

