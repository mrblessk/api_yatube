
# Sprint №8 Practicum.Yandex: "CRUD for Yatube"

- [Description](#description)
- [Objectives](#objectives)
- [Installation](#installation)
- [Usage](#usage)




## Description:
CRUD (abbr. create, read, update, delete) is an acronym for four basic functions used when working with persistent data stores:

- creation
- reading
- editing
- deletion

In this project, I had to implement these functions for "Yatube" following the instructions below.

## Objectives:
1. Create in the "api-application" the logic of interaction with the API.
2. The API should only be available to authenticated users.
3. Use in project "TokenAuthentication" as token authentication.
4. An authenticated user is authorized to modify and remove their content; otherwise, access is read-only. 
5. Attempting to modify someone else's data should return a 403 Forbidden response code.
6. To interact with resources, the following endpoints must be described and configured:
- `api/v1/api-token-auth/ (POST)`
- `api/v1/posts/ (GET, POST)`
- `api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE):`
- `api/v1/groups/ (GET)`
- `api/v1/groups/ (GET)`
- `api/v1/posts/{post_id}/comments/ (GET, POST)`
- `api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)`

7. In response to POST, PUT, and PATCH requests, your API should return the object that was added or changed.

### Required conditions in completing an objectives:
- work with Post model via ModelViewSet.
- Do not use third party libraries like Nested Routers or its equivalents.

## Installation:

1. Clone project:
```
git clone https://github.com/mrblessk/api_yatube.git
```

2. Open project directory:
```
cd api_yatube
```

3. Install virtual environment using Venv:
```
python<version> -m venv <virtual-environment-name>
```

4. Activate virtual environment:
```
source venv/Scripts/activate
```

> for deactivating:
> `deactivate`

5. Uprade pip:
```
python -m pip install --upgrade pip
```

6. Install requirements:
```
pip install -r requirements.txt
```

7. Make migrations:
```
python yatube_api/manage.py makemigrations
python yatube_api/manage.py migrate
```

8. Create superuser:
```
python yatube_api/manage.py createsuperuser
```

9. Remove comment from this line:
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

10. Сomment out this line: 
```
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

11. Make static collection:
```
python yatube_api/manage.py collectstatic
```

12. Create the file `.env`, in deirectory `..yatube_api/yatube_api`, with this content:
```
SECRET_KEY='Ваш секретный ключ'
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True
```

13. Dont forget adding to `.gitignore`: `.venv` and `.env` files

## Usage

1. For running tests use `pytest` (run from root directory).
2. For running project:
```
python yatube_api/manage.py runserver localhost:80
```

> The project will be available at the following: http://localhost/

3. Create content (posts, groups, comments) through http://localhost/admin
