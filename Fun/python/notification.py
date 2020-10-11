# python -m pip install plyer
from plyer import notification

notification.notify(
                    title='Programa',
                    message='Wadi daidzine', 
                    app_name='Test.py', 
                    app_icon=None, 
                    timeout=10, 
                    ticker='hello world', 
                    toast=True
)