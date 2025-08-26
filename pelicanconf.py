# ====================
# Основные настройки
# ====================
AUTHOR = 'admin'
SITENAME = 'Портфолио'
SITEURL = ""  # Для разработки оставить пустым, для продакшена указать домен
PATH = "content"  # Корневая папка с контентом
TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'ru'

# ====================
# Настройки тем и путей
# ====================
THEME = 'themes/my_theme'

# Пути к контенту
ARTICLE_PATHS = ['articles']  # Статьи блога (убрал 'content', так как это дублирование)
PAGE_PATHS = ['pages']       # Отдельные страницы
STATIC_PATHS = ['images', 'static', 'pdfs']  # Статические файлы (картинки, CSS/JS)

# ====================
# Настройки URL
# ====================
# Статьи блога
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

# Страницы
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Главная страница
INDEX_SAVE_AS = 'index.html'
DISPLAY_ARTICLES_ON_HOMEPAGE = False  # Не показывать статьи на главной
DISPLAY_PAGES_ON_MENU = True          # Показывать страницы в меню

# ====================
# Навигация
# ====================
MENUITEMS = [
    ('Главная', '/'),
    ('Обо мне', '/about/'),
    ('Резюме', '/resume/'),
    ('Блог', '/blog/'),
    ('Проекты', '/projects/'),
    ('Контакты', '/contacts/')
]

# ====================
# Шаблоны
# ====================
TEMPLATE_PAGES = {
    'home.html': 'index.html',       # Главная страница
    'blog_index.html': 'blog/index.html'  # Архив блога
}

# ====================
# Дополнительные настройки
# ====================
# Отключение RSS-лент (для портфолио обычно не нужны)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Пагинация
DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 2

# Для времени чтения
READTIME = True

# Для социальных кнопок (опционально)
SOCIAL_SHARE = True

# Скрыть ненужные страницы
DIRECT_TEMPLATES = ['categories', 'authors', 'archives', 'tags']

# Для разработки (раскомментировать при необходимости)
# RELATIVE_URLS = True

# Расчет времени чтения
def calculate_readtime(content):
    words_per_minute = 200
    words = len(content.split())
    return max(1, round(words / words_per_minute))

JINJA_FILTERS = {
    'readtime': calculate_readtime
}

PLUGINS = ['plugins.copy_images']
PLUGIN_PATHS = ['.']  # Если плагин в корне проекта

# Настройки для тегов
TAGS_URL = 'tags/{slug}/'
TAGS_SAVE_AS = 'tags/{slug}/index.html'
TAGS_FEED_ATOM = None  # или 'feeds/tag-{slug}.atom.xml' если нужны фиды
TAGS_FEED_RSS = None   # или 'feeds/tag-{slug}.rss.xml'

# Настройки для категорий (на всякий случай)
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'