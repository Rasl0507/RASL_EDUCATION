from flask import Flask, render_template, url_for
from werkzeug.utils import redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_wtf import FlaskForm


from data.users import User
from data import db_session
from forms.user import RegisterForm
from forms.login_form import LoginForm
from forms.search_form import Search


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
f = False
use_name = ''
use_email = ''
use_about = ''
href = '' # Название приложения для ссылки


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/', methods=['GET', 'POST'])
def post():  # Фунция для открытия главной страницы
    form = Search()
    if form.validate_on_submit():  # осуществление поиска
        return redirect(f'/search box/{form.text_name.data}')
    return render_template('design.html',
                           form=form)


@app.route('/windows', methods=['GET', 'POST'])
def windows():  # Функция для открытия виндовс страницы
    form = Search()
    if form.validate_on_submit():  # осуществление поиска
        return redirect(f'/search box/{form.text_name.data}')
    return render_template('windows.html',
                           form=form)


@app.route('/office', methods=['GET', 'POST'])
def office():  # Функция для открытия страницы офис
    form = Search()
    if form.validate_on_submit():  # осуществление поиска
        return redirect(f'/search box/{form.text_name.data}')
    return render_template('office.html',
                           form=form)


@app.route('/download soft', methods=['GET', 'POST'])
def download_soft():  # Функция для открытия страницы download soft
    form = Search()
    if form.validate_on_submit():  # осуществление поиска
        return redirect(f'/search box/{form.text_name.data}')
    return render_template('download_soft.html',
                           form=form)


@app.route('/communication', methods=['GET', 'POST'])
def communication(): # Функция для открытия страницы communication
    form = Search()
    if form.validate_on_submit():  # Осуществление поиска
        return redirect(f'/search box/{form.text_name.data}')
    return render_template('communication.html',
                           form=form)


@app.route('/profile')
def profile():  # Функция открытия страницы профиля
    global use_name
    global use_email
    global use_about
    if f: # определения авторизации пользователя и выбор подходящего шаблона
        with open('design/pofile_f.html', 'r', encoding='utf-8') as html_stream:
            html = html_stream.read()
            html = html.replace('{{ name }}', use_name)
            html = html.replace('{{ email }}', use_email)
            html = html.replace('{{ about }}', use_about)
            return html
    else:
        with open('design/profile.html', 'r', encoding='utf-8') as html_stream:
            html = html_stream.read()
        return html


