#Moduł subprocess zastępuje: os.system(), os.spawn*(), commands.*(), os.popen*(), popen2.*() oferując nam wyższym model
# abstrakcji i większą wygodę wykorzystania. Omówimy tu dwie funkcje, jedna to call, druga Popen. Różnica polega na tym,
# że pierwsza powoduje wykonanie liniowe wywoływanej komendy w ramach wątku naszej aplikacji, druga generuje osobny
# proces w systemie operacyjnym.


import subprocess
result=subprocess.call(['ping' ,'-n','2','onet.pl'])
print(f"result={result}")
print('koniec subprocess.call')

#result=0 brak błędu


result=subprocess.Popen(['ping','-n','2','onet.pl'])
print('koniec Popen i instrukcji pliku')
print(result.communicate())
