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
        ifcode = request.POST.get('ifcode', 'if')
        andcode = request.POST.get('andcode', 'and')
        airport_id = request.POST['airport']
        foiz = request.POST['foiz']
        agent_id = request.POST['agent']
        
        eval(f'{ifcode}:{agent_id}.airport == {airport_id} \n print("salom")')

    

    return render(request, 'index.html', context)
    
    
    
