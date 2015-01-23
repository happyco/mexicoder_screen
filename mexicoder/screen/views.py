from django.views.generic import ListView
from models import League, Team, Person
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView


class ListMenu(ListView):
    model = League
    template_name = 'menu_list.html'


class ListLeagueView(ListView):
    model = League
    template_name = 'league_list.html'


class CreateLeagueView(CreateView):

    model = League
    template_name = 'new_league.html'

    def get_success_url(self):
        return reverse('league-list')

    def get_context_data(self, **kwargs):

        context = super(CreateLeagueView, self).get_context_data(**kwargs)
        context['action'] = reverse('league-new')

        return context


class UpdateLeagueView(UpdateView):

    model = League
    template_name = 'edit_league.html'

    def get_success_url(self):
        return reverse('league-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateLeagueView, self).get_context_data(**kwargs)
        context['action'] = reverse('league-edit',
                                    kwargs={'pk': self.get_object().id})

        return context


class DeleteLeagueView(DeleteView):
    model = League
    template_name = 'delete_league.html'

    def get_success_url(self):
        return reverse('league-list')

    def get_context_data(self, **kwargs):
        context = super(DeleteLeagueView, self).get_context_data(**kwargs)
        context['action'] = reverse('league-delete',
                                    kwargs={'pk': self.get_object().id})

        return context

class ListTeamView(ListView):
    model = Team
    template_name = 'team_list.html'


class CreateTeamView(CreateView):

    model = Team
    template_name = 'new_team.html'

    def get_success_url(self):
        return reverse('team-list')

    def get_context_data(self, **kwargs):

        context = super(CreateTeamView, self).get_context_data(**kwargs)
        context['action'] = reverse('team-new')

        return context


class UpdateTeamView(UpdateView):

    model = Team
    template_name = 'edit_team.html'

    def get_success_url(self):
        return reverse('team-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateTeamView, self).get_context_data(**kwargs)
        context['action'] = reverse('team-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeleteTeamView(DeleteView):
    model = Team
    template_name = 'delete_team.html'

    def get_success_url(self):
        return reverse('team-list')

    def get_context_data(self, **kwargs):
        context = super(DeleteTeamView, self).get_context_data(**kwargs)
        context['action'] = reverse('team-delete',
                                    kwargs={'pk': self.get_object().id})
									
class ListPersonView(ListView):
    model = Person
    template_name = 'person_list.html'


class CreatePersonView(CreateView):

    model = Person
    template_name = 'new_person.html'

    def get_success_url(self):
        return reverse('person-list')

    def get_context_data(self, **kwargs):

        context = super(CreatePersonView, self).get_context_data(**kwargs)
        context['action'] = reverse('person-new')

        return context


class UpdatePersonView(UpdateView):

    model = Person
    template_name = 'edit_person.html'

    def get_success_url(self):
        return reverse('person-list')

    def get_context_data(self, **kwargs):

        context = super(UpdatePersonView, self).get_context_data(**kwargs)
        context['action'] = reverse('team-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeletePersonView(DeleteView):
    model = Person
    template_name = 'delete_person.html'

    def get_success_url(self):
        return reverse('person-list')

    def get_context_data(self, **kwargs):
        context = super(DeletePersonView, self).get_context_data(**kwargs)
        context['action'] = reverse('person-delete',
                                    kwargs={'pk': self.get_object().id})
