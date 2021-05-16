# RCSF-Django
![RCSF](https://user-images.githubusercontent.com/56162588/118394801-c2f51000-b63e-11eb-9c74-e46b3404429f.jpg)

### Passos para lançar e editar a aplicação
1. Abra a linha de comandos (PowerShell ou cmd)
1. Descarregue uma cópia (clone) do repositório com o comando `git clone https://github.com/RCSF-ULHT/rcsf-django` 
1. Entre na pasta  `cd rcsf-django`
1. Crie um ambiente virtual com o django instalado `python -m venv virtual`
1. Active o ambiente virtual `virtual\Scripts\activate`
1. Lance a aplicação no browser com o comando `python manage.py runserver`
1. abra a aplicação no Pycharm com o comando `pycharm .` ou no VS Code com o comando `code .`

### Passos para criar uma nóva página na aplicação
1. no ficheiro `views.py` crie uma nova função que renderize a nova página
2. na pasta `website\templates\website` crie uma página HTML correspondente para ser renderizada, extendendo o layout base (veja como é feito nas outras páginas)
3. no ficheiro `website\urls.py` crie um novo `path` para o novo URL
4. no ficheiro `layout.html` (que está na pasta `website\templates\website`) atualize o menu de navegação, inlcuindo um link para a nova página
