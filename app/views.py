from django.shortcuts import render, redirect
from .models import agent, airport


def index(request):
    agents = agent.objects.all()
    airports = airport.objects.all()

    context = ({
        'agents': agents,
        'airports': airports,
    })

    if request.method == 'POST':
        airport_id = request.POST['airport']
        foiz = request.POST['foiz']
        agent_id = request.POST['agent']
        agent1 = agent.objects.get(id=agent_id)
        airport1 = airport.objects.get(id=airport_id)

        if agent1.airport == airport1:
            agent1.foiz = foiz
            agent1.save()

    return render(request, 'index.html', context)
