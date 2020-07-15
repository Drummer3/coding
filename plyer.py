# python -m pip install plyer
from plyer import notification

notification.notify(
                    title='Title',
                    message='This is message', 
                    app_name='Test.py', 
                    app_icon=None, 
                    timeout=10, 
                    ticker='hello world', 
                    toast=True
)