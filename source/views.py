from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import requests

from .forms import  CompanyForm
from .models import  Company


def index(request):
    return render(request, "company/index.html")

def login_view(request):
    error_message = None  # Başlangıçta hata mesajı boş

    # if request.method == 'POST':
    #     print(request.POST["email"])
    #     print(request.POST["password"])
    #
    #
    #     email = request.POST["email"]
    #     password = request.POST["password"]
    #     user = authenticate(username=email, password=password)
    #     print(user)
    #     if user is not None:
    #         print("giriş yapıldı")
    #         login(request, user)
    #         return redirect('/')
    #
    # return render(request, 'company/login.html')
    if request.method == 'POST':

        # Email ve şifreyi POST verilerinden al
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Kullanıcıyı email ile doğrula
        try:
            user = User.objects.get(email=email)  # Email ile kullanıcıyı bul
            user = authenticate(request, username=user.username, password=password)  # Şifreyi kontrol et
        except User.DoesNotExist:
            user = None

        if user is not None:
            print("Giriş yapıldı")
            login(request, user)
            return redirect('/')  # Başarılı giriş sonrası yönlendir
        else:
            error_message = "Geçersiz email veya şifre."  # Hata mesajı

    return render(request, 'company/login.html', {'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('home')

def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    company.delete()
    return redirect('/company/list')  # Silme sonrası liste sayfasına yönlendir

@login_required
def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        print("HELLOOO")
        form = CompanyForm(request.POST, instance=company)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/company/list')  # Düzenleme sonrası liste sayfasına yönlendir
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company/company_edit.html', {'form': form, 'company': company})



def company_list(request):
    companies = Company.objects.all()
    for c in companies:
        print(c.siem_username)
    context = {
        'companies': companies,
        'siem_product_choices': Company.SIEM_PRODUCT_CHOICES,
        'status_choices': Company.STATUS_CHOICES,
        'sales_manager_choices': Company.SALES_MANAGER_CHOICES,
        'type_choices': Company.TYPE_CHOICES,
        'industry_choices': Company.INDUSTRY_CHOICES,
    }
    return render(request, 'company/company_list.html', context)



@login_required  # Kullanıcının giriş yapmasını zorunlu kılar
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)  # Formu henüz kaydetme
            company.created_by = request.user.username  # Oturum açmış kullanıcının adını ekle
            company.save()  # Şirketi kaydet
            return redirect('company_list')  # Şirket ekledikten sonra şirketler listesine yönlendir
    else:
        form = CompanyForm()
    return render(request, 'company/company_create.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hesap başarıyla oluşturuldu! Giriş yapabilirsiniz.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'company/register.html', {'form': form})



def get_data_source(request):
    # API'ye yapılacak istek için URL'yi belirleyin
    login_url = "https://10.0.3.81/rs/esm/login"  # Buraya dış API'nizin URL'sini yazın

    try:
        # API'ye GET isteği gönder
        login_payload = {
            "username": "emre.seyhan",
            "password": "Emre123*",
            "locale": "en_US"
        }

        # Disable SSL verification for the login request
        response = requests.post(login_url, json=login_payload, verify=False)
        print(response)
        # Eğer istek başarılıysa (200 OK), veriyi JSON formatında al
        if response.status_code == 200:
            data = response.json()

            # Veriyi bir .txt dosyasına kaydedelim
            with open('data.txt', 'w') as f:
                f.write(str(data))  # Veriyi string olarak kaydediyoruz

            return JsonResponse({"message": "Data fetched and saved to file successfully."})

        else:
            return JsonResponse({"error": "Failed to fetch data from the API."}, status=400)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

