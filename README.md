# FastAPI_Tournament
Simple service for organization tournaments

Цель проекта: Управление турнирами, игроками, командами и автоматический расчет рейтинга участников на основе результатов матчей.

### Installation
- Clone repository
- Create and activate virtual environment in working directory
```
$ virtualenv .env
// (for Python 3.8 and later versions)
$ source .venv/bin/activate
// (for Windows: .\venv\Scripts\activate)
```
- Install dependencies and required libraries
```
--(env)$ pip install "fastapi[standard]"--
--(env)$ pip install sqlmodel psycopg2-binary--

```
### Using
- Run local server
```
(env)$ fastapi dev app/app.py
```
If run is successful, you will receive something like that:
```
   FastAPI   Starting development server 🚀
 
             Searching for package file structure from directories with __init__.py files
             Importing from C:\Users\p_korneev_test\Desktop\for_education\PythonTest\FastAPI_Tournament\app
 
    module   🐍 app.py
 
      code   Importing the FastAPI app object from the module with the following code:

             from app import app

       app   Using import string: app:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories: ['C:\\Users\\p_korneev_test\\Desktop\\for_education\\PythonTest\\FastAPI_Tournament']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [10432] using WatchFiles
      INFO   Started server process [12040]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
```