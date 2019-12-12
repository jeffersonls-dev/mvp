from django.urls import path
from . import views
from bibliotecapp.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

app_name = 'livro'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-livro'),
    path('update/<int:livro_id>', views.update_livro,name='update-livro'),
    path('delete/<int:livro_id>', views.delete_livro,name='delete-livro'),
    path('download/<int:livro_id>', views.download, name='download-livro'),

    
]
#DataFlair
# if DEBUG:
urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    
