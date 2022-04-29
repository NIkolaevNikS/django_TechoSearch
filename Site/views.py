from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.http import *
from django.shortcuts import render, HttpResponsePermanentRedirect
from django.views import generic
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator

from .models import H_HeadSet_Hz, H_HeadSet_Set, H_HeadSet, H_HeadSet_Sens, H_HeadSet_Scheme, K_Keyboard, \
    K_Keyboard_Type, K_Keyboard_Format, K_Keyboard_SwitchModel, M_Mouse_SenserModel, M_Mouse, M_Mouse_DPI, \
    M_Mouse_Frequency, Manufacturer, ConnectType, ConnectionInt
from .forms import ManufacturerForm, MouseForm, LoginForm, UserRegistrationForm, KeyboardForm, HeadsetForm
from .serializers import MouseSerializer

from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    num_H_HeadSet_Hz = H_HeadSet_Hz.objects.all().count()
    num_H_HeadSet_Set = H_HeadSet_Set.objects.all().count()
    num_H_HeadSet = H_HeadSet.objects.all().count()
    num_H_HeadSet_Sens = H_HeadSet_Sens.objects.all().count()
    num_H_HeadSet_Scheme = H_HeadSet_Scheme.objects.all().count()
    num_K_Keyboard = K_Keyboard.objects.all().count()
    num_K_Keyboard_Type = K_Keyboard_Type.objects.all().count()
    num_K_Keyboard_Format = K_Keyboard_Format.objects.all().count()
    num_K_Keyboard_SwitchModel = K_Keyboard_SwitchModel.objects.all().count()
    num_M_Mouse_SenserModel = M_Mouse_SenserModel.objects.all().count()
    num_M_Mouse = M_Mouse.objects.all().count()
    num_M_Mouse_DPI = M_Mouse_DPI.objects.all().count()
    num_Manufacturer = Manufacturer.objects.all().count()
    num_ConnectType = ConnectType.objects.all().count()
    num_ConnectionInt = ConnectionInt.objects.all().count()
    num_M_Mouse_Frequency = M_Mouse_Frequency.objects.all().count()

    return render(request, 'Site/Slider.html',
                  context={'num_H_HeadSet_Hz': num_H_HeadSet_Hz,
                           'num_H_HeadSet_Set': num_H_HeadSet_Set,
                           'num_H_HeadSet': num_H_HeadSet,
                           'num_H_HeadSet_Sens': num_H_HeadSet_Sens,
                           'num_H_HeadSet_Scheme': num_H_HeadSet_Scheme,
                           'num_K_Keyboard': num_K_Keyboard,
                           'num_K_Keyboard_Type': num_K_Keyboard_Type,
                           'num_K_Keyboard_Format': num_K_Keyboard_Format,
                           'num_K_Keyboard_SwitchModel': num_K_Keyboard_SwitchModel,
                           'num_M_Mouse_SenserModel': num_M_Mouse_SenserModel,
                           'num_M_Mouse': num_M_Mouse,
                           'num_M_Mouse_DPI': num_M_Mouse_DPI,
                           'num_Manufacturer': num_Manufacturer,
                           'num_ConnectType': num_ConnectType,
                           'num_ConnectionInt': num_ConnectionInt,
                           'num_M_Mouse_Frequency': num_M_Mouse_Frequency})


