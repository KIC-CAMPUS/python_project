from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, update_session_auth_hash, logout
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts

from .forms import UserForm, UpdateForm, FindUsernameForm, CustomPasswordChangeForm, CustomPasswordChangeForm, \
    CheckPasswordForm
from .models import User

from coverletter_site.views import CoverLetterList, coverLetterDelete
from coverletter_site.models import CoverLetter


# 회원가입
def join(request):
    # POST
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            join_user = form.save()
            login(request, join_user)
            return render(request, "member/join_success.html")

    # GET
    else:
        form = UserForm()
    return render(request, "member/join.html", {'form': form})


# 아이디 찾기
def id_check(request):
    form = FindUsernameForm()
    username = None

    if request.method == "POST":
        form = FindUsernameForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            phone = form.cleaned_data['phone']
            birthday = form.cleaned_data['birthday']

            try:
                user = get_user_model().objects.get(first_name=first_name, phone=phone, birthday=birthday)
                print(f"Username found: {user.username}")
                username = user.username
            except ObjectDoesNotExist as e:
                print(f"ObjectDoesNotExist exception: {e}")
                username = "일치하는 사용자가 없어요."

    return render(request, "member/id_success.html", {'form': form, 'username': username})


class MypageView(CoverLetterList):
    template_name = "member/mypage.html"

    def get_queryset(self):
        return super().get_queryset().filter(bookmark=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # Calculate bookmark counts
        context['document_type_1_count'] = CoverLetter.objects.filter(document_type=1, user=user).count()
        context['document_type_2_count'] = CoverLetter.objects.filter(document_type=2, user=user).count()
        context['document_type_3_count'] = CoverLetter.objects.filter(document_type=3, user=user).count()
        context['document_type_4_count'] = CoverLetter.objects.filter(document_type=4, user=user).count()
        context['document_type_5_count'] = CoverLetter.objects.filter(document_type=5, user=user).count()

        return context


def mypage_coverLetterDelete(request):
    coverLetterDelete(request)
    return redirect(reverse_lazy('mypage'))


# 검색
class PostSearch(MypageView):
    def get_queryset(self):
        q = self.kwargs['q']
        post_list = super().get_queryset().filter(
            Q(title__contains=q)
        ).distinct()
        return post_list


# 정렬
class Mypage_CoverLetterSortList(MypageView):
    def get_queryset(self):
        q = self.kwargs['q']
        if q == "all":
            self.ordering = ['-pk']
        elif q == "latest":
            self.ordering = ['-create_at']
        elif q == "high":
            self.ordering = ['-rate']
        elif q == "low":
            self.ordering = ['rate']

        return super().get_queryset()


def findid(request):
    return render(request, "member/findid.html")


def findpw(request):
    return render(request, "member/findpassword.html")


# 비밀번호 변경
def password_edit_view(request):
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            return redirect('mypage')
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'member/editpassword.html', {'password_change_form': password_change_form})


# 회원 정보 수정

# 회원 정보 수정
def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mypage')
    else:
        form = UpdateForm(instance=request.user)
    context = {'form': form}
    return render(request, 'member/mypage_edit.html', context)


# 비밀번호 재 설정
def reset_password_go(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        birthday = request.POST.get('birthday')
        phone = request.POST.get('phone')

        try:
            user = User.objects.get(username=username, first_name=first_name, birthday=birthday, phone=phone)
            request.session['reset_user'] = user.pk
            return redirect('reset_password')
        except User.DoesNotExist:
            return render(request, 'member/findpassword.html', {
                'form_error': '회원의 정보가 일치하지 않습니다.'
            })
    return render(request, 'member/findpassword.html')


def reset_password(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user_pk = request.session.get('reset_user')
                user = User.objects.get(pk=user_pk)
                validate_password(password1)
                user.password = make_password(password1)
                user.save()
                request.session['reset_user'] = None
                return redirect('login')
            except ValidationError:
                return render(request, 'member/pw_change.html', {
                    'form_error_list': password_validators_help_texts()
                })
        else:
            return render(request, 'member/pw_change.html', {
                'form_error_list': ['비밀 번호가 서로 일치하지 않습니다.']
            })
    return render(request, 'member/pw_change.html')


def password_check(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            return redirect('/member/update')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'member/password_check.html', {'password_form': password_form})


def profile_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'member/delete.html', {'password_form': password_form})
