import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-sua-chave-secreta-aqui-mude-em-producao'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imobiliaria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'imobiliaria.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===============================
# 🎨 CONFIGURAÇÕES JAZZMIN PREMIUM
# ===============================

JAZZMIN_SETTINGS = {
    # Identidade Premium
    "site_title": "Imobiliária Premium - Admin",
    "site_header": "Imobiliária Premium",
    "site_brand": "Premium Admin",
    "site_logo": None,
    "login_logo": None,
    "welcome_sign": "Bem-vindo ao Painel Premium",
    "copyright": "Imobiliária Premium © 2025 - Todos os direitos reservados",
    
    # Busca
    "search_model": ["core.Imovel", "core.Proprietario", "core.Cliente"],
    "user_avatar": None,
    
    # Menu Superior
    "topmenu_links": [
        {"name": "🏠 Home Admin", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "💎 Ver Site", "url": "/", "new_window": True},
        {"name": "📊 Relatórios", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
    
    # Menu do Usuário
    "usermenu_links": [
        {"name": "👤 Meu Perfil", "url": "admin:auth_user_change", "icon": "fas fa-user"},
        {"model": "auth.user"}
    ],
    
    # =====================================
    # 🎨 ÍCONES PREMIUM POR MODELO
    # =====================================
    "icons": {
        # Sistema de Autenticação
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user-shield",
        "auth.Group": "fas fa-users",
        
        # Modelos Principais (Premium)
        "core.imovel": "fas fa-gem",
        "core.proprietario": "fas fa-user-tie", 
        "core.cliente": "fas fa-handshake",
        
        # Modelos Auxiliares
        "core.fotoimovel": "fas fa-camera-retro",
        "core.precoporfinalidade": "fas fa-coins",
        "core.infracondominio": "fas fa-swimming-pool",
    },
    
    # Ícones padrão
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    # =====================================
    # 🎨 CONFIGURAÇÕES DE LAYOUT
    # =====================================
    
    # Modais e Customizações
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    
    # Layout dos Formulários
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible", 
        "auth.group": "vertical_tabs",
        "core.imovel": "horizontal_tabs",
        "core.cliente": "horizontal_tabs"
    },
    
    # =====================================
    # 🎨 TEMA E CORES PREMIUM
    # =====================================
    
    # Tema Principal
    "theme": "default",
    
    # Navegação e Layout
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",  # Cor da marca
    "accent": "accent-warning",     # Acento dourado
    "navbar": "navbar-dark bg-dark", # Navbar escura premium
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-warning",  # Sidebar escura com acento dourado
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    
    # =====================================
    # 🎨 CONFIGURAÇÕES AVANÇADAS
    # =====================================
    
    # Ordem dos aplicativos no menu
    "order_with_respect_to": ["core", "auth"],
    
    # Ocultar aplicativos
    "hide_apps": [],
    
    # Ocultar modelos específicos
    "hide_models": [
        "core.fotoimovel",          # Gerenciado via inline
        "core.precoporfinalidade",  # Gerenciado via inline
        "core.infracondominio",     # Modelo auxiliar
    ],
    
    # Customizar labels dos aplicativos
    "custom_links": {
        "core": [{
            "name": "📈 Dashboard Premium", 
            "url": "admin:index", 
            "icon": "fas fa-chart-line",
            "permissions": ["core.view_imovel"]
        }]
    },
    
    # Language chooser
    "language_chooser": False,
}

# =========================================
# 🎨 JAZZMIN UI TWEAKS (CORES PREMIUM)
# =========================================

JAZZMIN_UI_TWEAKS = {
    # Texto
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    
    # Cores de acento (Dourado Premium)
    "accent": "accent-warning",
    
    # Navbar (Azul Petróleo/Preto)
    "navbar": "navbar-dark bg-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    
    # Layout
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    
    # Sidebar (Premium com acento dourado)
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    
    # Tema
    "theme": "default",
    "dark_mode_theme": None,
    
    # =====================================
    # 🎨 BOTÕES PREMIUM PERSONALIZADOS
    # =====================================
    "button_classes": {
        "primary": "btn-warning",      # Dourado para ações principais
        "secondary": "btn-secondary",  # Cinza para secundárias
        "info": "btn-info",           # Azul para informações
        "warning": "btn-warning",     # Dourado para avisos
        "danger": "btn-danger",       # Vermelho para exclusões
        "success": "btn-success"      # Verde para sucessos
    },
    
    # =====================================
    # 🎨 CUSTOM CSS PREMIUM (INLINE)
    # =====================================
    "custom_css": """
        /* Paleta de cores premium */
        :root {
            --premium-gold: #C8A866;
            --premium-gold-light: #D4AF37;
            --premium-dark: #0D0D0D;
            --premium-blue: #1E3A5F;
        }
        
        /* Header premium */
        .main-header {
            background: linear-gradient(135deg, var(--premium-blue) 0%, var(--premium-dark) 100%) !important;
            border-bottom: 3px solid var(--premium-gold) !important;
        }
        
        /* Brand premium */
        .navbar-brand {
            color: var(--premium-gold-light) !important;
            font-weight: bold !important;
        }
        
        /* Sidebar premium */
        .main-sidebar {
            background: linear-gradient(180deg, var(--premium-dark) 0%, var(--premium-blue) 100%) !important;
        }
        
        /* Botões premium */
        .btn-warning {
            background: linear-gradient(135deg, var(--premium-gold) 0%, var(--premium-gold-light) 100%) !important;
            border-color: var(--premium-gold) !important;
            color: var(--premium-dark) !important;
            font-weight: 600 !important;
        }
        
        .btn-warning:hover {
            background: linear-gradient(135deg, var(--premium-gold-light) 0%, var(--premium-gold) 100%) !important;
            border-color: var(--premium-gold-light) !important;
            color: var(--premium-dark) !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 8px rgba(200, 168, 102, 0.3) !important;
        }
        
        /* Cards premium */
        .card {
            border: 1px solid rgba(200, 168, 102, 0.2) !important;
            border-radius: 8px !important;
        }
        
        .card-header {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
            border-bottom: 2px solid var(--premium-gold) !important;
            color: var(--premium-blue) !important;
            font-weight: bold !important;
        }
        
        /* Links premium */
        a {
            color: var(--premium-blue) !important;
        }
        
        a:hover {
            color: var(--premium-gold) !important;
        }
        
        /* Tabelas premium */
        .table th {
            background-color: #f8f9fa !important;
            color: var(--premium-blue) !important;
            font-weight: 600 !important;
            border-bottom: 2px solid var(--premium-gold) !important;
        }
        
        /* Badges premium */
        .badge-success {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%) !important;
        }
        
        .badge-warning {
            background: linear-gradient(135deg, var(--premium-gold) 0%, var(--premium-gold-light) 100%) !important;
            color: var(--premium-dark) !important;
        }
        
        /* Formulários premium */
        .form-control:focus {
            border-color: var(--premium-gold) !important;
            box-shadow: 0 0 0 0.2rem rgba(200, 168, 102, 0.25) !important;
        }
        
        /* Menu sidebar premium */
        .nav-sidebar .nav-link {
            color: rgba(255, 255, 255, 0.9) !important;
        }
        
        .nav-sidebar .nav-link:hover {
            background-color: rgba(200, 168, 102, 0.2) !important;
            color: var(--premium-gold-light) !important;
        }
        
        .nav-sidebar .nav-link.active {
            background: linear-gradient(135deg, var(--premium-gold) 0%, var(--premium-gold-light) 100%) !important;
            color: var(--premium-dark) !important;
            font-weight: bold !important;
        }
        
        /* Footer premium */
        .main-footer {
            background: var(--premium-dark) !important;
            color: var(--premium-gold) !important;
            border-top: 2px solid var(--premium-gold) !important;
        }
        
        /* Animations premium */
        .btn, .card, .form-control {
            transition: all 0.3s ease !important;
        }
        
        /* Dashboard cards premium */
        .info-box {
            border-radius: 8px !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
            border: 1px solid rgba(200, 168, 102, 0.2) !important;
        }
        
        .info-box-icon {
            background: linear-gradient(135deg, var(--premium-gold) 0%, var(--premium-gold-light) 100%) !important;
            color: var(--premium-dark) !important;
        }
    """,
    
    # JavaScript personalizado premium
    "custom_js": """
        // Adicionar efeitos premium
        document.addEventListener('DOMContentLoaded', function() {
            // Adicionar ícone premium no título
            const brandElement = document.querySelector('.navbar-brand');
            if (brandElement && !brandElement.querySelector('.fas')) {
                brandElement.innerHTML = '<i class="fas fa-gem me-2"></i>' + brandElement.innerHTML;
            }
            
            // Smooth animations para botões
            document.querySelectorAll('.btn').forEach(btn => {
                btn.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-1px)';
                });
                btn.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });
            
            // Console log premium
            console.log('🎨 Imobiliária Premium Admin carregado com sucesso! 💎');
        });
    """
}

# ===============================
# 🔧 CONFIGURAÇÕES ADICIONAIS
# ===============================

# Configurações de e-mail (para produção)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Para desenvolvimento

# Configurações de cache (para produção)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Configurações de logging premium
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'premium': {
            'format': '💎 [{levelname}] {asctime} - {name}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'premium',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'core': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Configurações de segurança (para produção)
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True