def index1(request):
    num_H_HeadSet_Hz = H_HeadSet_Hz.objects.all().count()
    num_H_HeadSet_Set = H_HeadSet_Set.objects.all().count()
    num_H_HeadSet = H_HeadSet.objects.all().count()
    num_H_HeadSet_Sens = H_HeadSet_Sens.objects.all().count()
    num_H_HeadSet_Scheme = H_HeadSet_Scheme.objects.all().count()
    num_K_Keyboard = K_Keyboard.objects.all().count()
    num_K_Keyboard_Type = K_Keyboard_Type.objects.all().count()
    num_K_Keyboard_Format = K_Keyboard_Format.objects.all().count()
    num_K_Keyboard_SwitchModel = K_Keyboard_SwitchModel.objects.all().count()
    num_M_Mouse_SenserModel = M_Mouse_SenserModel.objects.all().count()
    num_M_Mouse = M_Mouse.objects.all().count()
    num_Manufacturer = Manufacturer.objects.all().count()
    num_ConnectType = ConnectType.objects.all().count()
    num_ConnectionInt = ConnectionInt.objects.all().count()
    num_M_Mouse_Frequency = M_Mouse_Frequency.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'Site/index1.html',
                  context={'num_H_HeadSet_Hz': num_H_HeadSet_Hz,
                           'num_H_HeadSet_Set': num_H_HeadSet_Set,
                           'num_H_HeadSet': num_H_HeadSet,
                           'num_H_HeadSet_Sens': num_H_HeadSet_Sens,
                           'num_H_HeadSet_Scheme': num_H_HeadSet_Scheme,
                           'num_K_Keyboard': num_K_Keyboard,
                           'num_K_Keyboard_Type': num_K_Keyboard_Type,
                           'num_K_Keyboard_Format': num_K_Keyboard_Format,
                           'num_K_Keyboard_SwitchModel': num_K_Keyboard_SwitchModel,
                           'num_M_Mouse_SenserModel': num_M_Mouse_SenserModel,
                           'num_M_Mouse': num_M_Mouse,
                           'num_Manufacturer': num_Manufacturer,
                           'num_ConnectType': num_ConnectType,
                           'num_ConnectionInt': num_ConnectionInt,
                           'num_M_Mouse_Frequency': num_M_Mouse_Frequency,
                           'num_visits': num_visits})


class M_MouseViewSet(ModelViewSet):
    queryset = M_Mouse.objects.all()
    serializer_class = MouseSerializer


class AllfilterMouse:

    def get_manufact(self):
        return Manufacturer.objects.all()

    def get_Connectionint(self):
        return ConnectionInt.objects.all()

    def get_Price(self):
        return M_Mouse.objects.filter().values("M_Mouse_Price")


class M_MouseListView(AllfilterMouse, generic.ListView):
    model = M_Mouse


class FilterMouse(AllfilterMouse, generic.ListView):
    def get_queryset(self):
        queryset = M_Mouse.objects.filter(
            Q(M_Mouse_ConnectionInt__in=self.request.GET.getlist("connectionint")) |
            Q(M_Mouse_Manufacturer__in=self.request.GET.getlist("manufacturer"))
        )
        return queryset


class M_MouseDetailView(generic.DetailView):
    model = M_Mouse


class K_KeyboardDetailView(generic.DetailView):
    model = K_Keyboard


class H_HeadSetDetailView(generic.DetailView):
    model = H_HeadSet


