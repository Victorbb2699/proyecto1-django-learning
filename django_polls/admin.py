# Importing the necessary modules from Django admin and the models defined in the current module.
from django.contrib import admin
from .models import Question, Choice

# Register your models here. This is a placeholder comment indicating where to register models.

# Defining an inline admin interface for the Choice model using a Tabular layout.
class ChoiceInline(admin.TabularInline):
    model = Choice  # Specifies that this inline will manage the Choice model.
    extra = 3  # Indicates that 3 extra empty Choice forms will be displayed.

# Defining the admin interface for the Question model.
class QuestionAdmin(admin.ModelAdmin):
    # Specifying the layout of the fields displayed in the admin interface.
    fieldsets = [
        (None, {"fields":["question_text"]}),  # The first fieldset contains the question_text field without a title.
        ("Date information", {"fields":["pub_date"], "classes": ["collapse"]}),  # The second fieldset contains the pub_date field and is collapsible.
    ]
    inlines = [ChoiceInline]  # Including the ChoiceInline to manage related Choice objects within the Question admin page.

    # Configuring the list display properties for the Question model in the admin interface.
    list_display = ["question_text", "pub_date", "was_published_recently"]  # Fields to display in the list view.
    list_filter = ["pub_date"]  # Adding a filter sidebar for filtering questions by publication date.
    search_fields = ["question_text"]  # Enabling a search box to search through question_text.

# Registering the Question model with the custom QuestionAdmin interface to make it accessible in the admin panel.
admin.site.register(Question, QuestionAdmin)