from django.conf.urls import patterns, include, url
from django.contrib import admin
from screen import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^Llist$', views.ListLeagueView.as_view(), name='league-list',),
                       url(r'^Lnew$', views.CreateLeagueView.as_view(), name='league-new',),
                       url(r'^Ledit/(?P<pk>\d+)/$', views.UpdateLeagueView.as_view(), name='league-edit',),
                       url(r'^Ldelete/(?P<pk>\d+)/$', views.DeleteLeagueView.as_view(), name='league-delete',),
                       url(r'^Tlist$', views.ListTeamView.as_view(), name='team-list',),
                       url(r'^Tnew$', views.CreateTeamView.as_view(), name='team-new',),
                       url(r'^Tedit/(?P<pk>\d+)/$', views.UpdateTeamView.as_view(), name='team-edit',),
					   url(r'^Tdelete/(?P<pk>\d+)/$', views.DeleteTeamView.as_view(), name='team-delete',),
					   url(r'^Plist$', views.ListPersonView.as_view(), name='person-list',),
                       url(r'^Pnew$', views.CreatePersonView.as_view(), name='person-new',),
                       url(r'^Pedit/(?P<pk>\d+)/$', views.UpdatePersonView.as_view(), name='person-edit',),
					   url(r'^Pdelete/(?P<pk>\d+)/$', views.DeletePersonView.as_view(), name='person-delete',),
                       url(r'^', views.ListMenu.as_view(), name='menu-list',),
                       # Examples:
                       # url(r'^$', 'mexicoder.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
