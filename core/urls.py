from django.conf.urls import url, include
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativo,
    lista_mensalistas,
    lista_movmensalistas,
    pessoas_novas,
    novo_veiculo,
    novo_rotativo,
    novo_mensalista,
    novo_movmensalista,
    pessoa_update,
    veiculo_update,
    movrotativo_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativo_delete,
    mensalista_delete,
    movmensalista_delete
)

urlpatterns = [
    url(r'^$', home, name='core_home'),

    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^cadpessoas/$', pessoas_novas, name='core_pessoas_novas'),
    url(r'^pessoaupdate/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    url(r'^pessoadelete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),
    

    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^cadveiculos/$', novo_veiculo, name='core_novo_veiculo'),
    url(r'^veiculoupdate/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    url(r'^veiculodelete/(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),



    url(r'^movrotativos/$', lista_movrotativo, name='core_lista_movrotativos'),
    url(r'^nvrotativos/$', novo_rotativo, name='core_novo_rotativo'),
    url(r'^movrotativoupdate/(?P<id>\d+)/$', movrotativo_update, 
            name='core_movrotativo_update'),
    url(r'^movrotativodelete/(?P<id>\d+)/$', movrotativo_delete, 
            name='core_movrotativo_delete'),


    url(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    url(r'^nvmensalistas/$', novo_mensalista, name='core_novo_mensalista'),
    url(r'^mensalistaupdate/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    url(r'^mensalistadelete/(?P<id>\d+)/$', mensalista_delete, name='core_mensalista_delete'),


    url(r'^movmensalistas/$', lista_movmensalistas, name='core_lista_movmensalistas'),
    url(r'^nvmensalistas/$', novo_movmensalista, name='core_novo_movmensalista'),
    url(r'^movmensalistaupdate/(?P<id>\d+)/$', movmensalista_update, 
            name='core_movmensalista_update'),
    url(r'^movmensalistadelete/(?P<id>\d+)/$', movmensalista_delete, 
            name='core_movmensalista_delete')
        

]
