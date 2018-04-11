from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.

#admin.site.register(Book)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)
#admin.site.register(Author)

# add inline to show info from another class within this class
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

#Currently all of our admin classes are empty (see "pass") so the admin behaviour will be unchanged!
#We can now extend these to define our model-specific admin behaviour.

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Book) #this does the same as admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline] #add inline to show info from another class within this class

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    #Below adds a separate section below for Status and Due Back.
    # Replace below code with list_display line and categories for old view
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )