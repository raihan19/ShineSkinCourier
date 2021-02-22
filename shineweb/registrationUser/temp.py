# import os
# from dotenv import load_dotenv
# from pathlib import Path
#
# env_path = Path('/home/raihan/PycharmProjects/ShineSkin/.env')
# load_dotenv(dotenv_path=env_path)
#
# print(os.getenv('EMAIL_USER'))
# print(os.environ.get('EMAIL_PASS'))



'''Another'''

# import pandas as pd
# from .models import Voltage
# import os
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "API499.settings")
#
#
# class insertion:
#     def insert(self):
#         data = pd.read_excel('/home/raihan19/Downloads/phase2/864287038320618/DeviceLogData_864287038320618_01-12-2018_20-08-2019.xls')
#
#         entry = [None] * data.shape[0]
#
#         for i in range(data.shape[0]):
#             entry[i] = Voltage(oldVoltage=data.Voltage[i])
#             entry[i].save()
