import os
import subprocess
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def home(request):
    return (request, 'home.html')

def convert_pdf_to_csv(pdf_file_path):
    # Вызов вашего Python-скрипта для конвертации PDF в CSV
    result = subprocess.run(['python', 'C:/Users/olegg/PycharmProjects/djbiscard/qrcode.py', pdf_file_path], capture_output=True, text=True)

    # Обработка результатов
    if result.returncode == 0:
        csv_file_path = result.stdout.strip()
        return csv_file_path
    else:
        error_message = result.stderr.strip()
        raise Exception(f'Ошибка выполнения скрипта: {error_message}')


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']

        # Сохранение загруженного файла на сервере
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Запуск вашего Python-скрипта для конвертации PDF в CSV
        try:
            csv_file_path = convert_pdf_to_csv(file_path)
        except Exception as e:
            return HttpResponse(f'Ошибка: {str(e)}')

        # Возвращение обработанного файла клиенту
        with open(csv_file_path, 'rb') as csv_file:
            response = HttpResponse(csv_file.read(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="converted.csv"'
            return response

    return render(request, 'upload.html')