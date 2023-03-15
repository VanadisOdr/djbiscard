from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request, name, age, job): #О пользователе инфа
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
            <p>Работаю в: {job}</p>
    """)

def info(request):
    host = request.META["HTTP_HOST"]  # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]  # получаем данные бразера
    user_ip = request.META["REMOTE_ADDR"] #айпи клиента
    path = request.path  # получаем запрошенный путь

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
        <p>User-ip: {user_ip}</p>
        
    """)
def user(request,  name="Undefined", age=0): #Передаю дефолтные значения
    return HttpResponse(f"""
            <h2>Страница пользователя</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
        
    """)

