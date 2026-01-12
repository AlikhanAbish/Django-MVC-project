from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Authorisation'

# login method view
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы!'
    title = 'Registration'

    # def get_context_data(self, **kwargs):
    #     context = super(UserRegistrationView, self).get_context_data(**kwargs)
    #     context['title'] = 'Registration'
    #     return context

# registration view method
# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрированы!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)  #@


class UserProfileView(TitleMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    title = 'Profile'

    def get_object(self, queryset=None):
        return self.request.user  # Returns the logged-in user directly

# profile view method
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#     form = UserProfileForm(instance=request.user)
#
#     baskets = Basket.objects.filter(user=request.user)
#     # total_sum = sum(basket.sum() for basket in baskets)
#     # total_quantity = sum(basket.quantity for basket in baskets)
#
#     # total_sum = 0
#     # total_quantity = 0
#     # for basket in baskets:
#     #     total_sum += basket.sum()
#     #     total_quantity += basket.quantity
#
#     context = {
#         'title' : 'Store - Профиль',
#         'form' : form,
#         'baskets' : baskets,
#     }
#     return render(request, 'users/profile.html', context)


# class EmailVerificationView(TitleMixin, TemplateView):
#     template_name = 'users/email_verification.html'
#     title = 'Store - Email Verification'
#
#     def get(self, request, *args, **kwargs):
#         code = kwargs['code']
#         user = User.objects.get(email=kwargs['email'])
#         email_verification=EmailVerification.objects.filter(user=user, code=code)
#         if email_verification.exists() and not email_verification.first().is_expired():
#             user.is_verified_email = True
#             user.save()
#             return super(EmailVerificationView, self).get(request, *args, **kwargs)
#         else:
#             return HttpResponseRedirect(reverse('index'))

