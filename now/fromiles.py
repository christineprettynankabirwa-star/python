#-----EvaluationCriteria------
#-----Criteria Admin------
class EvaluationCriteriaAdmin(admin.ModelAdmin):
    list_display = ("title", "max_score")
    search_fields = ("title",)


admin.site.register(EvaluationCriteria, EvaluationCriteriaAdmin)

#-----Evaluation------
#-----Evaluation Admin(FIXED)------
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("student", "placement", "criteria", "score", "date_evaluated")
    list_filter = ("placement", "criteria")
    search_fields = ("student__username",)

    autocomplete_fields = ("student", "placement", "criteria")

admin.site.register(Evaluation,EvaluationAdmin)