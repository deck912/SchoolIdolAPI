from django.conf.urls import include, patterns, url
from django.conf import settings
from web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^cards[/]+$', views.cards, name='cards'),
    url(r'^card[s]?/(?P<card>\d+)[/]$', views.cards, name='cards'),

    url(r'^create[/]+$', views.create, name='create'),
    url(r'^edit[/]+$', views.edit, name='edit'),
    url(r'^login[/]+$', views.login_custom_view, name='login'),
    url(r'^setaccountonlogin[/]+$', views.setaccountonlogin, name='setaccountonlogin'),
    url(r'^logout[/]+$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^addaccount[/]+$', views.addaccount, name='addaccount'),
    url(r'^editaccount/(?P<account>\d+)[/]+$', views.editaccount, name='editaccount'),
    # url(r'^addteam/(?P<account>\d+)[/]+$', views.addteam, name='addteam'),
    url(r'^user[s]?/(?P<username>[\w.@+-]+)[/]+$', views.profile, name='profile'),
    url(r'^users[/]+$', views.users, name='users'),
    url(r'^events[/]+$', views.events, name='events'),
    url(r'^event[s]?/(?P<event>[^/]+)[/]+$', views.event, name='event'),
    url(r'^idols[/]+$', views.idols, name='idols'),
    url(r'^idol[s]?/(?P<idol>[^/]+)[/]+$', views.idol, name='idol'),
    url(r'^activities[/]+$', views.activities, name='activities'),
    url(r'^activities/(?P<activity>\d+)[/]+$', views.activity, name='activity'),
    url(r'^twitter[/]+$', views.twitter, name='twitter'),
    url(r'^map[/]+$', views.mapview, name='map'),
    url(r'^donate[/]+$', views.donateview, name='donate'),


    url(r'^password_reset[/]+$', 'django.contrib.auth.views.password_reset',
        {'html_email_template_name': 'registration/password_reset_email_html.html',
         'from_email': settings.AWS_SES_RETURN_PATH,
     }, name='password_reset'),
    url(r'^password_reset/done[/]+$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done[/]+$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^ajax/modal/(?P<hash>\w+)[/]+$', views.ajaxmodal, name='ajaxmodal'),
    url(r'^ajax/addcard[/]+$', views.ajaxaddcard, name='ajaxaddcard'),
    url(r'^ajax/editcard/(?P<ownedcard>\d+)[/]+$', views.ajaxeditcard, name='ajaxeditcard'),
    url(r'^ajax/deletecard/(?P<ownedcard>\d+)[/]+$', views.ajaxdeletecard, name='ajaxdeletecard'),
    url(r'^ajax/deletelink/(?P<link>\d+)[/]+$', views.ajaxdeletelink, name='ajaxdeletelink'),
    url(r'^ajax/cards[/]+$', views.ajaxcards, name='ajaxcards'),
    url(r'^ajax/users[/]+$', views.ajaxusers, name='ajaxusers'),
    url(r'^ajax/ownedcards/(?P<account>\d+)/(?P<stored>\w+)[/]+$', views.ajaxownedcards, name='ajaxownedcards'),
    url(r'^ajax/follow/(?P<username>[\w.@+-]+)[/]+$', views.ajaxfollow, name='ajaxfollow'),
    url(r'^ajax/followers/(?P<username>[\w.@+-]+)[/]+$', views.ajaxfollowers, name='ajaxfollowers'),
    url(r'^ajax/following/(?P<username>[\w.@+-]+)[/]+$', views.ajaxfollowing, name='ajaxfollowing'),
    url(r'^ajax/activities[/]+$', views.ajaxactivities, name='ajaxactivities'),
    url(r'^ajax/likeactivity/(?P<activity>\d+)[/]+$', views.ajaxlikeactivity, name='ajaxlikeactivity'),
    url(r'^ajax/feed[/]+$', views.ajaxfeed, name='ajaxfeed'),
    url(r'^ajax/eventparticipations/(?P<account>\d+)[/]+$', views.ajaxeventparticipations, name='ajaxeventparticipations'),

    url(r'^avatar/twitter/(?P<username>[\w.@+-]+)[/]+$', views.avatar_twitter, name='avatar_twitter'),
    url(r'^avatar/facebook/(?P<username>[\w.@+-]+)[/]+$', views.avatar_facebook, name='avatar_facebook'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
)
