from django.contrib import admin
from django.urls import path

from blog.admin import blog_site
from bookstore.admin import bookstore_site_area

urlpatterns = [
    path('blog_admin/', blog_site.urls),
    path("admin/", admin.site.urls),
    path("bookstore_admin/", bookstore_site_area.urls),
]

# admin.site.index_title = "The Bookstore"
# admin.site.site_header = "Bookstore | Admin Area"
# admin.site.site_title = "Admin Area"
