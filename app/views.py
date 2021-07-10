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
        
        code = f'{ifcode}:{agent_id} \n{andcode}:{airport_id}, {foiz}'
        print(code)
        
        
        if agent_id.eval().airport == airport_id:
            print('salom')
        
    

    return render(request, 'index.html', context)
    
    
    