def add_mouse(request):
    if request.method == 'POST':
        fm = MouseForm(request.POST, request.FILES)
        if fm.is_valid():
            f1 = fm.cleaned_data['M_Mouse_name']
            f2 = fm.cleaned_data['M_Mouse_Manufacturer']
            f3 = fm.cleaned_data['M_Mouse_ConnectType']
            f4 = fm.cleaned_data['M_Mouse_Frequency']
            f5 = fm.cleaned_data['M_Mouse_DPI']
            f6 = fm.cleaned_data['M_Mouse_ConnectionInt']
            f7 = fm.cleaned_data['M_Mouse_Price']
            f8 = fm.cleaned_data['M_Mouse_SenserModel']
            f9 = fm.cleaned_data['M_Mouse_Image']
            ms = M_Mouse(M_Mouse_name=f1, M_Mouse_Manufacturer=f2, M_Mouse_ConnectType=f3,
                         M_Mouse_Frequency=f4, M_Mouse_DPI=f5, M_Mouse_ConnectionInt=f6,
                         M_Mouse_Price=f7, M_Mouse_SenserModel=f8, M_Mouse_Image=f9)
            ms.save()
            fm = MouseForm()
    else:
        fm = MouseForm()
    mouse = M_Mouse.objects.all()
    paginator = Paginator(mouse, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Site/m_mouse_form.html', {'form': fm, 'mouse': mouse, 'page_obj': page_obj})


def delete_mouse(request, id):
    mouse = M_Mouse.objects.get(M_Mouse_id=id)
    mouse.delete()
    return HttpResponseRedirect("/mouse/create/")


def update_mouse(request, id):
    if request.method == 'POST':
        pi = M_Mouse.objects.get(M_Mouse_id=id)
        fm = MouseForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = M_Mouse.objects.get(M_Mouse_id=id)
        fm = MouseForm(instance=pi)
    return render(request, 'Site/m_mouse_update.html', {'form': fm})


def add_keyboard(request):
    if request.method == 'POST':
        fm = KeyboardForm(request.POST, request.FILES)
        if fm.is_valid():
            f1 = fm.cleaned_data['K_Keyboard_name']
            f2 = fm.cleaned_data['K_Keyboard_Manufacturer']
            f3 = fm.cleaned_data['K_Keyboard_Type']
            f4 = fm.cleaned_data['K_Keyboard_SwitchModel']
            f5 = fm.cleaned_data['K_Keyboard_Format']
            f6 = fm.cleaned_data['K_Keyboard_ConnectType']
            f7 = fm.cleaned_data['K_Keyboard_Price']
            f8 = fm.cleaned_data['K_Keyboard_ConnectionInt']
            f9 = fm.cleaned_data['K_Keyboard_Image']
            kb = K_Keyboard(K_Keyboard_name=f1, K_Keyboard_Manufacturer=f2, K_Keyboard_Type=f3,
                            K_Keyboard_SwitchModel=f4, K_Keyboard_Format=f5, K_Keyboard_ConnectType=f6,
                            K_Keyboard_Price=f7, K_Keyboard_ConnectionInt=f8, K_Keyboard_Image=f9)
            kb.save()
            fm = KeyboardForm()
    else:
        fm = KeyboardForm()
    keyboard = K_Keyboard.objects.all()
    paginator = Paginator(keyboard, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Site/k_keyboard_form.html', {'form': fm, 'keyboard': keyboard, 'page_obj': page_obj})


def delete_keyboard(request, id):
    keyboard = K_Keyboard.objects.get(K_Keyboard_id=id)
    keyboard.delete()
    return HttpResponseRedirect("/keyboard/create/")


def update_keyboard(request, id):
    if request.method == 'POST':
        pi = K_Keyboard.objects.get(K_Keyboard_id=id)
        fm = KeyboardForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = K_Keyboard.objects.get(K_Keyboard_id=id)
        fm = KeyboardForm(instance=pi)
    return render(request, 'Site/k_keyboard_update.html', {'form': fm})


def add_headset(request):
    if request.method == 'POST':
        fm = HeadsetForm(request.POST, request.FILES)
        if fm.is_valid():
            f1 = fm.cleaned_data['H_HeadSet_name']
            f2 = fm.cleaned_data['H_HeadSet_Manufacturer']
            f3 = fm.cleaned_data['H_HeadSet_Scheme']
            f4 = fm.cleaned_data['H_HeadSet_Hz']
            f5 = fm.cleaned_data['H_HeadSet_Sens']
            f6 = fm.cleaned_data['H_HeadSet_ConnectType']
            f7 = fm.cleaned_data['H_HeadSet_Price']
            f8 = fm.cleaned_data['H_HeadSet_ConnectionInt']
            f9 = fm.cleaned_data['H_HeadSet_Image']
            f10 = fm.cleaned_data['H_HeadSet_Set']
            hs = H_HeadSet(H_HeadSet_name=f1, H_HeadSet_Manufacturer=f2, H_HeadSet_Scheme=f3,
                           H_HeadSet_Hz=f4, H_HeadSet_Sens=f5, H_HeadSet_ConnectType=f6,
                           H_HeadSet_Price=f7, H_HeadSet_ConnectionInt=f8, H_HeadSet_Image=f9,
                           H_HeadSet_Set=f10)
            hs.save()
            fm = HeadsetForm()
    else:
        fm = HeadsetForm()
    headset = H_HeadSet.objects.all()
    paginator = Paginator(headset, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Site/h_headset_form.html', {'form': fm, 'headset': headset, 'page_obj': page_obj})


def delete_headset(request, id):
    headset = H_HeadSet.objects.get(H_HeadSet_id=id)
    headset.delete()
    return HttpResponseRedirect("/headset/create/")


def update_headset(request, id):
    if request.method == 'POST':
        pi = H_HeadSet.objects.get(H_HeadSet_id=id)
        fm = HeadsetForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = H_HeadSet.objects.get(H_HeadSet_id=id)
        fm = HeadsetForm(instance=pi)
    return render(request, 'Site/h_headset_update.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
            else:
                return render(request, 'registration/login1.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def is_valid(pr):
    return pr != '' and pr is not None


def FilterSearchMouse(request):
    qs = M_Mouse.objects.all()
    Manufacturers = Manufacturer.objects.all()
    ConnectionInts = ConnectionInt.objects.all()
    Sensers = M_Mouse_SenserModel.objects.all()
    ConnectTypes = ConnectType.objects.all()
    Frequency = M_Mouse_Frequency.objects.all()
    DPI = M_Mouse_DPI.objects.all()
    M_Mouse_name_contains = request.GET.get('M_Mouse_name_contains')
    price_min = request.GET.get('min_price')
    price_max = request.GET.get('max_price')
    manufact = request.GET.getlist('manufactur')
    connectint = request.GET.get('connectint')
    sens = request.GET.get('senser')
    connecttype = request.GET.get('connecttype')
    freq = request.GET.get('frequency')
    dpi = request.GET.get('dpi')

    if is_valid(M_Mouse_name_contains) and M_Mouse_name_contains != ' ':
        qs = qs.filter(M_Mouse_name__icontains=M_Mouse_name_contains)

    if is_valid(price_min):
        qs = qs.filter(M_Mouse_Price__gte=price_min)

    if is_valid(price_max):
        qs = qs.filter(M_Mouse_Price__lte=price_max)

    if is_valid(manufact) and len(manufact) > 0:
        qs = qs.filter(Q(M_Mouse_Manufacturer__in=manufact))

    if is_valid(connectint) and connectint != '----':
        qs = qs.filter(M_Mouse_ConnectionInt__ConnectionInt_name=connectint)

    if is_valid(sens) and sens != '----':
        qs = qs.filter(M_Mouse_SenserModel__M_Mouse_SenserModel_name=sens)

    if is_valid(connecttype) and connecttype != '----':
        qs = qs.filter(M_Mouse_ConnectType__ConnectType_name=connecttype)

    if is_valid(freq) and freq != '----':
        qs = qs.filter(M_Mouse_Frequency__M_Mouse_Frequency_name=freq)

    if is_valid(dpi) and dpi != '----':
        qs = qs.filter(M_Mouse_DPI__M_Mouse_DPI_name=dpi)

    context = {
        'queryset': qs,
        'manufacturer': Manufacturers,
        'connectint': ConnectionInts,
        'senser': Sensers,
        'connecttype': ConnectTypes,
        'frequency': Frequency,
        'dpi': DPI,
    }
    return render(request, "Site/m_mouse_list.html", context)


def FilterSearchKeyboard(request):
    qs = K_Keyboard.objects.all()
    Manufacturers = Manufacturer.objects.all()
    ConnectionInts = ConnectionInt.objects.all()
    Types = K_Keyboard_Type.objects.all()
    ConnectTypes = ConnectType.objects.all()
    Formats = K_Keyboard_Format.objects.all()
    Switchs = K_Keyboard_SwitchModel.objects.all()
    K_Keyboard_name_contains = request.GET.get('K_Keyboard_name_contains')
    price_min = request.GET.get('min_price')
    price_max = request.GET.get('max_price')
    manufact = request.GET.getlist('manufactur')
    connectint = request.GET.get('connectint')
    typekb = request.GET.get('type')
    connecttype = request.GET.get('connecttype')
    formatkb = request.GET.get('format')
    switch = request.GET.get('switch')

    if is_valid(K_Keyboard_name_contains) and K_Keyboard_name_contains != ' ':
        qs = qs.filter(K_Keyboard_name__icontains=K_Keyboard_name_contains)

    if is_valid(price_min):
        qs = qs.filter(K_Keyboard_Price__gte=price_min)

    if is_valid(price_max):
        qs = qs.filter(K_Keyboard_Price__lte=price_max)

    if is_valid(manufact) and len(manufact) > 0:
        qs = qs.filter(Q(K_Keyboard_Manufacturer__in=manufact))

    if is_valid(connectint) and connectint != '----':
        qs = qs.filter(K_Keyboard_ConnectionInt__ConnectionInt_name=connectint)

    if is_valid(typekb) and typekb != '----':
        qs = qs.filter(K_Keyboard_Type__K_Keyboard_Type_name=typekb)

    if is_valid(connecttype) and connecttype != '----':
        qs = qs.filter(K_Keyboard_ConnectType__ConnectType_name=connecttype)

    if is_valid(formatkb) and formatkb != '----':
        qs = qs.filter(K_Keyboard_Format__K_Keyboard_Format_name=formatkb)

    if is_valid(switch) and switch != '----':
        qs = qs.filter(K_Keyboard_SwitchModel__K_Keyboard_SwitchModel_name=switch)

    context = {
        'queryset': qs,
        'manufacturer': Manufacturers,
        'connectint': ConnectionInts,
        'type': Types,
        'connecttype': ConnectTypes,
        'format': Formats,
        'switch': Switchs,
    }
    return render(request, "Site/k_keyboard_list.html", context)


def FilterSearchHeadset(request):
    qs = H_HeadSet.objects.all()
    Manufacturers = Manufacturer.objects.all()
    ConnectionInts = ConnectionInt.objects.all()
    Schemes = H_HeadSet_Scheme.objects.all()
    ConnectTypes = ConnectType.objects.all()
    Hzs = H_HeadSet_Hz.objects.all()
    Senses = H_HeadSet_Sens.objects.all()
    Sets = H_HeadSet_Set.objects.all()
    H_HeadSet_name_contains = request.GET.get('H_HeadSet_name_contains')
    price_min = request.GET.get('min_price')
    price_max = request.GET.get('max_price')
    manufact = request.GET.getlist('manufactur')
    connectint = request.GET.get('connectint')
    schemehs = request.GET.get('scheme')
    connecttype = request.GET.get('connecttype')
    hertz = request.GET.get('hz')
    sens = request.GET.get('sens')
    seths = request.GET.get('set')

    if is_valid(H_HeadSet_name_contains) and H_HeadSet_name_contains != ' ':
        qs = qs.filter(H_HeadSet_name__icontains=H_HeadSet_name_contains)

    if is_valid(price_min):
        qs = qs.filter(H_HeadSet_Price__gte=price_min)

    if is_valid(price_max):
        qs = qs.filter(H_HeadSet_Price__lte=price_max)

    if is_valid(manufact) and len(manufact) > 0:
        qs = qs.filter(Q(H_HeadSet_Manufacturer__in=manufact))

    if is_valid(connectint) and connectint != '----':
        qs = qs.filter(H_HeadSet_ConnectionInt__ConnectionInt_name=connectint)

    if is_valid(schemehs) and schemehs != '----':
        qs = qs.filter(H_HeadSet_Scheme__H_HeadSet_Scheme_name=schemehs)

    if is_valid(connecttype) and connecttype != '----':
        qs = qs.filter(H_HeadSet_ConnectType__ConnectType_name=connecttype)

    if is_valid(hertz) and hertz != '----':
        qs = qs.filter(H_HeadSet_Hz__H_HeadSet_Hz_id=hertz)

    if is_valid(sens) and sens != '----':
        qs = qs.filter(H_HeadSet_Sens__H_HeadSet_Sens_name=sens)

    if is_valid(seths) and seths != '----':
        qs = qs.filter(H_HeadSet_Set__H_HeadSet_Set_name=seths)

    context = {
        'queryset': qs,
        'manufacturer': Manufacturers,
        'connectint': ConnectionInts,
        'sens': Senses,
        'connecttype': ConnectTypes,
        'hz': Hzs,
        'set': Sets,
        'scheme': Schemes,
    }
    return render(request, "Site/h_headset_list.html", context)
