from django.contrib import admin


class AbstractGristModelAdmin(admin.ModelAdmin):
    list_display = ("external_id",)
    ordering = ("external_id",)
    list_display_links = ("external_id",)

    def get_readonly_fields(self, request, obj=None):
        """ Force all fields to read-only """
        if self.fields:
            return self.fields
        else:
            fields = []
            for _, fieldset in self.fieldsets:
                fields.extend(fieldset["fields"])
            return fields
