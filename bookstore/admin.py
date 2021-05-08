from django.contrib import admin


class BookstoreAdminArea(admin.AdminSite):
    site_header = "Bookstore Admin Area"


bookstore_site_area = BookstoreAdminArea(name="BookstoreAdmin")

# bookstore_site_area.register()