@app.route('/sign up', methods=['GET', 'POST'])
def sign_up():  # Открытие страницы регистрации
    db_session.global_init("db/blogs.db")
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            about=form.about.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():  # Открытие страницы Авторизации
    form = LoginForm()
    global f
    global use_name
    global use_email
    global use_about
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.username.data).first()
        if user and user.check_password(form.password.data):
            f = True
            use_name = user.name
            use_email = user.email
            use_about = user.about
            return redirect("/")
        return render_template('login.html',
                                message="Неправильный логин или пароль",
                                form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/about')
def about_avtor():  # Открытие страницы об авторе
    with open('design/about.html', 'r', encoding='utf-8') as html_stream:
        html = html_stream.read()
    html = html.replace('{{ message }}', '''Во время обучения в школе, ко мне не перестают приходить вопросы, 
                 от людей разного возраста, о том “Как установить какое-либо приложение”, “Где можно найти?”, 
                 “По какой ссылке переходить, чтобы установка была безопаснее”. После этого я решился разработать собственный 
                 сайт, где кто угодно может легко и безопасно установить желаемое приложение для своего компьютера. Это 
                 приложение должно решить проблему большинства.''')
    return html


@app.route("/ptt")
def ptt():
    form = Search()
    return render_template('search_tt.html', form=form)


@app.route('/search box/<name_app>', methods=['GET', 'POST'])
def searching(name_app):  # Страница поиска
    form = Search()
    global href
    if form.validate_on_submit(): # Осуществление поиска
        return redirect(f'/search box/{form.text_name.data}')
    if name_app == 'Windows 11':  # замена информаций на каточке в шаблоне
        with open('data/Windows 11.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Windows 11'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/windows11x64.jpg")
    if name_app == 'Windows 8.1':
        with open('data/Windows 8.1.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Windows 8.1'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/windows8.jpg")
    if name_app == 'Windows 10':
        with open('data/Windows 10.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Windows 10'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/windows-10.jpg")
    if name_app == 'Windows 7':
        with open('data/Windows 7.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Windows 7'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/windows-7_64.jpg")
    if name_app == 'Office':
        with open('data/Office.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Office'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/app-office.png")
    if name_app == 'Zona':
        with open('data/Zona.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Zona'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/zona.jpg")
    if name_app == 'DriverPack':
        with open('data/DriverPack.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'DriverPack'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/driverpack.jpg")
    if name_app == 'PyCharm':
        with open('data/PyCharm.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'PyCharm'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/pycharm.jpg")
    if name_app == 'uFiler':
        with open('data/uFiler.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'uFiler'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/ufiler.jpg")
    if name_app == 'uTorrent':
        with open('data/uTorrent.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'uTorrent'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/uTorrent.jpg")
    if name_app == 'Яндекс.Диск':
        with open('data/Яндекс.Диск.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Яндекс.Диск'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/яндекс диск.jpg")
    if name_app == 'Облако Mail.Ru':
        with open('data/Облако Mail.Ru.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Облако Mail.Ru'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/облако майл.png")
    if name_app == 'Skype':
        with open('data/Skype.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Skype'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/skype.jpg")
    if name_app == 'Zoom':
        with open('data/Zoom.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Zoom'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/zoom.jpeg")
    if name_app == 'Яндекс.Телемост':
        with open('data/Яндекс.Телемост.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
            href = 'Яндекс.Телемост'
            return render_template("search_box.html", form=form,
                                   text=ttext, path="img/телемост.jpg")
    return render_template("search_box.html",
                           form=form)


@app.route("/ads", methods=['GET', 'POST'])
def ads():  # Функция перенаправления на яндекс.Диск
    global href
    if href == 'Windows 11':
        return redirect("https://disk.yandex.ru/d/1oewymwg3focug")
    if href == 'Windows 8.1':
        return redirect("https://disk.yandex.ru/d/wHhUgRzS7i7zZw")
    if href == 'Windows 10':
        return redirect("https://disk.yandex.ru/d/mcyR32eZ1upuiw")
    if href == 'Windows 7':
        return redirect("https://disk.yandex.ru/d/uqFrUph3-I0-SQ")
    if href == 'Office':
        return redirect("https://disk.yandex.ru/d/odpvLOqXQLEJzQ")
    if href == 'Zona':
        return redirect("https://disk.yandex.ru/d/_ncfDO_jBa3e9g")
    if href == 'DriverPack':
        return redirect("https://disk.yandex.ru/d/tkluR_d05MubJQ")
    if href == 'PyCharm':
        return redirect("https://disk.yandex.ru/d/axGJkhY_ORcR2Q")
    if href == 'uFiler':
        return redirect("https://disk.yandex.ru/d/rFRxhYUpVMmOVw")
    if href == 'uTorrent':
        return redirect("https://disk.yandex.ru/d/e96lnxt40bfqCA")
    if href == 'Яндекс.Диск':
        return redirect("https://disk.yandex.ru/d/YccVKsnJ7TbS_A")
    if href == 'Облако Mail.Ru':
        return redirect("https://disk.yandex.ru/d/JyHtdF9glkOBZQ")
    if href == 'Skype':
        return redirect("https://disk.yandex.ru/d/OnBGc4WU8nKMOA")
    if href == 'Zoom':
        return redirect("https://disk.yandex.ru/d/93Ix4vtcKMRRxQ")
    if href == 'Яндекс.Телемост':
        return redirect("https://disk.yandex.ru/d/-iKZfoEA56ETCw")
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)