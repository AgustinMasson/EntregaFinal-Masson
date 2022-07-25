from django.urls import path
from Blog import views
from Blog.views import page, pagedetail, updatepage, deletepage

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("Home", views.home, name="Home"),
    path("NotPages", views.pageserror, name="PagesError"),
    path("Pages", page.as_view(template_name = "Blog/pages.html"), name="Pages"),
    path(r'^(?P<pk>\d+)$', pagedetail.as_view(template_name = "Blog/pagedetail.html"), name="PageDetail"),
    path("NewPage", views.PostBlogs, name="NewPage"),
    path(r'^Update/(?P<pk>\d+)$', views.updatepage.as_view(), name="UpdatePage"),
    path(r'^Delete/(?P<pk>\d+)$', deletepage.as_view(template_name = "Blog/deletepage.html"), name="DeletePage"),
    path("About", views.about, name="About"),
    path("About2", views.about2, name="About2")
]