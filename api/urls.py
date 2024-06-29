from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import ObtainAuthToken

from api import views


router=DefaultRouter()

router.register("register",views.SignUpView,basename="register")

router.register("expenses",views.ExpenseViewSet,basename="expenses")

router.register("incomes",views.IncomeViewset,basename="incomes")



urlpatterns=[

    path('token/',ObtainAuthToken.as_view()),

    path('expenses/summary/',views.ExpenseSummaryView.as_view(),name="summary"),

    path('income/summary/',views.IncomeSummaryView.as_view(),name="summary"),

]+router.urls