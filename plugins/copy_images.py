import os
import shutil

def copy_article_images(generator):
    # Правильно: используем generator.articles вместо pelican.articles
    for article in generator.articles:
        article_path = os.path.dirname(article.source_path)
        images_path = os.path.join(article_path, 'images')
        if os.path.exists(images_path):
            output_path = os.path.join(generator.output_path, 'blog', article.slug, 'images')
            os.makedirs(output_path, exist_ok=True)
            for image in os.listdir(images_path):
                src = os.path.join(images_path, image)
                dst = os.path.join(output_path, image)
                shutil.copy2(src, dst)

def register():
    try:
        from pelican import signals
        # Подключаем к правильному сигналу - после генерации статей
        signals.article_generator_finalized.connect(copy_article_images)
    except ImportError:
        pass