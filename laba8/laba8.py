from PIL import Image
import os

def convert_to_ico(image_path):
  try:
    if not os.path.exists(image_path):
      raise FileNotFoundError(f"Изображение не найдено по пути: {image_path}")

    img = Image.open(image_path)
    base, ext = os.path.splitext(image_path)
    img.save(base + ".ico")
    print(f"Изображение успешно конвертировано в .ICO и сохранено по пути: {base + '.ico'}")

  except FileNotFoundError as e:
    print(f"Ошибка: {e}")
  except IOError as e:
    print(f"Ошибка при обработке изображения: {e}")
  except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

image_path = "python.jpg"
convert_to_ico(image_path)

